#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    split_text = corpus.split()
    # print split_text
    dictionary = {}

    # i wanna take the first and second items in the list 'split_text' and assign them as the keys in the dictionary. then i wanna take the third item in the list 'split_text' and assign it as the value in the dictionary.
    for i in range(0, len(split_text) - 2):
        # this tuple will be used as a key in the dictionary. to create a tuple, just add ()
        key = (split_text[i], split_text[i + 1])
        # problem: dictionary values are being overwritten when there are duplicate keys
        # solution: create an if/else statement that says if key already exists, append new value to existing value; else add key & value
        value = split_text[i + 2]
        dictionary[key] = [value]
    # print dictionary
    return dictionary

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # create an empty list that will house the end product
    # to start, get a random key from dictionary(chains), and add it to the empty list as the first two items in the list (first word in tuple as first item in list, second word in tuple as second item in list)
    #   
    # if the key has multiple values, get a random item from the list of values
    # print as list
    # then take the last two items in the list as a key, then print the value
    return "Here's some random text."

def main():
    # first: review all variables provided in skeleton, then work back from there.
    # remember lists vs. strings vs. objects
    args = sys.argv
    # print args
    filename = args[1]
    # print filename

    # Change this to read input_text from a file
    input_text = open(filename).read() #.read() to take contents of file & convert to string
    # print input_text

    chain_dict = make_chains(input_text)
    # print chain_dict

    # random_dict = {"key": "value"}
    # new_text = make_text(random_dict)

    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()

# '=' assignment, not equation
# assigning variables to call other functions into main
# write out pseudo code for what make text function does

# make_text - 
# mashup - string + append string
# twitter - character limit