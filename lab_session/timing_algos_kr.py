import time
#from linear_search import *
#from binary_search import *

def time_it(search_function , L, v):
	'''(function ,object ,value) --> number
	Time (in millseconds) how long it takes to run the
	search_function to find the value v in list L.
	'''
	t_begin = time.perf_counter()
	search_function(L,v)
	t_end = time.perf_counter()
	return int((t_end - t_begin) * 1000000)


def linear_search(array ,value):
	n = len(array)
	for i in range(n):
		if array[i] == value:
			return i
	return -1

def binary_search(array ,value):
	N = len(array)
	i = 0
	j = N - 1
	while i != j+1:
		mid = (i+j)//2
		if array[mid] < value:
			i = mid+1
		else:
			j = mid-1
	if 0 <= i < N and array[i] == value:
		return i
	else:
		return -1

if __name__ == '__main__':
	a = binary_search([2,2,2,6,6,6,7,89,100,101,2,3,4],100)
	b = linear_search([2,2,2,6,6,6,7,89,100,101,2,3,4],100)
	print(a, b)


	c = time_it(linear_search,[1,2,3,4,5,9,133,22,31,46],3)
	d = time_it(binary_search,[1,2,3,4,5,9,133,22,31,46],3)
	print (c, d)

	for prob_sz in [10**7]:
		test_list = list(range(prob_sz))
		for search_func in [linear_search ,binary_search]:
			for test_value in [0,prob_sz//2, prob_sz]:
				t = time_it(search_func, test_list, test_value)
				print (search_func.__name__, prob_sz, test_value, t*1000)