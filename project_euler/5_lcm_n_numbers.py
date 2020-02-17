"""


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


"""


import math

def find_primes(n):
	primes = [2]
	for i in range(3, n+1):
		flag = 0
		for j in range(2, i//2 + 1):
			if i % j == 0:
				flag = 1
				break
		if flag == 0:
			primes.append(i)
	
	return primes

def find_max_powers(n, primes):
	vals = {}
	for i in primes:
		for j in range(1, int(math.log(n, i)+1)):
			if i**(j+1) >= n:
				vals[i] = j

	return vals

def calc_lcm(vals):
	lcm = 1
	for i in vals:
		lcm *= i**vals[i]

	return lcm


resp = 'y'
while resp == 'y':
	n = int(input("Enter number: "))
	primes = find_primes(n)
	print (primes)
	print (len(primes))
	vals = find_max_powers(n, primes)
	for i in vals:
		print (i, vals[i])
	lcm = calc_lcm(vals)
	print (lcm)
	resp = input("Conti? (y/n): ")