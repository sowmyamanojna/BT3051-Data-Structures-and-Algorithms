def shuffle(store_list, idx):
	n = store_list[0][-idx]
	for i in range(1, fact(i)):
		
		

def fact(n):
	f = 1
	for i in range(1,n+1):
		f *= i
	return f

def print_perm(n):
	total_no = fact(n)
	print (total_no)

	store_list = np.zeros((fact, n))
	store_list[0] = [i for i in range(1, n)]

	for i in range(1, total_no):
		shuffle(store_list, i)



f = open("rosalind_perm.txt")
n = f.readline().strip().split()
f.close()

n = int(n[0])
print (n)
print_perm(n)