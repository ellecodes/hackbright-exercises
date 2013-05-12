
numbers = []

def function(z):
	i = 0
	for i in range (0, z):
		print "At the top of i is %d" % i
		numbers.append(i)

		
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

print function(1)

print "The numbers: "


for num in numbers:
	print num