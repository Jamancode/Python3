class student:

	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0 - 100

	def get_grade(self):
		return self.grade	



class klassen:
	def __init__(self, name, max_studenten):
		self.name = name
		self.max_studenten = max_studenten
		self.studenten = []


	def add_student(self, student):
		if len(self.studenten) < self.max_studenten:
			self.studenten.append(student)
			return True
		return False	#
	
	def get_average_grade(self):
		value = 0 
		for student in self.studenten:
			value += student.get_grade()
		 return value / len(self.studenten)


s1 = student("tim", 19, 95)
s2 = student("bill", 19, 75)
s3 = student("Jill", 19, 65)

klassen = klassen("Science", 2)
klassen.add_student(s1)
klassen.add_student(s2)
print(klassen.get_average_grade())

