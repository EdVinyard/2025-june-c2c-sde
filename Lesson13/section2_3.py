import random

inventory = [
    { 'prod_Id': 4327,  'type': 'Shoes',   'price': 100.00, 'total': 20 },
    # ...
]

class Product:
    def __init__(self, type, price, total):
        self.id = random.randint(1000, 5000)
        self.type = type
        self.price = price
        self.total = total

    def features(self):
        return {
            'prod_id': self.id,
            'type'   : self.type,
            'price'  : self.price,
            'total'  : self.total,
            }
