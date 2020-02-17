def calc_probab(m, n, k):
	rec_rec = n*(n-1)/((m+n+k)*(m+n+k-1))
	rec_het = m*n/((m+n+k)*(m+n+k-1))
	het_het = m*(m-1)/(4*(m+n+k-1)*(m+n+k))

	return 1 - rec_rec - het_het - rec_het


fin = open("rosalind_iprb.txt")
[k, m, n] = list(map(int, fin.readline().split()))
print (calc_probab(m, n, k))
fin.close()