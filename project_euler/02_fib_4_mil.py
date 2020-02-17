def calc_fib(a, b, n):
	s = 0
	while b<=n:
		if b%2 == 0:
			s += b
		a, b = b, a+b

	return s

print(calc_fib(1, 2, 90))
print(calc_fib(1, 2, 4*10**6))