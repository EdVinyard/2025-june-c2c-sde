def check_word(correct, incorrect, word, incorrect_guess_count):
    player_guess = input('Guess a letter. ')

    # if the letter was already guessed
    #     Tell player they already guessed that
    # elif guess in word
    #     Tell player it is correct
    #     Add letter to correct list
    # elif guess not in word
    #     Tell player it is incorrect, add letter to incorrect list
    # else
    #     Tell player they did not guess a letter, please try again

    return incorrect_guess_count

wrong = ['x', 'y', 'z']
right = ['f', 'r']
wrong_count = 1
random_word = 'frank'
wrong_count = check_word(right, wrong, random_word, wrong_count)
print(f'You guessed wrong {wrong_count} times so far.')
