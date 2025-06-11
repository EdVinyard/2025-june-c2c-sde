import random

# Player name
name = input('What is your name? ')
print(f'Welcome to our escape room, {name}.')

# Choose a door
door = input('Please choose a door (1, 2, or 3): ')
correct_door = random.choice(['1', '2', '3'])

if door == correct_door:
  print('You escaped!')
else:
  print('You did not escape :(')

# Guess the password
options = ['paper', 'pencil', 'computer', 'glasses', 'shirt', 'shoes']
correct_password = random.choice(options)

for word in options:
  if word == correct_password:
    print(word + ' 😉')
  else:
    print(word)
