class Complex():

	def __init__(self, x, y):
		self.real = x
		self.img = y

	def __repr__(self):
		return str(float(self.real)) + ' + ' + str(float(self.img)) + 'j'


	def __add__(self, other):
		result = Complex(0, 0)
		result.real = self.real + other.real
		result.img = self.img + other.img
		return result

	def __mul__(self, other):
		result = Complex(0, 0)
		result.real = self.real*other.real - self.img*other.img
		result.img = self.real*other.img + self.img*other.real
		return result

	def __abs__(self):
		return (self.real**2 + self.img**2)**0.5

if __name__ == '__main__':
	a = Complex(0, 1)
	b = Complex(0, 1)
	print (a*b)
	print (a+b + Complex(3, 5))
	print (abs(a))