import matplotlib.pyplot as plt
import random


def func(x):
	val = 4*x**3
	return val


s = 0
for i in range(ini, end):
	x = random.random()
	y = random.random()

	if y <= func(x):
		s += 1
		plt.plot(x, y)

print ("val =", s/10**5)
plt.show()
