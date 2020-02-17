def calc_mul_3_5(n):
	s = 0
	for i in range(1, n):
		if i % 3 == 0 or i % 5 == 0:
			s += i

	print s

	return s


s = calc_mul_3_5(1000)