name = input('What is your name? ')
print(f'Welcome to our escape room, {name}! ')

door_choice = input('Which door will you open? (1, 2, or 3) ')

if door_choice == '1':              # input() returns a string, not an integer
    print('You escaped!')
else:
    print("It's just an empty closet.")
