def incrementList(a):
	b = a
	for i in range(len(b)):
		b[i] += 1

	return a

a = [1, 2, 3, 4]
print ("a:", a)
incrementList(a)
print (a)
