"""
有理数类：
__add__，实现加法功能
_num,私有，用函数def num(self)，提供访问

"""     
    
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
    	return self._num*another.den() < self._den*another.num()

    def print(self):
        print(str(self._num)+"/"+str(self._den))

r1 = Rational(2,3)
r2 = Rational(1,2)
r = r1+r2
r.print()
