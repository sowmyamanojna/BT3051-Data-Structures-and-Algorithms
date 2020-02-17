# from hw1a import Gene

def complement(string):
	complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
	comp = ""
	for i in string:
		comp += complement[i]
	return comp[::-1]


def orf(string, prot_data, start=['ATG'], stop=['TAG', 'TGA', 'TAA']):
	offset = [0, 1, 2]
	proteins = []
	n = len(string)
	strings = [string, complement(string)]
	
	for string in strings:
		for i in offset:
			end = (n-i)%3
			seq = ""
			flag = False
			# print("offset:", i)
			for j in range(i, n-end, 3):
				# print(j)
				codon = string[j:j+3]
				if codon in start or flag == True:
					# print(codon)
					if codon in stop: 
						if seq!= "" and seq not in proteins: 
							proteins.append(seq)
						flag = False
						seq = ""
						# print(seq)
						# print(codon)
						pass

					else: 
						seq += prot_data[codon]
						# print(codon)
						# print(seq)
						flag = True
					# print(seq)
			# print()
	# print(proteins)
	calc_sub_met(proteins)

def calc_sub_met(proteins):
	for i in proteins:
		calc_met = [j for j in range(len(i)) if i[j] == 'M']
		if sum(calc_met)>1:
			for j in calc_met[1:]:
				if i[j:] not in proteins: 
					proteins.append(i[j:])

	for i in proteins:
		print(i)



f = open('dna_table.txt')
data = f.read().strip().split()
f.close()

keys = [data[i] for i in range(len(data)) if i%2 == 0]
values = [data[i] for i in range(len(data)) if i%2 == 1]
prot_data = dict(zip(keys, values))

fin = open('rosalind_orf.txt')
data = fin.read().strip().split()
fin.close()

string = ""
for i in data:
	if i[0]!='>': string += i

orf(string, prot_data)