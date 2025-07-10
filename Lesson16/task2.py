import random

def input_int(prompt):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Invalid integer: ' + s)

def number_guessing_game():
    game_active = True
    target_number = random.randint(1, 20)
    while game_active:
        guess = input_int('Guess a number. (1-20) ')

        if target_number == guess:
            print('You got it!')
            game_active = False
        elif guess > target_number:
            print('Too high.  Try again.')
        else:
            print('Too low.  Try again.')

if __name__ == '__main__':
    number_guessing_game()
