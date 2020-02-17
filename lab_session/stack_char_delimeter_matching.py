from character_stack import CharStack

# a = '{[2*(x+y)]+3}'
LEFT_SET = '[{('
RIGHT_SET = ']})'

def check_delimeter_match(a):
	c = CharStack()

	for i in a:
		if i in LEFT_SET:
			c.push(i)
		elif i in RIGHT_SET:
			if c.len() == 0:
				return False
			elif RIGHT_SET.index(i) != LEFT_SET.index(c.pop()):
				return False

	if c.len() > 0:
		return False

	return True

A = input("Enter a paranthesised string: \n> ")
if check_delimeter_match(A):
	print ("The string is properly paranthesised")
else:
	print ("Re-check paranthesization")
