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

def add_new_product():
    print('\n **Adding A New Product To The Inventory**')
    print('------------------------------------')
    # 2. Ask the user for the product type, price, total.
    type = input('Enter a type: ')
    price = 10.00
    total = 25

    # 3.
    #     a. Call the Product initializer to create a Product.
    #     b. Call the .features() method on the Product object.
    #     c. Append product features to the store_inventory list.
    # 4. Print at least the new Product ID.

def remove_product():
    print('write this function')

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
