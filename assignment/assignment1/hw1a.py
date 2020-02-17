#BT3051 Assignment 1a
#Roll number: BE17B007
#Collaborators: -
#Time: 15


def GC_content(gene):
	gc = [1 for i in gene.sequence if i in "GC"]
	gc = sum(gc)
	gc = gc*100/gene.length
	print("%0.1f" %(gc))


class Gene():
	"""
	Gene class with the following attributes:
	sequence	Actual gene sequence
	geneID		Gene sequence ID
	length		Length of the gene sequence

	>>> a=Gene("DNA1","AGCTGCATGTACGTAGTCA")
	>>> b=Gene("DNA2","TCATCGGTAGCAATTT")
	>>> GC_content(a)
	47.4
	>>> c=a+b
	>>> c.sequence
	'AGCTGCATGTACGTAGTCATCATCGGTAGCAATTT'
	>>> -a
	'TCGACGTACATGCATCAGT'
	"""
	def __init__(self, geneID = "", sequence = ""):
		self.geneID = geneID
		self.sequence = sequence
		self.length = len(sequence)

	def __add__(self, other):
		result = Gene()
		result.sequence = self.sequence + other.sequence
		result.length = self.length + other.length

		return result

	def __neg__(self):
		# result = Gene()
		complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
		comp = ""
		for i in self.sequence:
			comp += complement[i]
		# result.sequence = comp
		return comp