#!/usr/bin/env python

import sys

def main():
    args = sys.argv
    # Change this to read input_text from a file
    script, filename = args
    f = open(filename)
    input_text = f.read()
    f.close()
    print input_text

    split_satan = input_text.split(" ")
    print split_satan


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    dictionary = {}

    for word in split_satan:
        if word in dictionary:
            # dictionary.setdefault(word,)
            # set this as key
    else:
        dictionary[word] += ""






def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."



     # chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

if __name__ == "__main__":
    main()
