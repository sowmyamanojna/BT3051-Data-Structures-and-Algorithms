with open('nums.txt') as f:
	x = f.readlines()
	print (x)
	for line in x:
		print (line.strip())
		z = f.readline()
		print (z)

print (f.readline())