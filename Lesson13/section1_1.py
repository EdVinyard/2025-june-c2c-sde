import random

class Product:
    def __init__(self, type, price, total):
        self.id = random.randint(1000, 5000)
        self.type = type
        self.price = price
        self.total = total

def birthday_problem():
    '''see https://en.wikipedia.org/wiki/Birthday_problem'''
    chosen_ids = set()
    while True:
        product = Product('widget', 1.23, 45)

        if product.id in chosen_ids:
            break

        chosen_ids.add(product.id)

    print('first duplicate ID chosen after iteration ' + str(len(chosen_ids)))

birthday_problem()
