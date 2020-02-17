def phyth(n):
	vals = [(i, j, k) for i in range(1, n+1) for j in range(i, n+1) for k in range(j, n+1) if i**2 + j**2 == k**2 ]
	print (vals)
	return vals

resp = 'y'
while True:
	n = int(input("Enter the number: "))
	vals = phyth(n)
	resp = input("Conti? (y/n): ")
	if resp == 'n':
		break

