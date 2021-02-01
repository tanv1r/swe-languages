from collections import OrderedDict

# glossary = {
	# 'variable'  : 'an alias for storage',
	# 'string'    : 'a seqeunce of characters',
	# 'list'      : 'a sequence of items',
	# 'dictionary': 'a set of key/value pairs',
	# 'class'     : 'a model of real world idea'
# }

glossary = OrderedDict()

glossary['variable'] = 'an alias for storage'
glossary['string'] = 'a seqeunce of characters'
glossary['list'] = 'a sequence of items'
glossary['dictionary'] = 'a set of key/value pairs'
glossary['class'] = 'a model of real world idea'

glossary['inheritance'] = 'extending an already modeled idea'
glossary['attribute'] = 'storage for a class'
glossary['method'] = 'function for a class'

for key, value in glossary.items():
	print( key + ": " + value )
