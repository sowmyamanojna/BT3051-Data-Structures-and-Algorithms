def prtm(string, mass_table):
	mass =  0
	for i in string:
		mass += float(mass_table[i])

	return mass


fin = open("prot_mass.txt")
data = fin.read().strip().split()
fin.close()

keys = [data[i] for i in range(len(data)) if i%2 == 0]
values = [data[i] for i in range(len(data)) if i%2 == 1]
mass_table = dict(zip(keys, values))

fin = open("rosalind_prtm.txt")
string = fin.readline().strip()
print (prtm(string, mass_table))
fin.close()