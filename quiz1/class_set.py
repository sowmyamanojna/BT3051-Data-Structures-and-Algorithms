class Set():
	def __init__(self, val=[]):
		self._value = val
		self._value = self.get_unique()

	def get_unique(self):
		uvals = []
		for i in self._value:
			if i not in uvals:
				uvals.append(i)

		return uvals

	def __sub__(self, other):
		n = max(len(self._value), len(other._value))
		result = Set()
		result._value = [i for i in self._value if i not in other._value]

		return result

	def __repr__(self):
		string = str(self._value)
		return string

a = Set([1, 2, 2, 4, 6, 7, 7])
b = Set([2, 2, 2])

print(a)
print(b)
print(a-b)
