'''
python array
'''

class Array:
	"""docstring for Array"""
	def __init__(self, size =16):
		self.size = size
		self.iterms = [None]*size
		self.logic_size = 0

	def __setitem__(self, index, value):
		self.iterms[index] = value
		self.logic_size += 1
		if self.logic_size>=3*self.size//4:
			temp = Array(2*self.size)
			for i in range(logic_size):
				temp[i] =self.iterms[i]
			self.iterms = temp

	def __getitem__(self, index):
		return self.iterms[index]

	def __str__(self):
		return str(self.iterms)

	def __len__(self):
		return self.size

	def __iter__(self):
		for i in self.iterms:
			yield i
