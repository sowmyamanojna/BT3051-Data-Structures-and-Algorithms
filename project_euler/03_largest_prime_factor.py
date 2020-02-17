def is_prime(n):
	for i in range(2, n//2 + 1):
		if n%i == 0:
			return False
	return True


def largest_prime_factor(n):
	i = 2
	lpf = []
	while n>=2:
		if n%i == 0 and is_prime(i):
			lpf.append(i)
			n = n//i
			if is_prime(n):
				lpf.append(n)
		i += 1

	return max(lpf)

print (largest_prime_factor(13195))
print (largest_prime_factor(600851475143))
