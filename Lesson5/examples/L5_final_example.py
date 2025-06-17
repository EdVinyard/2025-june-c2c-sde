import random

name = input('What is your name? ')
print('Welcome to the INTERGALACTIC Escape Room, ' + name + '!')

# Choose a door
door = input('Choose a door. (1, 2, or 3) ')
correct_door = random.choice(['1', '2', '3'])

if door == correct_door:
    print('You escaped!')
else:
    print('You did not escape :(')

# password puzzle
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

if password_guess == correct_password:
    print('The computer begins to glow.')
    print('The wall in front of you sinks into the ground...')
    print('revealing a getaway space craft!')
    print('You have escaped!')
else:
    print('Incorrect password! Try again!')
