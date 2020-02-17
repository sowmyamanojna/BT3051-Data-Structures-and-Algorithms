'''

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def sum_square_diff(n):
	square_s = int(n*(n+1)*(2*n+1)/6)
	s_square = int((n*(n+1)/2)**2)
	diff = s_square - square_s
	print (diff)

	return diff

resp = 'y'
while resp == 'y':
	n = int(input("Enter n: \n>"))
	diff = sum_square_diff(n)
	resp = input("Conti? (y/n)")