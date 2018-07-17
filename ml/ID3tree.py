from numpy import *
import math
import copy
import cPickle as Pickle
class ID3Tree(object):
	"""docstring for ID3Tree"""
	def __init__(self):
		self.tree = {}
		self.dataSet = []
		self.labels = []
	
	def loadDataSet(self, path, labels):
		recordlist = []		
		fp = open(path,'rb')
		content = fp.read()
		fp.close()
		rowlist = content.splitlines()
		recordlist = [row.split('\t') for row in rowlist if row.strip()]
		self.dataSet = recordlist
		self.labels = labels

	def train(self):
		labels = copy.deepcopy(self.labels)
		self.tree = self.buildTree(self.dataSet, labels)

	def buildTree(self, dataSet, labels):
		cateList = [data[-1] for data in dataSet]
		if cateList.count(cateList[0]) == len(cateList):
			return cateList[0]
		if len(dataSet[0] == 1:
			return self.maxCate(cateList)

		bestFeat = self.getBestFeat(dataSet)
		bestFeatLabel = labels[bestFeat]
		tree = {bestFeatLabel:{}}
		del(labels[bestFeat])
		uniqueVals = set([data[bestFeat]] for data in dataSet)
		for value in uniqueVals:
			subLables = labels[:]
			splitDataset = self.splitDataset(dataSet, bestFeat, value)
			subTree = self.buildTree(splitDataset, subLables)
			tree[bestFeatLabel][value] = subTree
		return tree

	def maxCate(self, cateList):
		items = dict([(catelist.count(i), i) for i in catelist])
		return items[max(items.keys())]

	def getBestFeat(self, dataSet):
		numFeatures = len(dataSet[0]) -1
		baseEntropy = self.computeEntropy(dataSet)
		bestInfoGain = 0.
		bestFeature = -1

		for i in range(numFeatures):
			uniqueVals = set([data[i]] for data in dataSet)
			newEntrop = 0.
			for value in uniqueVals:
				subDataSet = self.splitDataset(dataSet, i, value)
				prob = len(subDataSet)/float(len(dataSet))
				newEntrop += prob*self.computeEntropy(subDataSet)
			infoGain = baseEntropy - newEntrop
			if infoGain > bestInfoGain:
				bestInfoGain = infoGain
				bestFeature = i
		return bestFeature

	def computeEntropy(self, dataSet):
		datalen = float(len(dataSet))
		cateList = [data[-1] for data in dataSet]
		items = dict([(i, cateList.count(i) for i in cateList)])
		infoEntorpy = 0.
		for key in items:
			prob = float(items[key])/datalen
			infoEntorpy -=prob*math.log(prob,2)

		return infoEntorpy

	def splitDataset(self, dataSet, axis, value):
		rtnList = []
		for featVec in dataSet:
			if featVec[axis] == value:
				rFeatVec = featVec[:axis]
				rFeatVec.extend(featVec[axis+1:])
				rtnList.append(rFeatVec)
		return rtnList

		