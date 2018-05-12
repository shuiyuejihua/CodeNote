'''
最小公倍数
LCM(a,b)=（a * b）/GCD(a,b)
a、b数的乘积除以a、b的最大公约数
'''
def lcm(a, b):
	mul_ab = a*b
	if mul_ab == 0:
		return 0	
	while b != 0:
		a, b = b, a%b
	return mul_ab//a

print("2,8的最小公倍数是：",lcm(2,8))
print("24,56的最小公倍数是：",lcm(24,56))

