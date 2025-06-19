room = [
    'xxxxx',
    'x..ex',
    'x...x',
    'x...x',
    'xxxxx',
]


def move(old_row, old_col, direction):
    new_row = old_row
    new_col = old_col

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

    if room[new_row][new_col] == 'x':
        print('Ouch!  You bumped into a wall.')
        new_row = old_row
        new_col = old_col

    return new_row, new_col


row, col = 3, 1
print('position: ' + str(row) + ', ' + str(col))

while row != 1 or col != 3:
    direction = input(
        'Which direction will you move? (up, down, left, right) ')
    row, col = move(row, col, direction)
    print('position: ' + str(row) + ', ' + str(col))

print('You escaped!')
