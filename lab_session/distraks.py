# from ArrayStack import ArrayStack
from CharStack import CharStack

operator = CharStack()
operand = CharStack()

lefty = '{[('
righty = '}])'
operators = '+-*/'
char = input("Enter parenthesised string: \n>").split()

for i in char:
	if i in lefty:
		pass
	
	elif i in righty:
		a = float(operand.pop())
		b = float(operand.pop())
		optr = operator.pop()
		
		if optr == '+':
			operand.push(b+a)
		elif optr == '-':
			operand.push(b-a)
		elif optr == '*':
			operand.push(b*a)
		elif optr == '/':
			operand.push(b/a)

	elif i in operators:
		operator.push(i)
		
	else:
		operand.push(i)

print(operand.pop())
# ( ( 22 + 656565 ) - 2 )