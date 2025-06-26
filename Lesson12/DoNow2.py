"""
This program is a simple version of a store inventory management.
It allows a user to:
1. View the store's inventory
2. Add new products to the inventory
3. remove products from the inventory
"""
############################################################################
# Section 1 - Import Modules
###########################################################################
import random  # used to generate random product ID

#####################################################################################
# Section 2 - Class Definition
######################################################################################
class Product:
    # constructor method used to instantiate any new class
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

##############################################################################
# Section 3 - Global Variables
#############################################################################
store_inventory = [  # sample store inventory
    Product('Shoes', 100.0, 20),
    Product('Tshirts', 43.5, 32),
    Product('Pants', 34.0, 19),
    Product('Jumper', 250.0, 5),
    Product('Blouse', 24.76, 3),
    Product('Dress', 50.0, 10),
    ]

##############################################################################
# Section 4 - Functions Definition
#############################################################################

# Displays the main menu
def display_menu():
    print("\n **GenZ STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")

    # used to capture and process user selections

def user_selection():
    in_use = True
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:  # Go to Store Inventory.
        display_inventory()  # print('show inventory')
    elif user_choice == 2:  # Initiate New Product Process.
        add_new_product()  # print('add a new product')
    elif user_choice == 3:  # Initiate Removing a Product.
        remove_product()  # print('remove a product')
    elif user_choice == 4:  # Exit the program
        print("Thank you for using the program!"
              )  # adds thank you message before exiting the program
        # print("program ends.")  # changes the value of isUsed to False
        in_use = False
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")
    return in_use

# this function displays story inventory
def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in store_inventory:
        product.display()
    print("___________________________")

# add a new product function
def add_new_product():
    print("\n **Adding A New Product To The Inventory**")
    print("------------------------------------")
    type = input("Enter a type(Shoes, Jacket,...): ").capitalize()
    # simple validation technique
    try:
        price = float(input("Enter a price: "))
    except ValueError:
        price = 0.0  # assigned a default number
    try:
        total = int(input("Enter a total: "))  # needs validation
    except ValueError:
        total = 0  # assigned a default number

    # only add a product to the inventory if price and total greater than zero
    if price > 0 and total > 0:
        # create a new product instance based on the attributes provided
        new_product = Product(type, price, total)
        # added product to inventory
        store_inventory.append(new_product)
        display_inventory()  # used for testing

    else:
        print(
            "Invalid Price or/and Total. Product not Added to the Inventory ")

# Remove a product
def remove_product():
    to_delete_index = -1
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")

    try:
        PID = int(input("Enter Product ID Number to Remove: "))
    except ValueError:
        PID = 0

    found = False
    for product in store_inventory:
        if product.id == PID:
            found = True
            store_inventory.remove(product)
            print("Product was successfully removed from the store inventory.")
            break  # ends the search and loop

    if not found:
        print("This is not in the inventory. Try again.")

##################################################################################
# Section 5 - Running Section
##################################################################################
program_loop = True
while program_loop:
    display_menu()
    program_loop = user_selection()
