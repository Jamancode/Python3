class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age

d = Dog("Tim", 13)
d.set_age(23)
print(d.get_age())
