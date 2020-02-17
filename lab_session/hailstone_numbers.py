def hailstone_numbers(n):	
	h = [n]
	while True:
		if n%2 == 0:
			n = n//2
			h.append(n)
		else:
			n = 3*n + 1
			h.append(n)

		if n == 1:
			break

	return h

n = int(input("Enter the number: "))
print (hailstone_numbers(n))