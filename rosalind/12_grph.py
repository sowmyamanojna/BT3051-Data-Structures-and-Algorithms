def compare_sim(names, dnas):
	matches = {}
	for i in names:
		matches[i] = []

	for i in range(len(dnas)):
		for j in range(len(dnas)):
			if i != j:
				if dnas[i][-3:] == dnas[j][:3]:
					matches[names[i]].append(names[j])


	for i in matches:
		if matches[i] != []:
			for j in matches[i]:
				print(i, j)

fin = open("rosalind_grph.txt")
data = fin.read().strip().split()
names = []
dnas = []
dna = ""

for i in data:
	if i[0] == ">":
		names.append(i[1:])
		if dna != "" :
			dnas.append(dna)
		dna = ""
	else:
		dna += i
dnas.append(dna)
compare_sim(names, dnas)