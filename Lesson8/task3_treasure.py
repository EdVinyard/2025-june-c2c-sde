import random


treasure_row = str(random.randint(0, 4))    # string
treasure_col = str(random.randint(0, 4))    # string
#print(treasure_row, treasure_col) # for debugging

guess_row = ''                              # string
guess_col = ''                              # string

while guess_row != treasure_row or guess_col != treasure_col:
    guess_row = input('In what row is the treasure?     (0-4) ')
    guess_col = input('In what columnn is the treasure? (0-4) ')

    if guess_row != treasure_row or guess_col != treasure_col:
        print('No treasure there, sorry!  Try again.')

print('You found the treasure!')
