import random

numbers = [0,1,2,3,4,5,6,7,8,9]

def pick_random_number(options):
    selected = random.choice(options)
    print(selected)

pick_random_number(numbers)
