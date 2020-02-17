class Stack():
	def __init__(self, val = []):
		self._value = val
		# print("Stack initialised!")

	def push(self, x):
		self._value.append(x)
		# print ("{} is pushed into stack!!!".format(x))
		return self

	def pop(self):
		if len(self._value) > 0:
			self._value = self._value[1:]
			# print ("Values popped")
		else:
			print ("Underflow - List is EMPTY!!!")

		return self

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
			# print ("List isn't empty")
			return False

	def __repr__(self):
		string = ""
		for i in self._value:
			string = string + str(i) + "  "
		return string

	def top(self):
		return self._value[0]
