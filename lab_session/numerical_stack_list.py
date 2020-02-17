class Stack():
	def __init__(self, val = []):
		self._value = val
		print("Stack initialised!")

	def push(self):
		x = int(input("Enter number to be pushed: "))
		self._value.append(x)
		print ("{} is pushed into stack!!!".format(x))

	def pop(self):
		if len(self) > 0:
			self._value.pop()
			print ("Values popped")
		else:
			print ("Underflow - List is EMPTY!!!")

	def __len__(self):
		val = 0
		for i in self._value:
			val += 1

		return val

	def is_Empty(self):
		if len(self) == 0: 
			print ("The list is EMPTY!!!")
			return True
		else:
			print ("List isn't empty")
			return False

	def __repr__(self):
		string = ""
		for i in self._value:
			string = string + str(i) + "\t"
		return string
