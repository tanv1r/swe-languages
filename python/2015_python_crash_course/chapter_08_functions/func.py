#def greet_user():
#	"""Display a simple greeting"""
#	print( "Hello!" )

#greet_user()


#def favorite_book(title):
#	print( "One of my favorite books is " + title.title() )
#
#favorite_book( "Adevntures of Sherlock Holmes" )

#def get_formatted_name(first_name, last_name):
#	"""Return neatly formatted name"""
#	full_name = first_name + " " + last_name
#	return full_name.title()
#
#formatted_name = get_formatted_name( first_name = "mohammad", last_name = "tanviruzzaman" )
#print( formatted_name )

#def greet_users(names):
#	"""Print a simple greeting to each user in the list."""
#	for name in names:
#		message = "Hello, " + name.title() + "!"
#		print( message )
#		
#usernames = [ 'angshu', 'arpi', 'rizwana' ]
# This shows possible risk of being type-unsafe language
#greet_users( 'arpi' )

#def make_pizza(*toppings):
#	"""Make a pizza with toppings"""
#	print(toppings)
#
#make_pizza('pepperoni')
#make_pizza('pepperoni', 'olives')

#def build_profile(first, last, **user_info):
#	profile = {}
#	profile['first_name'] = first
#	profile['last_name'] = last
#	for key, value in user_info.items():
#		profile[key] = value
#	return profile
#
#user_profile = build_profile( 'albert', 'einstein',
#								location='princeton',
#								field='physics' )
#
#print( user_profile )

#import pizza
#pizza.make_pizza( 16, 'pepperoni' )

import pizza as p
p.make_pizza( 16, 'pepperoni' )

#from pizza import make_pizza
#make_pizza( 16, 'pepperoni' )

#from pizza import make_pizza as mp
#mp( 16, 'pepperoni' )
