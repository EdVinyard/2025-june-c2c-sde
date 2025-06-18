ROOM = [
    'xxxxx',
    'x..ex',
    'x...x',
    'x...x',
    'xxxxx',
    ]

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

row, col = 3, 1
print('position: ' + str(row) + ', ' + str(col))
announce_walls(row, col)

while ROOM[row][col] != 'e':
    direction = input(
        'Which direction will you move? (up, down, left, right) ')
    row, col = move(row, col, direction)
    print('position: ' + str(row) + ', ' + str(col))
    announce_walls(row, col)

print('You escaped!')
