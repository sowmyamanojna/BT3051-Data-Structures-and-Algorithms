import random
import matplotlib.pyplot as plt

pi_vals = []

pi = 0
n = 100
m = 10**6
for i in range(m):
	for j in range(n):
		[x, y] = [random.random(), random.random()]
		if x**2 + y**2 <= 1.0:
			pi += 1
	pi = (pi/n)*4

	pi_vals.append(pi)

itern = [i for i in range(m)]
plt.plot(itern, pi_vals, '.')
plt.show()