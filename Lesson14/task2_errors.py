class ShoppingCart:
    def __init__(self):
        self.products = {} # maps name to price

    def add(self, name, price):
        self.products[name] = price

    def remove(self, name):
        try:
            del self.products[name]
        except KeyError:
            print('no such item in cart: ' + name)

    def __str__(self):
        s = ''
        for name, price in self.products.items():
            s += name + ' $' + str(price) + '\n'
        return s

def input_product_name(prompt):
    name = ''
    while len(name.strip()) == 0:
        name = input(prompt)

        if len(name.strip()) == 0:
            print('product name must include non-whitespace characters')

    return name

def input_price(prompt):
    price = -1
    while price <= 0.0:
        price_str = input(prompt)
        try:
            price = float(price_str)
        except ValueError:
            pass

        if price <= 0.0:
            print('invalid price: ' + price_str)

    return price

def main():
    shopping_cart = ShoppingCart()
    choice = -1
    while choice != '3':
        print('=== Shopping Cart contents ===')
        print(shopping_cart)
        print('==============================')
        print('1. add to cart')
        print('2. remove from cart')
        print('3. exit')

        choice = input('? ')

        if choice == '1':
            name = input_product_name('product name? ')
            price = input_price('product price? ')
            shopping_cart.add(name, price)
        elif choice == '2':
            name = input_product_name('product name? ')
            shopping_cart.remove(name)

if __name__ == '__main__':
    main()
