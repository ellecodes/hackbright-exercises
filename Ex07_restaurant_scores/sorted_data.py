from sys import argv
script, filename = argv
f = open(filename)
captured_text = f.read().split("/n")
f.close()
print captured_text

dictionary = {}

for item in captured_text:
	clean_list = item.split(":")
	key_rest = clean_list[0]
	value_score = clean_list[1]
	dictionary[key_rest] = value_score

keys = dictionary.keys()
alpha_keys = sorted(keys)

for item in alpha_keys:	# for loop to run through 'alpha_keys' list
	rating = dictionary.get(item) # then create a variable that will stand for the value/rating..and 'get' the value that corresponds with the dictionary key for the item from 'alpha_list'
	print "Restaurant %s is rated %s." % (item, rating)
