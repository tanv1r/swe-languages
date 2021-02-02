print("Enter 'q' to exit.")
while True:
	try:
		first_number_str = input( 'Enter first integer: ' )
		
		if first_number_str == 'q':
			break
		
		first_number = int( first_number_str )
		
		second_number_str = input( 'Enter second integer: ' )
		
		if second_number_str == 'q':
			break
		
		second_number = int( second_number_str )
		
		sum_of_two = first_number + second_number
	except ValueError:
		print('Please enter two valid integers.')
	else:
		print( 'Sum is ' + str(sum_of_two) )
