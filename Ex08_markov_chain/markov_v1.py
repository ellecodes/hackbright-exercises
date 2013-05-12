import sys 
import random

def main():
    args = sys.argv
    # Change this to read input_text from a file
    script, filename = args
    f = open(filename)
    input_text = f.read()
    f.close()
    
    return make_chains(input_text)

def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    for line in text:
        words = text.split()

    print words
    
    d = {}

    d[words[0:1]] = append(words[2])

    print d

    for i in range(len(words) - 2):
        # creates key1 and key2
        k = (words[i], words[i + 1])
        # creates value, based on 
        v = words[i + 2]
    
        #determine in word already in dictionary
        markov[k[0:1]] = append(k[2])
        print markov

        if k not in markov.keys():
            markov.setdefault(k, 1)
        # otherwise, add the value to the dictionary
        else:
            #add the value as a list item to the dictionary key
            markov[k[0:1]] = append(k[2])

    # return markov

    # for key, value in markov():
    #     print '%s %r' % (key, value)

    print make_chains()

def make_text():
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #select a starting point(a key from frequency table)
    #print it?
    #randomly select another state to go to (the next word)
    #next word chosen is dependent on frequency
    #use new word as key and start over
    
    # random key from list
    # random.choice() returns a random choice from non-empty sequence
    # starting_point = random.choice(story)
    # print starting_point
    
    # while i in starting_point < 10:
    #     return starting_point
    
make_text()
        
    # convert tuple into a list
    # random_list = [ ]
    # random_list = random_list + list(starting_point)
    
    #
    
    
    # EXAMPLE OF LIST
    # story = [humpty, dumpty = sat; dumpty, sat = on; sat, on = a; on, a = wall; a, wall = humpty; wall, humpty = dumpty; humpty, dumpty = had; dumpty, had = a]
    # here, we have 2 examples of humpty, dumpty as key
    # this comes the most often, so this key should be included
        # we can include this by having a counter of instances?
        # for whatever comes up with highest/maximum, print?
    # QUESTION: if we have frequency of key, do we then also look for frequency of value? and if values equal in frequency, do we print the key with all its values?

     # chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

if __name__ == "__main__":
    main()