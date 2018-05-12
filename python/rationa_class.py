# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Ratina10:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def plus(self, another):
        den = self.den * another. den
        num = self.num*another.den + self.den*another.num
        return Ratina10(num, den)
    
    def print(self):
        print(str(self.num)+"/"+str(self.den))
        
    def print2(self):
        print("{0}/{1}".format(self.num, self.den))
        
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n%m, m
        return n
        

#r1 = Ratina10(3, 5)
#r2 = r1.plus(Ratina10(7,15))
#r2.print2()
#print(r1._gcd(100,33))
         
    
class Rational:
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n%m, m
        return n
    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self._num = sign*(num//g)
        self._den = den//g
        
    def num(self):
        return self._num
    def den(self):
        return self._den
    
    def __add__(self, another):
        den = self._den*another.den()
        num = self._num*another.den()+self._den*another.num()
        return Rational(num ,den)

    def __mul__(self, another):
    	return Rational(slef._num*another.num(), self._den*another.den())

    def __lt__():
    	return self.num*another.den() < self._den*another.num()

    def print(self):
        print(str(self.num)+"/"+str(self.den))

r1 = Rational(2,3)
print(r1._gcd(100,33))