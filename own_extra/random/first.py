"""

A function to sum up all 
natural numbers till n

"""

def gauss(n):
	s = 0
	for i in range(1, n+1):
		s += i

	return s

n = input("Enter n: ")
s = gauss(n)
print s