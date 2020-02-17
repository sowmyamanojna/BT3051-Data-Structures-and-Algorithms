"""


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


"""


def ch_pr(n):
	flag = 0
	
	if n % 2 == 0:
		flag = 1
	
	for i in range(3, n//2 + 1, 2):
		if n % i == 0:
			flag = 1

	if flag == 1:
		return False
	else:
		return True

def pr_no(n, m):
	pr_div = [2]

	for i in range(3, n + 1, 2):
		if ch_pr(i) and len(pr_div) < m:
			pr_div.append(i)
			print(len(pr_div))
		elif len(pr_div) >= m:
			print("Breaking....")
			break

	if len(pr_div) < m:
		print ("Increase Number")

	return pr_div

resp = "y"
while  resp == 'y':
	n = int(input("Enter number: "))
	m = int(input('Enter length: '))
	pr_div = pr_no(n, m)
	print(pr_div)
	resp = input("Conti? (y/n)")

