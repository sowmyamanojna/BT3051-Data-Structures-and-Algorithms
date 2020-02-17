#BT3051 Pop Quiz 1
#Roll number: BE17B007
#Name: N Sowmya Manojna
#Time: 30

"""
Dated: 30/08/2019
Define a minimalist BinaryNumber class to  represent binary 
numbers (use list beginning as the least significant bit), 
such that the following statement which access relevant class 
methods, return output as follows:

b1 = BinaryNumber([0, 1, 1, 1])
b2 = BinaryNumber([0, 0, 0, 1])
>>> print(b1)
[1110]_2
>>> print(b2)
[1000]_2
>>> print(b1.value() + b2.value())
22
>>> b3 = BinaryNumber([0, 1, 1, 2])
...
ValueError: Check your input!
"""

class BinaryNumber():
	""" Class to repersent a Binary Number """

	def __init__(self, val):
		""" Initialisation of a Binary Number """
		self._value = val
		if not self.check_validity():
			raise ValueError("Check your input!")

	def __repr__(self):
		""" Representation of the Binary Number """
		string = "["
		n = len(self._value)
		for i in range(n-1, -1, -1):
			string += str(self._value[i])
		string += "]_2"

		return string

	def value(self):
		"""" Calculates the decimal value of the Binary Number """
		val = 0
		for i, j in enumerate(self._value):
			val += 2**(i)*j
		return val

	def check_validity(self):
		""" Checks the validity of the Binary Number """
		for i in self._value:
			if i > 1 or i < 0 :
				return False
		return True

# b1 = BinaryNumber([0, 1, 1, 1])
# b2 = BinaryNumber([0, 0, 0, 1])
# print (b1)
# print (b2)

# print (b1.value() + b2.value())

# b3 = BinaryNumber([0, 1, 1, 2])