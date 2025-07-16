import string

def check_word(correct, incorrect, word, tries):
    guess = input('Guess a letter: ').lower()

    if len(guess) != 1:
        print('Guess ONE letter.')
    elif guess not in string.ascii_lowercase:
        print('Guess a LETTER.')
    elif guess in incorrect or guess in correct:
        print(f'You already guessed "{guess}"!')
    elif guess in word:
        correct.append(guess)
        print(f'"{guess} is in the word.\n')
    else:
        incorrect.append(guess)
        tries += 1
        print(f'"{guess}" is NOT in the word.\n')

    return tries

check_word(['x'], ['t'], 'the', 0)
