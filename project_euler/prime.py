""" 
Write code which divides the values and checks for primes after that

"""

def chpr(n):
	flag = 0
	for i in range(2, n//2 + 1):
		if n % i == 0:
			flag = 1
			break

	if flag == 0:
		return True
	else:
		return False

def prime_fact(m):
	pfact = []
	for i in range(2, m//2 + 1):
		if (m % i == 0) and chpr(i):
			pfact.append(i)

	return pfact


while True:
	n = int(input("Enter number: "))
	print (prime_fact(n))
	resp = input("Conti? (y/n)")
	if resp == 'n':
		break