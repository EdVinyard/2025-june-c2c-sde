#############
# Section 1 - Import Modules and Global Variables
#############
import random  # used to generate random PID

inventory = [
    {'prod_Id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
    {'prod_Id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
    {'prod_Id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
    {'prod_Id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},
    {'prod_Id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
    {'prod_Id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10},
    {'prod_Id': 1664, 'type': 'Suits', 'price': 250.0, 'total': 5}
]

#############
# Section 2 - Functions Definition
#############

def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in inventory:
        print("~~~~~~~~~~~~")
        for key, value in product.items():
            print(f'{key}: {value}')

def display_menu():
    print("\n **GenZ STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")


def user_selection():
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:  # Go to Store Inventory.
        print('show inventory')
    elif user_choice == 2:  # Initiate New Product Process.
        print('add a new product')
    elif user_choice == 3:  # Initiate Removing a Product.
        print('remove a product')
    elif user_choice == 4:  # Exit the program
        print("program ends.")
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")


#############
# Section 3 - Class Definition
#############

# Creating a Product class
# 1- Define the classs with className: Product
# 2a- use __init__ () To instantiate the class
# 2b.- Class Attributes are: type,brand, price, size, color,style,total (keep the same order and names)
# 2c- Use the keyword self as many times as necessary
class Product:
    def __init__(self, type, price, total):
        self.id = random.randint(1000, 9999)
        self.type = type
        self.price = price
        self.total = total

    def features(self):
        # return something like
        # {'prod_Id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20}

#############
# Section 4 - Running Section
#############


# Do Not Change this code, only uncomment to test your code
display_inventory()
#display_menu()
#user_selection()
