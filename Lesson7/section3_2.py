room = [
    # 01234 col
    'xxxxx', # 0 row
    'x..ex', # 1
    'x...x', # 2
    'x...x', # 3
    'xxxxx', # 4
]

def move(old_row, old_col, direction):
    new_row = old_row
    new_col = old_col

    if direction == 'up':
        new_row = new_row - 1
    elif direction == 'down':
        new_row = new_row + 1
    elif direction == 'left':
        new_col = new_col - 1
    elif direction == 'right':
        new_col = new_col + 1

    return [new_row, new_col]
