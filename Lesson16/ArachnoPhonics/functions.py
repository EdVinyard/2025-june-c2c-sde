import random

# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
# Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word():
    pass

# Returns the word to the console containing "_" for any letter not guessed by the user.
# Takes in the correct word and the list of correct guesses as parameters
def print_word():
    pass

# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.
def print_spider(tries, spiderList):
    spiderList[tries]()

# Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
    wordList = open('words.txt').read().split()
    word = random.choice(wordList)
    print('Word = ' + '_'*len(word))
    return word

# Put the introduction code/input player name into here
def introduction():
    pass
