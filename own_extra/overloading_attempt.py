"""
OVERLOADING IS A BIG no no IN PYTHON!!!

Output:
# Attempted giving 3 arguments!

Traceback (most recent call last):
  File "overloading_attempt.py", line 39, in <module>
    stud.assign_values(rollnumber, degree)
TypeError: assign_values() takes 2 positional arguments but 3 were given

"""

class Student():
	"""docstring for student"""
	def __init__(self, name=None, rollno=None):
		self._name = name
		self._rollno = rollno
		self._val = 0
		

	def assign_values(self, rollno, degree):
		self._yearin = int(rollno[2:4]) + 2000
		n = 5 if degree.lower() == "dd" else 4
		self._yearout = self._yearin + n
		self._department = rollno[0:2]
		self._val = 1

	def assign_values(self, rollno):
		self._yearin = int(rollno[2:4]) + 2000
		self._department = rollno[0:2]
		self._val = 2

	def __repr__(self):
		string = ""
		string += self._name + "\n"
		string += self._department + " department\n"
		string += str(self._yearin)
		if self._val == 1:
			string += " - " + str(self._yearout)

		return string


resp = "y"
while resp == "y":
	name = input("Enter name: ")
	stud = Student(name)
	rollnumber = input("Enter rollnumber: ")
	degree = input("Enter degree: ")
	if rollnumber and degree:
		stud.assign_values(rollnumber, degree)
		print (stud)
	elif rollnumber and not degree:
		stud.assign_values(rollnumber)
		print (stud)
	else:
		print ("Plis to enter valid data!!")

	resp = input("Conti?(y/n): ").lower()