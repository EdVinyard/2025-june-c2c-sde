import spider as sd
import functions as md
import time
import os

correct = []            # List of correct letters guessed
incorrect = []          # List of incorrect letters guessed
incorrect_count = 0     # Number of incorrect guesses
game_in_progress = True

print('YOUR IMPROVED WELCOME MESSAGE GOES HERE.')

word = md.generate_word()

while game_in_progress:
    incorrect_count = md.check_word(correct, incorrect, word, incorrect_count)
    time.sleep(1)
    md.clear_screen()
    progress = md.print_word(word, correct)
    print(f'Word: {progress}')
    sd.print_spider(incorrect_count)
    print(f'Incorrect Guesses: {incorrect}')

    # Call your functions in the right order.

    # Check win and lose conditions here.
