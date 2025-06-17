room: list[str] = [
  'xxx',
  'x.x',
  'xxx',
]

def is_walking_path(row, column):
    return room[row][column] == '.'

print('expect False: ' + str(is_walking_path(0, 0)))
print('expect True : ' + str(is_walking_path(1, 1)))
