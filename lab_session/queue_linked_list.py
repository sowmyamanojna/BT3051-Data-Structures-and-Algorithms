class Queue():

	def __init__(self, val=0):
		self._val = val
		self._top = None
		self._bottom = None

	def enqueue(self):
		new_val = float(input("Enter the number to be pushed: "))
		new_node = Queue(new_val)
		self._bottom = new_node
		new_node._top = self

		return self

	def dequeue(self):		
		if len(self)==0 or self==None:
			print("Underflow - Queue is empty")
		else:
			self = self._bottom

		return self

	def top(self):
		print(self._val)
		return self._val

	def __len__(self):
		a = self
		count = 0
		# print (a._val)
		while a!=None:
			a = a._bottom
			count += 1

		return count

	def __repr__(self):
		string = ""
		for i in range(len(self)):
			string += str(self._val) + " "
			self = self._bottom

		return string


if __name__ == '__main__':
	resp = "y"
	n = float(input("Enter number to initialise the queue with: "))
	q = Queue(n)
	while resp == "y":
		inp = int(input("What operation do you want to perform?\n1 Enqueue \n2 Dequeue \n3 Display \n4 Length \n5 Peep: "))
		if inp == 1:
			q.enqueue()
		elif inp == 2:
			if q!=None:
				q = q.dequeue()
			else:
				print("Underflow is reached!!")
		elif inp == 3:
			print(q)
		elif inp == 4:
			if q!=None:
				len(q)
			else:
				print("EMPTY Queue!!")
		elif inp == 5:
			q.top()
		else:
			print("Enter valid number")

		resp = input("Conti? (y/n): ").lower()
