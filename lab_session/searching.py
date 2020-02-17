import random
import time
from random import randint
import matplotlib.pyplot as plt
from statistics import mean

def linear_search(s, x):
	n = len(s)
	flag = 0
	for i in range(n):
		if x == s[i]:
			flag = 1
			return i
	
	if flag == 0:
		return -1


def binary_search(s):
	x = s[-1]
	n = len(s)
	flag = 0
	beg = 0
	end = n-1

	while (beg <= end):
		mid = (beg + end)//2

		if s[mid] == x:
			flag = 1
			return mid

		elif (s[mid] > x):
			end = mid -1

		else:
			beg = mid + 1

	if flag == 0:
		return -1


if __name__ == '__main__':
	t_lin = []
	t_bin = []
	ran = []

	for j in range(49, 1001):
		s = [randint(1, 1001) for k in range(1, j+1)]
		x = s[-1]

		t_start_bin = time.perf_counter()
		binary_search(s)
		t_end_bin = time.perf_counter()
		t_bin.append((t_end_bin - t_start_bin) * 1000)

		t_start_lin = time.perf_counter()
		s.sort()
		linear_search(s, x)
		t_end_lin = time.perf_counter()
		t_lin.append((t_end_lin - t_start_lin) * 1000)
		
		ran.append(j)

	t_avg_lin = mean(t_lin)
	t_avg_bin = mean(t_bin)

	plt.figure()
	plt.plot(ran, t_lin, label = 'Linear')
	plt.plot(ran, t_bin, label = 'Binary')
	plt.legend(loc = 'best')
	plt.show()