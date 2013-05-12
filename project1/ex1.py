import os
import sys

# Create a new dir for each letter of the alphabet
directories = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
directories = directories.split(' ')

for entry in directories:
	print entry
	os.mkdir(entry, 0777)

# Loop through files in original_files, sort each file into 
# appropriate directory (based on 1st letter)

