import random

# Prompts user for letter guess. Checks through the secret word to see if it
# contains the letter guessed by the user. Returns the number of wrong guesses
# Takes in the correct letter list, incorrect letter list, secret word and the
# number of tries as parameters.
def check_word(correct, incorrect, word, incorrect_count):
    # TODO: Write this function.
    return incorrect_count


# Returns the word to the console containing "_" for any letter not yet guessed
# by the user.  Takes in the correct word and the list of correct guesses.
def print_word(word, correct_guesses):
    # TODO: Write this function.
    return '_ ' * len(word)


# Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
    word_list = open('words.txt').read().split()
    word = random.choice(word_list)
    blanks = '_ ' * len(word)
    print('Word = ' + blanks)
    return word


# Put the introduction code/input player name into here
def introduction():
    pass


def clear_screen():
    pass
