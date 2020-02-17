def pascal_triangle(n):
	if n >= 1:
		print ("1")
	if n >= 2:
		print ("1 1")
	a = [1, 1]
	for j in range(2, n):
		b = [1]
		for i in range(len(a)-1):
			b.append(a[i] + a[i+1])
		b.append(1)

		for i in b:
			print (i, end=" ")
		print()
		a = b

n = int(input('Enter number: \n>'))
pascal_triangle(n)

