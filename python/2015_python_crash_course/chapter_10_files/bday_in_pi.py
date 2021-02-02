file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
	pi_string = ''
	lines = file_object.readlines()
	for line in lines:
		pi_string += line.strip()
		
while True:
	birth_date = input("Enter your birth date as mmddyy: ")
	if birth_date == 'q':
		break
	
	index = pi_string.find(birth_date)
	if index >= 0:
		print("Your birth date starts at " + str(index) + "-th digit in pi.")
	else:
		print("Sorry, the first million digits of pi do not contain your birth date, may be try with more digits!")
