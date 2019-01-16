"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    word_list = text_string.split()

    for i in range(len(word_list)-n_gram):
        key = []
        # creating a key of user specified length
        for n in range(n_gram):
            key.append(word_list[n+i])
        key_tuple = tuple(key) # converts to a tuple to make it immutable


        addition = word_list[i+n_gram]
        if key_tuple in chains.keys():
            chains[key_tuple].append(addition)
            
        else:
            chains[key_tuple] = [addition]
    return chains


def make_text(chains, n_gram):
    """Return text from chains."""

    words = []

    current_key = choice(list(chains.keys())) # generates a tuple
    #print('current key is:', current_key)

    # Checks if the first letter in current key is lowercase it will generate
    # a new key until it gets a capital letter

    while not current_key[0].isupper():
        current_key = choice(list(chains.keys()))

    words.extend(list(current_key))

    # keeps track of count to protect against an infinite loop
    count = 0

    punctuation = '!?.'
    
    while current_key in chains.keys() and count<5000:
        link = choice(chains[current_key]) # selects a value
        
        words.append(link)

        # make current key a list to allow edits
        current_key = list(current_key)
        current_key.append(link)
        current_key = tuple(current_key[1:])
        count += 1

        if link[-1] in punctuation:
            break

    return " ".join(words)


input_path = sys.argv[1]
n_gram = int(sys.argv[2])


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print(random_text)
