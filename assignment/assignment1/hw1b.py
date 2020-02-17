#BT3051 Assignment 1b
#Roll number: BE17B007
#Collaborators: -
#Time: 2 hours

import sys
import doctest

def read_FASTA(fname):
	""" (str) -> (list of tuples) 
	
	Input:
	fname		name of the file that is to be read

	Output:
	sequences	tuple of sequence names and sequences

	Working:
	data 		Used to store the complete data inside the file.
				The information is stripped and split
	names		List of names of all the fasta sequences (without the '>')
	seqs 		List of all the sequences (it can read the file even in the presence of new lines in between)
	"""

	with open(fname) as fin:
		data = fin.read().strip().split()
	
	names = [i[1:] for i in data if i[0] == '>']
	
	seqs = []
	seq = ""
	for i in data:
		if i[0] == '>':
			if seq != "":
				seqs.append(seq)
				seq = ""
			pass
		else:
			seq += i
	seqs.append(seq)

	sequences = [(name, seq) for name, seq in zip(names, seqs)]
	return sequences # a list of (sequence_name , sequence) tuples

def complement(dnaStrand):
	"""
	Complements the input DNA strand using Base pairing rules

	Input:
	dnaStrand 		DNA strand to be complemented

	Output:
	comp 			Complement of the input DNA strand
	"""
	complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
	comp = ""
	for i in dnaStrand:
		comp += complement[i]
	return comp[::-1]


def identify_orfs(dnaStrand):
	""" (str) -> (list of strings) 
	
	Input:
	dnaStrand 			Strand whose Open Reading Frame is to be found

	Output:
	frames 				List of all Open Reading Frames in dnaStrand

	Working:
	start 				List of start codons
	stop 				List of stop codons
	offsets 			To account for different reading frames
	seqs 				List of all possible sequences between start and stop codons
	calc_met			Calculates the number of start codons present in the already created strings
	element in frames 	Have a common Stop codon, spliced each time a start occurs
	"""

	start = ['ATG']
	stop=['TAG', 'TGA', 'TAA']
	offset = [0, 1, 2]
	frames = []
	n = len(dnaStrand)
	dnaStrands = [dnaStrand, complement(dnaStrand)]
	
	for dnaStrand in dnaStrands:
		for i in offset:
			end = n%3
			seq = ""
			flag = False

			for j in range(i, n-end, 3):
				codon = dnaStrand[j:j+3]
				if codon in start or flag == True:
					if codon in stop: 
						if seq!= "" and seq not in frames: 
							frames.append(seq)
						flag = False
						seq = ""
						pass

					else: 
						seq += codon
						flag = True

	for i in frames:
		calc_met = [j for j in range(0, len(i)-2, 3) if i[j:j+3] == 'ATG']
		if sum(calc_met)>1:
			for j in calc_met[1:]:
				if i[j:] not in frames: 
					frames.append(i[j:])

	return frames # a list of orf strings

def translate_DNA(dnaStrand,  translation_table = 'DNA_TABLE.txt'):
	""" 
	>>> translate_DNA('ATGTATGATGCGACCGCGAGCACCCGCTGCACCCGCGAAAGCTGA')
	'MYDATASTRCTRES'

	Input:
	dnaStrand 			DNA strand to be translated
	translation_table 	Matrix based on which translation takes place

	Output:
	protein 			Translated(amino acid) sequence of dnaStrand

	"""
	with open(translation_table) as f:
		data = f.read().strip().split()

	keys = [data[i] for i in range(len(data)) if i%2 == 0]
	values = [data[i] for i in range(len(data)) if i%2 == 1]
	prot_data = dict(zip(keys, values))	

	protein = ""
	n = len(dnaStrand)

	for i in range(0, n, 3):
		if prot_data[dnaStrand[i:i+3]] != 'Stop':
			protein += prot_data[dnaStrand[i:i+3]]
		else:
			break

	return protein

def compute_protein_mass(protein_string):
	""" 
	>>> compute_protein_mass('SKADYEK') 
	821.392

	Input:
	protein_string 			Protein string whose mass is to be calculated

	Output:
	mass 					Mass of protein_string

	Working:
	Mass of each amino acid is calculated using data from PROT_MASS.txt
	Then it is summed
	"""
	with open("PROT_MASS.txt") as fin:
		data = fin.read().strip().split()

	keys = [data[i] for i in range(len(data)) if i%2 == 0]
	values = [data[i] for i in range(len(data)) if i%2 == 1]
	mass_table = dict(zip(keys, values))

	mass =  0
	for i in protein_string:
		mass += float(mass_table[i])
	mass = float(round(mass, 3))
	return mass

if __name__ == '__main__': 
	#DO NOT CHANGE THE FOLLOWING STATEMENTS 
	for seq_name , seq in read_FASTA("hw1b_dataset.faa"): 
		print (seq_name+":")
		for orf in identify_orfs(seq):
			protein=translate_DNA(orf)
			print (protein,compute_protein_mass(protein))
			