"""
Explaination for the problem can be found at:

https://math.stackexchange.com/questions/1307287/random-uniformly-distributed-points-in-a-circle

https://programming.guide/random-point-within-circle.html

http://www.anderswallin.net/2009/05/uniform-random-points-in-a-circle-using-polar-coordinates/

https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly


"""

import math
import random
import matplotlib.pyplot as plt

x_val = []
y_val = []

for i in range(10**5):
	r = math.sqrt(random.random())
	theta = 2*math.pi*random.random()

	x = r*math.sin(theta)
	y = r*math.cos(theta)

	x_val.append(x)
	y_val.append(y)

plt.plot(x_val, y_val, '.')
plt.show()
plt.axis('equal')