#import json
from json import dump

#numbers = [3, 1, 4, 1, 5, 9, 2]
numbers = [2, 7, 1, 8, 2]

file_name = 'numbers.json'
with open(file_name, 'w') as writer:
	#json.dump(numbers, writer)
	dump(numbers, writer)

