# Homework Header as usual
#
#
#

import sys
import doctest

def read_FASTA(fname):
	""" (str) -> (list of tuples) 
	# function body with documentation
	"""
	return sequences # a list of (sequence_name , sequence) tuples

def identify_orfs(dnaStrand):
	""" (str) -> (list of strings) 
	# function body with documentation
	"""
	return frames # a list of orf strings

def translate_DNA(dnaStrand,  translation_table = 'DNA_TABLE.txt'):
	""" 
	# function body including documentation and test cases
	>>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
	MYDATASTRCTRES
	"""
	return protein # the protein string

def compute_protein_mass(protein_string):
	""" 
	#function body including documentation and test cases 
	>>> compute_protein_mass('SKADYEK') 
	821.392 
	"""
	return mass # the mass of the protein string as a float

if __name__ == '__main__': 
	#DO NOT CHANGE THE FOLLOWING STATEMENTS 
	for seq_name , seq in read_FASTA("hw1b_dataset.faa"): 
		print (seq_name+”:”)
		for orf in identify_orfs(seq):
			protein=translate_DNA(orf)
			print (protein,compute_protein_mass(protein))