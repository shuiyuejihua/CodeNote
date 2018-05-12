'''
牛顿迭代法求平方根：
牛顿迭代法：
求f(x)=0的根
Xn+1 = Xn - f(Xn)/f`(Xn)
f`(x)位f(x)的导数

求y的平方根x：y=x**2
f(x) = x**2 - y
令f(x) = 0
f`(x) = 2x
x = x-(x**2 - y)/2x
即：
x = (x - y/x)/2
'''
def ntmethod(y):
	x = 1.
	while abs(x*x - y) > 1e-6 :	#判断条件，停止迭代
		x = (x + y/x)/2
	return x 

print("9的平方根是：",ntmethod(9))
print("9的平方根是：{:<.4f}".format(ntmethod(9)))
print("5的平方根是：",ntmethod(5))
print("5的平方根是：{:.4f}".format(ntmethod(5)))