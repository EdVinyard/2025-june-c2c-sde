'''
This is a guess-the-word game where the user guesses one letter at a time.

After each turn, you'll see a picture of a spider materializing.  Every time you
guess a letter that is NOT in the word, more of the spider will be visible.  If
you run out of guesses, the spider will get you!
'''
import os
import random
import spider

INTRODUCTION = __doc__
DIRECTORY = os.path.dirname(__file__)

def hide_unguessed_letters(target_word: str, guessed_letters: list[str]) -> None:
    '''
    Prints the word to the console containing "_" for any letter not guessed by
    the user. Takes in the correct word and the list of correct guesses as
    parameters.

    For example, given the word "red" and the guessed letters `['e','x']`, this
    function returns "_e_".
    '''
    result = ''

    for letter in target_word:
        if letter in guessed_letters:
            result += letter
        else:
            result += '_'

    return result

def random_word():
    '''
    Returns a random word from the words.txt file.
    '''
    wordList = open(os.path.join(DIRECTORY, 'words.txt')).read().split()
    word = random.choice(wordList)
    return word

def has_user_won(target_word: str, guesses: list[str]) -> bool:
    for letter in target_word:
        if letter not in guesses:
            return False

    return True

def input_letter(guessed: list[str], prompt: str) -> str:
    is_invalid_guess = True
    while is_invalid_guess:
        letter = input(prompt).lower()

        if len(letter) != 1:
            print('You must guess just a single letter.')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('You must guess a LETTER.')
        elif letter in guessed:
            print('You already guessed "' + letter + '".')
        else:
            is_invalid_guess = False

    return letter

def print_guesses_remaining(max_incorrect_guess_count, incorrect_guess_count):
    remaining_guess_count = max_incorrect_guess_count - incorrect_guess_count

    if remaining_guess_count > 1:
        guess_or_guesses = 'guesses'
    else:
        guess_or_guesses = 'guess'

    print(str(remaining_guess_count) + ' ' + guess_or_guesses + ' remain.')

def extra_space(string):
    '''
    adds a space between each letter of the supplied string

    For example, given "RED", returns "R E D".
    '''
    last_char_index = len(string) - 1
    with_extra_space = ''
    for index, character in enumerate(string):
        with_extra_space += character

        if index < last_char_index:
            with_extra_space += ' '

    return with_extra_space

def word_contains_letter(word, letter):
    for l in word:
        if l == letter:
            return True

    return False

def print_guesses(guessed_letters):
    if len(guessed_letters) > 0:
        guess_str = ''
        for letter in guessed_letters:
            guess_str += letter

        print('You have guessed: ' + extra_space(guess_str.upper()))

def main():
    guessed_letters = []
    MAX_INCORRECT_GUESS_COUNT = 6
    incorrect_guess_count = 0
    word = random_word()
    continue_game = True

    print(INTRODUCTION)

    while continue_game:
        spider.print_spider(incorrect_guess_count)
        print('     ' + extra_space(hide_unguessed_letters(word, guessed_letters)))
        print()
        print_guesses_remaining(MAX_INCORRECT_GUESS_COUNT, incorrect_guess_count)
        print_guesses(guessed_letters)
        letter_guess = input_letter(guessed_letters, 'Guess a letter. => ')
        guessed_letters.append(letter_guess)

        if word_contains_letter(word, letter_guess):
            print('Correct!  "' + letter_guess + '" is in the word.')
        else:
            print('Sorry, "' + letter_guess + '" is not in the word.')
            incorrect_guess_count += 1

        if has_user_won(word, guessed_letters):
            continue_game = False
            print('You win!  The word is "' + word + '".')
        elif incorrect_guess_count >= MAX_INCORRECT_GUESS_COUNT:
            continue_game = False
            spider.print_spider(incorrect_guess_count)
            print('You lose.  The word was "' + word + '".')

if __name__ == '__main__':
    main()
