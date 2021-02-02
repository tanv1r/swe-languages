#import json
from json import load

file_name = 'numbers.json'
with open(file_name) as reader:
	#numbers = json.load(reader)
	numbers = load(reader)

print(numbers)
