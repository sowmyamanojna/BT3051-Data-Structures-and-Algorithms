def splice(dna, introns):
	for i in introns:
		while i in dna:
			dna = dna.replace(i, "")
	
	return dna

def translate_protein(exons, prot_data):
	prot = ""
	for i in range(0, len(exons)-2, 3):
		prot += prot_data[exons[i:i+3]]

	return prot[:-4]


f = open('dna_table.txt')
data = f.read().strip().split()
f.close()

keys = [data[i] for i in range(len(data)) if i%2 == 0]
values = [data[i] for i in range(len(data)) if i%2 == 1]
prot_data = dict(zip(keys, values))

f = open('rosalind_splc.txt')
data = f.read().strip().split()
f.close()

dna = ""
introns = []
intron = ""

for l in range(1, len(data)):
	if data[l][0] == ">":
		break
	else:
		dna += data[l]

for i in range(l, len(data)):
	if data[i][0] == ">":
		if intron != "":
			introns.append(intron)
			intron = ""
	else:
		intron += data[i]
introns.append(intron)

print (dna)
print (introns)

exons = splice(dna, introns)
print (exons)
print (exons == dna)
print (translate_protein(exons, prot_data))
