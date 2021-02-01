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

from car import Car		
from battery import Battery

# Note, on line 53, we are passing in the parent class as a parameter to the child class
class ElectricCar(Car):
	"""Represent aspects of a car, speicific to electric vehicles."""
	
	def __init__(self, make, model, year, battery=Battery()):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		#self.battery_size = 70
		#self.battery = Battery()
		self.battery = battery
		
	def fill_gas_tank(self):
		"""Electric cars do not have gas tanks."""
		print("This car does not need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2021, Battery(85))
print( my_tesla.get_descriptive_name() )
#print( my_tesla.battery_size )
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

























