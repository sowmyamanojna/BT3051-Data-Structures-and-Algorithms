class Stack():
	def __init__(self, val = None):
		self.top = None;
		self.next_node = None
		self.val = val
		self.len = 1

	def push(self):
		data = int(input("Enter number to be pushed: "))
		print ("Pushing {0}...".format(data))
		new_node = Stack(data)
		new_node.next_node = self
		self.top = new_node
		self.len += 1

		return new_node

	def pop(self):
		if self.len>=1:
			print("Popping ...")
			self.len -= 1
			self = self.next_node

		return self

	def print_stack(self):
		if self == None:
			print ("Underflow")
		while self != None:
			print (self, end = "\t")
			self = self.next_node

	def __repr__(self):
		return str(self.val)

	def get_len(self):
		if self!=None:
			return self.len
		elif self==None:
			return 0	


mapper = {
	1:"push",
	2:"pop",
}

resp = 'y'
beg_data = int(input("Enter the initial value of the stack element: "))
a = Stack(beg_data)
print ("Current stack: ", a)

while resp == 'y':
	function = int(input("What do you wanna do? \n1 Push\n2 Pop \n3 Length: "))
	if function == 1:
		new_stack = a.push()
		a = new_stack

	elif function == 2:
		if a != None:
			new_stack = a.pop()
			a = new_stack
		else:
			print ("Under flow")

	elif function == 3:
		print (a.get_len())
	
	if a != None:
		a.print_stack()
	else:
		print ()

	resp = input("\nConti? (y/n) ")