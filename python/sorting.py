
"""
排序算法小结
"""

# 冒泡排序
def bubble_sort(array):
	for i in range(len(array)):
		flag = False
		for j in range(1, len(array)-i):
			if 	array[j-1] > array[j]:
				array[j], array[j-1] = array[j-1], array[j]
				flag = True
		if 	flag == False:
				break
	return array



def bubble_sort2(array):
	for i in range(len(array)-1):
		for j in range(len(array)-1-i):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
	return array

# 冒泡排序测试
a = [2,4,1,4,3,5,10,4,6]

# 选择排序
def select_sort(array):
	for i in range(len(array)-1):
		k = i
		for j in range(i, len(array)):
			if array[j] < array[k]:
				k = j
		if k != i:
			array[i], array[k] = array[k], array[i]
	return array

def test_sort(fun, array):
	lst = array[:]
	print(fun(lst))

#test_sort(select_sort,a)

# 插入排序
# 从2号位置拿出来一个数，然后和前面的循环比较，移动位置
def insert_sort(array):
	for i in range(1, len(array)):
		x = array[i]
		j = i
		while j > 0 and array[j-1] > x:
			array[j] = array[j-1]
			j -= 1
		array[j] = x
	return array

test_sort(insert_sort, a)