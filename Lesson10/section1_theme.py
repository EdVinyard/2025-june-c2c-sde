import random

ROOM = [
    'xxxxx',
    'x...x',
    'x.xpx',
    'x.xex',
    'xxxxx',
    ]

def puzzles():
    # Choose a door
    correct_door = random.choice(['1', '2', '3'])
    door = input('Choose a door. (1, 2, or 3) ')

    while door != correct_door:
        print('You did not escape :(')
        door = input('Choose a door. (1, 2, or 3) ')

    print('You enter an empty dark room...')
    print()
    print('There is something glowing in the corner. ')

    possible_passwords = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']
    correct_password = random.choice(possible_passwords)

    for word in possible_passwords:
        if word == correct_password:
            print(word + ' 😉')
        else:
            print(word)

    print('You see a computer terminal asking for a password.')
    password_guess = input('Enter the password. ')

    while password_guess != correct_password:
        print('Incorrect password! Try again!')
        password_guess = input('Enter the password. ')

    print('The computer begins to glow.')
    print('The wall in front of you sinks into the ground...')
    print('revealing a getaway space craft!')

def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col

    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1
    else:
        print('invalid direction: ' + direction)

    if ROOM[new_row][new_col] == 'x':
        print('Ouch! You bump into a wall.')
        new_row = current_row
        new_col = current_col

    return new_row, new_col

def announce_walls(r, c):
    if ROOM[r-1][c] == 'x':
        print('There is a wall up from you.')
    if ROOM[r+1][c] == 'x':
        print('There is a wall down from you.')
    if ROOM[r][c-1] == 'x':
        print('There is a wall left from you.')
    if ROOM[r][c+1] == 'x':
        print('There is a wall right of you.')

def welcome():
    name = input('What is your name? ')
    print('----------------------------------------------------------------------')
    print('''
                                .-.
            .-""`""-.    |(@ @)
        _/`oOoOoOoOo`\_ \ \-/
        '.-=-=-=-=-=-=-.' \/ \
        `-=.=-.-=.=-'    \ /\
            ^  ^  ^       _H_ \
    ''') # from https://www.asciiart.eu/space/aliens by JGS
    print('Welcome to the INTERGALACTIC Escape Room, ' + name + '!')
    print('We do not expect much from a puny earthling...')
    print('but we will give you a chance to escape.')
    print('----------------------------------------------------------------------')

welcome()
row, col = 3, 1
print('position: ' + str(row) + ', ' + str(col))
announce_walls(row, col)

while ROOM[row][col] != 'e':
    direction = input(
        'Which direction will you move? (up, down, left, right) ')
    row, col = move(row, col, direction)
    print('position: ' + str(row) + ', ' + str(col))

    if ROOM[row][col] == 'p':
        puzzles()

    announce_walls(row, col)

print('You escaped!')
