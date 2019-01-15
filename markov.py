"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string):
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

    for i in range(len(word_list)-2):
        key = (word_list[i],word_list[i+1])
        addition = word_list[i+2]
        if key in chains.keys():
            chains[key].append(addition)
            
        else:
            chains[key] = [addition]
            
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    current_key = choice(list(chains.keys())) # generates a tuple
    words.extend(list(current_key))
    while current_key in chains.keys():
        link = choice(chains[current_key]) # generates a string
        words.append(link)

        current_key = (current_key[1], link)

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
