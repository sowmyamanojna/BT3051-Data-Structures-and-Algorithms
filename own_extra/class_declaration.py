class Student():
	def __init__(self, name, rollno):
		self._name = name
		self._rollno = rollno
		self._existage = 0
		self._existmarks = 0

	def set_age(self, age):
		self._age = age
		self._existage = 1

	def set_marks(self, marks):
		self._marks = marks
		self._existmarks = 1

	def display(self):
		print(self._name)
		print(self._rollno)
		if self._existage:
			print(self._age)
		if self._existmarks:
			print(self._marks)


stud = Student("Name", "AA00A000")
stud.display()
print()

stud.set_age(20)
stud.display()
print()

stud.set_marks(100)
stud.display()