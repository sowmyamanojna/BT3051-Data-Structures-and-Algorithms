sequence = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", 
			"UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
			"UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
			"UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
			"UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
			"UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
			"UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A", 
			"UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A", 
			"UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D", 
			"UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D", 
			"UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
			"UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
			"UGU":"C","CGU":"R", "AGU":"S", "GGU":"G",
			"UGC":"C","CGC":"R", "AGC":"S", "GGC":"G",
			"UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
			"UGG":"W","CGG":"R", "AGG":"R", "GGG":"G"}

def prot(string):
	prot_seq = [sequence[string[3*i:3*(i+1)]] for i in range((len(string) - 4)//3 + 1)]
	prot_seq_string = ""
	for i in prot_seq:
		prot_seq_string += i

	return prot_seq_string

fin = open("rosalind_prot.txt")
string = fin.read().strip()
print (prot(string))