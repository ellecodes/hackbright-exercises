
# create a REPL for a calculator

while True:
	input = raw_input("> ")
	input = input.split(' ')
	if input[0] == 'q':
		break
	elif input[0] == '+':
		print add((int(input[1])), (int(input[2])))
		continue
	elif input[0] == '-':
		print subtract((int(input[1])), (int(input[2])))
		continue
	elif input[0] == '*':
		print multiply((int(input[1])), (int(input[2])))
		continue
	elif input[0] == '/':
		print divide((int(input[1])), (int(input[2])))
		continue
	elif input[0] == 'square':
		print square(int(input[1]))
		continue
	elif input[0] == 'cube':
		print cube(int(input[1]))
		continue
	elif input[0] == 'pow':
		print power((int(input[1])), (int(input[2])))
		continue
	elif input[0] == 'mod':
		print mod((int(input[1])), (int(input[2])))
		continue
	else:
		print "I don't understand that"
		continue

