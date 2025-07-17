import random
import os

# Prompts user for letter guess. Checks through the secret word to
# see if it contains the letter guessed by the user. Returns the
# number of wrong guesses.  Takes in the correct letter list,
# incorrect letter list, secret word and the number of tries as
# parameters.
def check_word(correct, incorrect, word, tries):
    guess = input('Guess a letter: ')

    if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Guess just ONE LETTER.')
    elif guess in incorrect or guess in correct:
        print('You already guessed that!')
    elif guess in word:
        correct.append(guess)
        print(f'"{guess}" is in the word.\n')
    else:
        incorrect.append(guess)
        tries += 1
        print(f'"{guess}" is NOT in the word.\n')

    return tries


# Returns the word to the console containing "_" for any letter
# not guessed by the user.  Takes in the correct word and the
# list of correct guesses as parameters.
def hide_unguessed_letters(word, correct_guesses):
    result = ''
    for character in word:
        if character in correct_guesses:
            result = result + character
        else:
            result = result + '_'

    return result


# Opens the word list text file, stores the contents into a
# list, chooses a random word from the list, finds the length
# of that word and prints a string of blanks for each letter
# in the word. Returns the word.
def generate_word():
    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory, 'words.txt')
    word_file = open(file_path)
    file_content = word_file.read()
    all_words = file_content.split()
    word = random.choice(all_words)
    #print('Word: ' + '_' * len(word))
    return word


# Put the introduction code/input player name into here
def introduction():
    clear_screen()
    print(f'Welcome to ArachnoPhonics!')


def clear_screen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Mac OS, Linux
        os.system('clear')
