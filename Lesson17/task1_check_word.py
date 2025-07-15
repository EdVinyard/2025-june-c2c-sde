correct_guesses = []
incorrect_guesses = []

def input_letter(guessed, prompt):
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

def check_word(correct, incorrect, word, guess_count):
    all_guesses = correct + incorrect # concatenate the lists
    letter = input_letter(all_guesses, 'Guess another letter. => ')
    if letter in word:
        print(f'"{letter}" is in the word.')
        correct.append(letter)
    else:
        print(f'"{letter}" is NOT in the word.')
        incorrect.append(letter)

    return guess_count + 1

guess_count = check_word(['t'], ['x'], 'the', 1)
