class Queue():

	def __init__(self, val):
		self._val = val

	def push(self):
		val = int(input("Enter values to be pushed: "))
		self._val.append(val)
		print("{} has been pushed!!!".format(val))

	def pop(self):
		if len(self._val) > 0:
			A = self._val[0]
			self._val = self._val[1:]
			print ("Value has been popped from the queue!!!")
			return A
		else:
			print ("Underflow - Array is empty")


	def __len__(self):
		return len(sel._val)

	def top(self):
		return sel._val[0]

	def __repr__(self):
		string = ""
		for i in self._val:
			string += str(i) + " "

		return string

	def is_empty(self):
		if len(self) == 0:
			return True
		return False

if __name__ == '__main__':

	# A = input("Enter array list to be stored in a queue: ")
	# A = A.split()
	q = Queue()

	resp = "y"
	while resp == "y":
		inp = int(input("Enter function to be performed: \n1 Push \n2 Pop \n3 Display \n4 Top \n5 is_empty: "))
		if inp == 1:
			q.push()
		elif inp == 2:
			q.pop()
		elif inp == 3:
			print(q)
		elif inp == 4:
			q.top()
		elif inp == 5:
			q.is_empty()
		else:
			print("Enter valid number :D")

		resp = input("Conti?(y/n): ").lower()