import random

class_roster = [
    'Alassan', 'Amauri', 'Andrew',   'Anerys', 'Dom',
    'Gracey',  'Jaydon', 'Jonathan', 'Juan',   'Melia',
    'Miguel',  'Seth',   'Vishal',
    ]

# Level 1 - Choose a random student from the class roster.
# Level 2 - Choose random students UNTIL the user decides to quit.

def input_yes_no(prompt):
    user_response = input(prompt + ' (Y/n) ')
    if user_response == '': # the user only pressed [Enter]
        return True

    user_response = user_response.lower() # ignore case
    if user_response == 'y':
        return True

    return False

choose_another = True
while choose_another:
    student = random.choice(class_roster)
    print(student)
    choose_another = input_yes_no('Choose another?')
