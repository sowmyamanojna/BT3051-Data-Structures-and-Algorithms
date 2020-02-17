def fib(n, count):
	count += 1

	if n == 1:
		return 1
	elif n==2 or n==3:
		return n
	else:
		return fib(n-2, count) + fib(n-1, count)

count = 0
print(fib(10, count))
print(count)