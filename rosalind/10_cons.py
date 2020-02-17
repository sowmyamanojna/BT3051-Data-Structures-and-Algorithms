import numpy as np

def calc_frequency(dnas):
	n = len(dnas)
	m = len(dnas[0])
	profile = {
				"A" : [0]*m,
				"C" : [0]*m,
				"G" : [0]*m,
				"T" : [0]*m
				}

	for i in dnas:
		for j in range(m):
			profile[i[j]][j] += 1
	return profile

def get_array(profile):
	count = []
	for i in nuc:
		count.append(profile[i])

	count = np.array(count)
	count = np.transpose(count)
	count = count.tolist()
	return count


def get_consensus(profile):
	count = get_array(profile)
	n = len(count[0])
	m = len(count)
	nuc = ['A', 'C', 'G', 'T']
	mapping = dict(zip(list(range(4)), nuc))

	consensus = ""
	for i in count:
		consensus += mapping[i.index(max(i))]
	return consensus

fin = open('rosalind_cons.txt')
dnas = []
data = fin.read().split()
n = len(data)
dna = ""
for i in data:
	if i[0] == ">":
		if dna != "":
			dnas.append(dna)
			dna = ""
	else:
		dna += i
dnas.append(dna)

nuc = ['A', 'C', 'G', 'T']
profile = calc_frequency(dnas)
consensus = get_consensus(profile)

print (consensus)
for i in nuc:
	print(i, ":", sep = "", end = " ")
	for j in profile[i]:
		print (j, end = " ")
	print()
