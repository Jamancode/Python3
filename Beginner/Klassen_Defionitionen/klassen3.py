class Pet:
	def __init__ (self, name, age):
		self.name = name
		self.age = age
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I dont know waht i say")

class Cat(Pet):
	def speak(self):
		print("Meow")	

class Dog(Pet):
	def speak(self):
		print("wooff")

p = Pet("Tim", 23)
p.speak()
c = Cat("Bill", 42)
c.speak()
d = Dog("Jill", 13)
d.speak()