import random


def quiz_question(left, right):
    product = left * right      # integer
    user_answer = 'placeholder' # string
    while user_answer != product:
        user_answer = input(str(left) + ' * ' + str(right) + ' = ')
        if user_answer != str(product):
            print('Incorrect.  Try again.')
    print('Correct!')

name = input('What is your name? ')

print('This is a multiplication quiz, ' + name + '.')

i = 0
while i < 5:
    quiz_question(random.randint(1, 10), random.randint(1, 12))
    i = i + 1
