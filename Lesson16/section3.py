import os
import random

def generate_word():
    '''
    Returns a random word from the words.txt file.
    '''
    word_file = open('words.txt')    # open() returns a file object
    print(str(word_file) + '\n' )
    file_content = word_file.read()  # all the text from the whole file
    print(file_content[:50] + '...\n')
    word_list = file_content.split() # one line of the file in each list item
    print(str(word_list[:10]) + '...\n')
    word = random.choice(word_list)  # one word, chosen at random
    return word

word = generate_word()
print(word)
