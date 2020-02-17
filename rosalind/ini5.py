fin = open("rosalind_ini5.txt", 'r')

text = fin.read().split("\n")

for i in range(1,len(text),2):
	print text[i]