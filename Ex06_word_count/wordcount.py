from sys import argv

script, filename = argv

#open the file
opened_file = open(filename)
txt = opened_file.read()
opened_file.close()

#count how many times each space-separated word occurs
for line in txt:

    lower_text = txt.lower()

    separated_text = lower_text.split()

    stripped_list = []
        
    for i in separated_text:
	    strip_word = i.strip('?.,')
	    stripped_list.append(strip_word)

dictionary = {}

for word in stripped_list:
	if word not in dictionary:
		dictionary.setdefault(word, 1)

	else:
		dictionary[word] += 1

#for word in stripped_list:
#	word_instance = stripped_list.count(word)
#	dictionary.setdefault(word, word_instance)

for key, value in dictionary.iteritems():
	print '%s %r' % (key, value)

