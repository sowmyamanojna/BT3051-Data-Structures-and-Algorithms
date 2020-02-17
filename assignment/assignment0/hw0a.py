"""
#BT3051 Assignment 0a
#Roll number: BE17B007
#Collaborators: -
#Time: 3
"""

name = input("Enter your name: \n>")
age = float(input("Enter your age: \n>"))
if age >= 18.0:
	print ("%s, you are eligible to apply for a driver’s license." %(name))
else:
	print ("%s, you are not eligible to apply for a driver’s license." %(name))