def calc_pos(dna, temp):
	n = len(dna)
	m = len(temp)
	pos = []
	for i in range(n-m+1):
		if dna[i:i+m] == temp:
			pos.append(i+1)
	return pos

fin = open('rosalind_subs.txt')
dna = fin.readline().strip()
temp = fin.readline().strip()

pos = calc_pos(dna, temp)
for i in pos:
	print (i, end = " ")
print()

fin.close()