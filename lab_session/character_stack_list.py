class CharStack():
	def __init__(self):
		self._char = []

	def __repr__(self):
		return str(self._char)

	def push(self, char):
		self._char.append(char)

	def len(self):
		return len(self._char)

	def pop(self):
		if len(self._char) == 0:
			print("Underflow")
			return 0
		return self._char.pop()
		
