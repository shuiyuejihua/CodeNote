# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:19:34 2018

@author: shui
"""
import heapq

def heapsort(l):
    h = []
    for v in l:
        heapq.heappush(h,v)
    print(h[0])
    return [heapq.heappop(h) for i in range(len(h))]

#print(heapsort([2,1,8,3,5]))
#b = [5,2,1,4,3]
#heapq.heapify(b)
#print(b)

m = [[1,3,4,5],[2,3,4,5],[3,3,4,5],[4,3,4,5]]
n = list(*m)
print(n)













   