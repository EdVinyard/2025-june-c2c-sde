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
        self.id = random.randint(1000, 5000)  # new attribute added
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
store_inventory = [  # sample store inventory
    Product('Shoes',   100.00, 20),
    Product('Tshirts',  43.50, 32),
    Product('Pants',    34.00, 19),
    Product('Jumper',  250.00,  5),
    Product('Blouse',   24.76,  3),
    Product('Dress',    50.00, 10),
    ]

# ---------------------------------------------------------------------
# Section 4 - Functions Definition
# ---------------------------------------------------------------------
def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in store_inventory:
        product.display()
    print("___________________________")

def add_new_product():
    print("\n **Adding A New Product To The Inventory**")
    print("------------------------------------")
    type = input("Enter product type (Shoes, Jacket,...): ").capitalize()

    try:
        price = float(input("Enter product price: "))
    except ValueError:
        print('Invalid price.')
        return

    if price <= 0:
        print('Invalid price.')
        return

    try:
        total = int(input("Enter product total count: "))
    except ValueError:
        print('Invalid total.')
        return

    if total <= 0:
        print('Invalid total.')
        return

    new_product = Product(type, price, total)
    store_inventory.append(new_product)

def remove_product():
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")

    try:
        product_id = int(input("Enter Product ID Number to Remove: "))
    except ValueError:
        print('Invalid Product ID.  No Product removed.')
        return

    found = False
    for product in store_inventory:
        if product.id == product_id:
            found = True
            store_inventory.remove(product)
            print("Product ID " + str(product_id) + " was removed.")

    if not found:
        print("Product ID " + str(product_id) + " not found. Try again.")

def main_menu():
    print("\n **GenZ STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")

    exit_now = False
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:
        display_inventory()
    elif user_choice == 2:
        add_new_product()
    elif user_choice == 3:
        remove_product()
    elif user_choice == 4:
        print("Goodbye!")
        exit_now = True
    else:
        print("\nInvalid choice.  Try again!")

    return exit_now

# ---------------------------------------------------------------------
# Section 5 - Running Section
# ---------------------------------------------------------------------
exit_now = False
while not exit_now:
    exit_now = main_menu()
