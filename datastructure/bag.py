# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:10:59 2018

@author: shui
"""

class Bag:
    
    def __init__(self, size=None):
        self._size = size
        self.item = []
        
    def add(self, value):
        if len(self)>self._size:
            raise Exception('Full')
        self.item.append(value)
        
    def remove(self, value):
        return self.item.remove(value)
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        for i in self.item:
            yield i
            
a = [21,10,4,1,3,5]
b = a.copy
a.sort()
print(len('2134'))
