import time
import random

def linear_search(numbers, value):
	for i in range(len(numbers)):
		if numbers[i] == value:
			return i

	return -1

def binary_search(numbers, value):
	n = len(numbers)
	beg = 0
	end = n
	while beg <= end:
		mid = (beg+end)//2
		if numbers[mid] == value:
			return mid
		elif numbers[mid] > value:
			end = mid-1
		else:
			beg = mid+1

	return -1

a = [random.randint(1, 1001) for i in range(1001)]
a.sort()

t_beg = time.perf_counter()
print (linear_search (a,1))
t_end = time.perf_counter()
print ("linear_search:", t_end-t_beg)

t_beg = time.perf_counter()
print (linear_search (a,5))
t_end = time.perf_counter()
print ("linear_search:", t_end-t_beg)

t_beg = time.perf_counter()
print (binary_search (a,1))
t_end = time.perf_counter()
print ("binary_search:", t_end-t_beg)

t_beg = time.perf_counter()
print (binary_search (a,5))
t_end = time.perf_counter()
print ("binary_search:", t_end-t_beg)