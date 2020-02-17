from sympy import isprime

sm = 0
for i in range(2*10**6-1, 1, -2):
# for i in range(10-1, 1, -2):
	if isprime(i):
		sm += i
sm += 2

print (sm)
