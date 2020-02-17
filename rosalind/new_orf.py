def complement(string):
	mapping = {"A":"T", "T":"A", "C":"G", "G":"C"}
	complement = ""

	for i in string:
		complement += mapping[i]
	complement = complement[::-1]
	return complement


def codon_to_amino(string, prot_data):
	strings = [string, complement(string)]
	offsets = [0, 1, 2]
	n = len(string)

	prots = []
	for string in strings:
		each_string = []
		for i in offsets:
			each_offset = []
			end = (n-i)%3
			for j in range(i, n-end, 3):
				codon = string[j:j+3]
				each_offset.append(prot_data[codon])
			print(each_offset)

			each_string.append(each_offset)
		print(each_string)
			
		prots.append(each_string)

	get_all_str(prots)

def get_all_str(prots):

	for each_string in prots:
		for each_offset in each_string:
			count_met = [j for j in range(len(each_offset)) if each_offset[j] == "M"]
			count_ends = [j for j in range(len(each_offset)) if each_offset[j] == "Stop"]

			print(count_met)
			print(count_ends)

			for i in count_met:
				print("i:", i)
				strings = []
				num_of_stops = len(count_ends)

				if num_of_stops == 1:
					j = count_ends[0]
					print("j:", j)
					if i<j:
						data = each_offset[i:j]
						string = ""
						for k in data:
							string += k
						if string not in strings:
							print(string)
							strings.append(string)
				else:
					for j in range(len(count_ends)):
						print("i:", i)
						print(count_ends[j])
						string = ""
						if (i<count_ends[j]) and (i>count_ends[j-1]):
							data = each_offset[i:count_ends[j]]
							for k in data:
								string += k
							if string not in strings:
								print(string)
								strings.append(string)

	for i in strings:
		print (i)

	return strings


fin = open("dna_table.txt")
data = fin.read().strip().split()
fin.close()

keys = [data[i] for i in range(len(data)) if i%2 == 0]
values = [data[i] for i in range(len(data)) if i%2 == 1]
prot_data = {}
for i in range(len(keys)):
	prot_data[keys[i]] = values[i]

fin = open("rosalind_orf.txt")
data = fin.read().strip().split()
fin.close()

string = ""
for i in range(1, len(data)):
	string += data[i]

codon_to_amino(string, prot_data)