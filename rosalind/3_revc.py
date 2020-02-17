


fhand = open('rosalind_revc.txt')
dna = fhand.readline().strip()
cs = ""
val = {
        "A" : "T",
        "T" : "A",
        "G" : "C",
        "C" : "G"
}

for i in range(len(dna)-1, -1, -1):
    print (i)
    cs += val[dna[i]]

print (cs)
fhand.close()
