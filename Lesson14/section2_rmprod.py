'''
a simple store inventory management system that allows the user to:
    1. View the store's inventory
    2. Add new products to the inventory
    3. remove products from the inventory
'''
############################################################################
# Section 1 - Import Modules and Global Variables
###########################################################################
import random  # used to generate random PID

store_inventory = [  # sample store inventory
    {'product_id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
    {'product_id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
    {'product_id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
    {'product_id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},
    {'product_id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
    {'product_id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10},
    {'product_id': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
    ]

##############################################################################
# Section 2 - Functions Definition
#############################################################################
def display_menu():
    print('\n **GenZ STORE INVENTORY SYSTEM**')
    print('  1. View Store Inventory ')
    print('  2. Add A New Product')
    print('  3. Remove Products')
    print('  4. Exit\n')

def user_selection():
    exit_now = False
    user_choice = int(input('Enter a number between 1-4: '))

    if user_choice == 1:  # Go to Store Inventory.
        display_inventory()  # print('show inventory')
    elif user_choice == 2:  # Initiate New Product Process.
        add_new_product()  # print('add a new product')
    elif user_choice == 3:  # Initiate Removing a Product.
        remove_product()  # print('remove a product')
    elif user_choice == 4:  # Exit the program
        exit_now = True
    else:
        print('Invalid choice.')

    return exit_now

def display_inventory():
    print('\n **GEN-Z STORE INVENTORY**')
    for product in store_inventory:
        print('----------------------------')
        for key, value in product.items():
            print(f'{key}: {value}')
    print('___________________________')

def input_price(prompt):
    while True:
        price_string = input(prompt)
        try:
            price_float = float(price_string)

            if price_float > 0.0:
                return price_float
        except ValueError:
            pass

        print('Invalid price: ' + price_string)

def input_total(prompt):
    while True:
        total_str = input(prompt)
        try:
            total_int = int(total_str)

            if total_int > 0.0:
                return total_int
        except ValueError:
            pass

        print('Invalid total count: ' + total_str)

def add_new_product():
    print('\n **Adding A New Product To The Inventory**')
    print('------------------------------------')
    type = input('Enter a type: ')
    price = input_price('Enter the item price: ')
    total = input_total('Enter the total count: ')
    product = Product(type, price, total)
    features = product.features()
    store_inventory.append(features)

def remove_product():
    to_delete_index = -1
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")
    # User inputs Product ID.  Use int() to convert from string to integer.
    # Find the product features dictionary in the store_inventory list.
    # Delete the product features dictionary from the store_inventory list.
    # Warn the user if they entered a Product ID that isn't in inventory.

def main_loop():
    exit_now = False

    while not exit_now:
        display_menu()
        exit_now = user_selection()

    print('Goodbye.')

#####################################################################################
# Section 3 - Class Definition
######################################################################################
class Product:
    def __init__(self, type, price, total):
        self.product_id = random.randint(1000, 5000)  # new attribute added
        self.type = type
        self.price = price
        self.total = total

    def features(self):
        return {
            'product_id': self.product_id,
            'type': self.type,
            'price': self.price,
            'total': self.total
            }

##################################################################################
# Section 4 - Running Section
##################################################################################
main_loop()
