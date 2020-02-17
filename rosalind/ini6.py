fin = open("rosalind_ini6.txt", 'r')
s = fin.read()
s = s.split()
d = {}

for i in s:
	d[i] = 0

for i in s:
	d[i] += 1

for i in d:
	print i, d[i]