def rev_str(x):
	n = len(x)
	b = [x[i] for i in range(n-1, -1, -1)]
	y = ""
	for i in b:
		y += i
	print (y)
	return y

resp = 'y'
while resp == "y":
	x = input("Enter string: ")
	y = rev_str(x)
	resp = input("Conti? (y/n): ").lower()