#BT3051 Assignment 0b
#Roll number: BE17B007
#Collaborators: -
#Time: 3


n = int(input("Enter a number: \n>"))
for i in range(1, n+1):
	for j in range(i):
		print ((j+1)**i, end = " ")
	print()