fhand = open("rosalind_hamm.txt")
data = fhand.read().split()

s = 0
for i, j in zip(data[0], data[1]):
	if i != j:
		s += 1

print (s)