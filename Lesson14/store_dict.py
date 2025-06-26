"""
This program is a simple version of a store inventory management.
It allows a user to:
1. View the store's inventory
2. Add new products to the inventory
3. remove products from the inventory
"""
# ---------------------------------------------------------------------
# Section 1 - Import Modules
# ---------------------------------------------------------------------
import random  # used to generate random product ID

# ---------------------------------------------------------------------
# Section 2 - Class Definition
# ---------------------------------------------------------------------
class Product:
    def __init__(self, type, price, total):
        self.id = random.randint(1000, 5000)
        self.type = type
        self.price = price
        self.total = total

    def display(self):
        print("----------------------------")
        print('product ID', self.id)
        print('type:', self.type)
        print('price:', self.price)
        print('total:', self.total)

# ---------------------------------------------------------------------
# Section 3 - Global Variables
# ---------------------------------------------------------------------
EXAMPLE_PRODUCTS = [
    Product('Shoes',   100.00, 20),
    Product('Tshirts',  43.50, 32),
    Product('Pants',    34.00, 19),
    Product('Jumper',  250.00,  5),
    Product('Blouse',   24.76,  3),
    Product('Dress',    50.00, 10),
    ]

store_inventory = {}
for product in EXAMPLE_PRODUCTS:
    store_inventory[product.id] = product

# ---------------------------------------------------------------------
# Section 4 - Functions Definition
# ---------------------------------------------------------------------
def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in store_inventory.values():
        product.display()
    print("___________________________")

def input_price():
    while True:
        try:
            price = float(input("Enter product price: "))

            if price > 0:
                return price
        except ValueError:
            pass

        print('Invalid price.')

def input_total_count():
    while True:
        try:
            total = int(input("Enter product total count: "))

            if total > 0:
                return total
        except ValueError:
            pass

        print('Invalid total count.')

def input_product_id():
    try:
        return int(input("Enter Product ID Number to Remove: "))
    except ValueError:
        print('Invalid Product ID.')

def add_new_product():
    print("\n **Adding A New Product To The Inventory**")
    print("------------------------------------")
    type = input("Enter product type (Shoes, Jacket,...): ").capitalize()
    price = input_price()
    total = input_total_count()
    new_product = Product(type, price, total)
    store_inventory.append(new_product)
    print('Added new product:')
    new_product.display()

def remove_product():
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")
    product_id = input_product_id()

    if product in store_inventory:
        store_inventory.remove(product)
        print("Product ID " + str(product_id) + " was removed.")
    else:
        print("Product ID " + str(product_id) + " NOT FOUND.")

def main_menu():
    print("\n **GenZ STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")

    user_choice = input("Enter a number between 1-4: ")
    if user_choice == '1':
        display_inventory()
    elif user_choice == '2':
        add_new_product()
    elif user_choice == '3':
        remove_product()
    elif user_choice == '4':
        return True
    else:
        print("\nInvalid menu item: " + user_choice)

    return False

# ---------------------------------------------------------------------
# Section 5 - Running Section
# ---------------------------------------------------------------------
