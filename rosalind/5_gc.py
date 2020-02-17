def calc_gc_cont(x):
	num = 0
	for i in x:
		if i == "G" or i == "C":
			num += 1

	return [num, len(x)]


fhand = open("rosalind_gc.txt")
data = fhand.read().split()
print (data)

val = []
st = []
for i in data:
	if i[0] == '>':
		val.append(st)
		st = [i]
	if i[0] != '>':
		st.append(i)
val.append(st)

val = val[1:]
print (val)

dna = []
fasta = []
st = ""
for i in val:
	st = ""
	for j, k in enumerate(i):
		if j != 0:
			st += k
		else:
			fasta.append(k)
	dna.append(st)

for i, j in zip(dna, fasta):
	print(j)
	print (i)

gc = []
for i in dna:
	gc.append(calc_gc_cont(i)[0]/calc_gc_cont(i)[1])

v = max(gc)
print(v)
i = gc.index(v)
print (i)

print (gc)
print (fasta[i][1:])
print (gc[i]*100)