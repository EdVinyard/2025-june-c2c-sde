import time

spiderList = []

def check_word():
    pass # TO DO

def print_word(word, correct):
    pass # TO DO

def print_spider(incorrect_count, spider_list):
    pass # TO DO

def clear_screen():
    pass # TO DO

word = 'frank'              # for testing; should be chosen randomly
correct = []                # correct letters guessed
incorrect = []              # INCORRECT letters guessed
game_in_progress = True     # quit when False

# ask for name; print intro statements

while game_in_progress:
    incorrect_count = check_word(correct, incorrect, word)
    time.sleep(1)
    clear_screen()
    progress = print_word(word, correct)
    print(f'Word = {progress}')
    print_spider(incorrect_count, spiderList)
    print(f'Incorrect Guesses = {incorrect}')

    # Call your functions in the right order here.

    # Check win and lose conditions here.
