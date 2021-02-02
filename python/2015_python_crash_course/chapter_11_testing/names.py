from name_function import get_formatted_name

print("Enter 'q' to quit.")

while True:
	first = input( "Please enter the first name: " )
	if first == 'q':
		break
	
	last = input('Please enter the last name: ')
	if last == 'q':
		break
	
	formatted_name = get_formatted_name(first, last)
	print("Neatly formatted name: " + formatted_name + ".") 
