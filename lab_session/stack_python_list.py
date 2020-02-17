from numerical_stack import Stack

resp = "y"
l = list(map(int, input("Enter initial values: ").split()))
print (l)
a = Stack(l)

while resp == "y":
	n = int(input("Enter function to be performed: \n1 Display \n2 Push \n3 Pop \n4 isEmpty check: "))

	if n == 1:
		print (a)
	elif n == 2:
		a.push()
	elif n == 3:
		a.pop()
	elif n == 4:
		a.is_Empty()

	resp = input("Conti? (y/n):").lower()


# 1 2 54 511 21552132 1213 1321 3213 213215 321 321 2121