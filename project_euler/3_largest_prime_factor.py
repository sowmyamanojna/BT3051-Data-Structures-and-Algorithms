"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import sympy

def largest_prime_factor(n):
	prime_nos = []
	for i in range(2, int(n/2)):
		if n % i == 0 and sympy.isprime(i):
			prime_nos.append(i)
			print (prime_nos)

	return prime_nos

print (max(largest_prime_factor(600851475143)))
