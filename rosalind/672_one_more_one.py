def g(n):
	no_ones = 0
	while n != 1:
		if n%7 == 0:
			n /= 7
		else:
			n += 1
			no_ones += 1

	return no_ones

def s(n):
	sm = 0
	for i in range(1, n+1):
		sm += g(i)

	return sm

def h(k):
	value = int((7**k-1)/11)
	return s(value)

print(h(10**9)%1117117717)
