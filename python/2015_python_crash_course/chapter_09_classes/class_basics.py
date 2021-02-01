# class Dog():
	# """A simple attempt to model a dog"""
	
	# # appears having to write self in every method definition
	# # is unnecessary work!
	# def __init__(self, name, age):
		# """Initialize name and age attributes."""
		# self.name = name
		# self.age = age
	
	# def sit(self):
		# """Simulate a dog sitting in response to a command."""
		# print(self.name.title() + " is now sitting.")
		
	# def roll_over(self):
		# """Simulate a dog rolling over in response to a command."""
		# print(self.name.title() + " rolled over!")
		
# my_dog = Dog('tommie', 6)

# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

# my_dog.sit()
# my_dog.roll_over()

class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back an odometer.")
	
	def increment_odometer(self, miles):
		self.odometer


























