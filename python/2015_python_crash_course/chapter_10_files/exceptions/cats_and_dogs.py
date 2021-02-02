cat_file = 'cats.txt'
dog_file = 'dogs.txt'

try:
	with open(cat_file) as cat_file_object:
		cat_names = cat_file_object.readlines()
except FileNotFoundError:
	#print(cat_file + " could not be found.\n")
	pass
else:
	print('Cat names are:')
	for name in cat_names:
		print(name)
	try:
		with open(dog_file) as dog_file_object:
			dog_names = dog_file_object.readlines()
	except FileNotFoundError:
		print( dog_file + " could not be found." )
	else:
		print('Dog names are:')
		for name in dog_names:
			print(name)
