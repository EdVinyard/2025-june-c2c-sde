import random

ROOM = [
    'xxxxx',
    'x.pex',
    'x...x',
    'x...x',
    'xxxxx',
    ]

def puzzle():
    name = input('What is your name? ')

    #custom theme = space
    print(f'Welcome to the INTERGALACTIC Escape Room, {name}!')

    door = input('Please choose a door (1, 2, or 3): ')

    correct_door = random.choice(['1', '2', '3'])

    while door!= correct_door:
    door = input('Nope, try again! 1, 2, or 3 ')

    #intro to password puzzle + description message
    print('You enter an empty dark room...')
    print(' ')
    print('There is something glowing in the corner')

    #space theme: asteroid, planet, star, moon, astronaut, sun
    options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']

    correct_password = random.choice(options)

    for word in options:
    if word == correct_password:
        print(word.capitalize())
    else:
        print(word)

    print('In front of you, you see a computer terminal asking you for a password. ') #custom message

    password_guess = input('Choose the password from the list. ')

    while password_guess != correct_password:
    print('Incorrect password. Try again. ')
    password_guess = input('Password: ')

    #custom space theme escape messages
    print('The computer begins to glow. ')
    print('The wall in front of you sinks into the ground, revealing a getaway space craft! ')
    print('You have escaped! ')

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

name = input('What is your name? ')
print('Welcome to the INTERGALACTIC Escape Room, ' + name + '!')

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
