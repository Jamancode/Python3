class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name
	def get_age(self):
		return self.age

d = Dog("Tim", 13)
print(d.get_age())
d2 = Dog("Bill", 42)
print(d2.get_name())
d3 = Dog("Susi", 23)
print(d3.get_name())