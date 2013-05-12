from sys import argv
import string
import os

script, filename = argv

book = open(filename)                                                                                                     
text = book.read()

l_text = text.lower()
alphabet = string.ascii_lowercase
l_alphabet = list(alphabet)
"""
print l_text
print alphabet
print l_alphabet
"""
for i in l_alphabet:
	print i
	print l_text.count(i)





