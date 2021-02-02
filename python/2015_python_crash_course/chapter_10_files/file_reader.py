# looks like the using statement in C#
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	# item in contents is a character
	# item in file_object is like a line of string
	#contents = file_object.read()
	#contents.rstrip()
	#print(contents)
	#for line in file_object:
	#	print(line)
	lines = file_object.readlines()
	#for line in lines:
	#	print(line)
	pi_string = ''
	for line in lines:
		pi_string += line.strip()
	
	print(pi_string)
