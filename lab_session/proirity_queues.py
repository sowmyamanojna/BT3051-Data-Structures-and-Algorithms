class Queue():

	def __init__(self):
		self._val = []
		self._priority = []

	def enqueue(self):
		val = int(input("Enter values to be enqueued: "))
		self._val.append(val)
		prior = int(input("Enter priority of the value: "))
		self._priority.append(prior)
		print("{0} has been pushed with priority as {1}!!!".format(val, prior))

	
	def dequeue(self):
		if len(self._val) > 0:
			# A = self._val[0]
			a = self._priority.index(max(self._priority))
			A = max(self._priority)
			self._val.remove(self._val[a])
			self._priority.remove(self._priority[a])
			print(self._val)
			print(self._priority)
			print ("Value has been dequeued from the queue!!!")
			
			return A
		
		else:
			print ("Underflow - Array is empty")


	def __len__(self):
		return len(sel._val)

	def top(self):
		return sel._val[0]

	def __repr__(self):
		string = ""
		for i, j in zip(self._val, self._priority):
			string += "(" + str(i) + ", " + str(j) + ")"

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
		inp = int(input("Enter function to be performed: \n1 Enqueue \n2 Dequeue \n3 Display \n4 Top \n5 is_empty: "))
		if inp == 1:
			q.enqueue()
		elif inp == 2:
			q.dequeue()
		elif inp == 3:
			print(q)
		elif inp == 4:
			q.top()
		elif inp == 5:
			q.is_empty()
		else:
			print("Enter valid number :D")

		resp = input("Conti?(y/n): ").lower()