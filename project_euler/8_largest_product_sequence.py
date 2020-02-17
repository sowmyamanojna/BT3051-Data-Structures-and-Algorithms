s = input("Enter number: ")

n = len(s)

max_prod = 1
for i in s[:13]:
	max_prod *= int(i)

for i in range(n-12):
	val = s[i:i+13]
	prod = 1
	for i in val:
		prod *= int(i)
	if max_prod < prod:
		max_prod = prod

print (max_prod)