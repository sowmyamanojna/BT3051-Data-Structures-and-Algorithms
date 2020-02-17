from random import randint
import time
import matplotlib.pyplot as plt

def multiply(data):
	n = len(data)

	for i in range(n):
		for j in range(i, n):
			data[i]*data[j]

size = [x for x in range(1, 400)]
t = []
for n in size:
	print (n)
	data = [randint(1, 10001) for i in range(n)]
	time_beg = time.perf_counter()
	multiply(data)
	time_end = time.perf_counter()
	t.append(time_end - time_beg)

scale = 5*10**(-8)
vals = [scale*x*(x-1)/2 for x in range(1, 400)]

plt.figure()
plt.plot(size, t)
plt.plot(size, vals)
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()