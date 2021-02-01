from random import randint

class Die():
	"""Models a die with sides number of faces."""
	
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll_die(self):
		print( str(randint(1, self.sides)) + " came up." )
		
six_sided_die = Die(6)
print('Rolling six-sided die 10 times')
for i in range(10):
	six_sided_die.roll_die();

ten_sided_die = Die(10)
print('Rolling ten-sided die 10 times')
for i in range(10):
	ten_sided_die.roll_die();

twenty_sided_die = Die(20)
print('Rolling ten-sided die 10 times')
for i in range(10):
	twenty_sided_die.roll_die();
