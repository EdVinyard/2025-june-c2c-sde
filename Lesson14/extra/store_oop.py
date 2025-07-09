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
    def __init__(self, type: str, price: float, total: int):
        self.id = random.randint(1000, 5000)
        self.type = type
        self.price = price
        self.total = total

    def display(self) -> None:
        print("----------------------------")
        print('ID         :', self.id)
        print('type       :', self.type)
        print('price (USD):', self.price)
        print('total      :', self.total)

class Inventory:
    def __init__(self, starting_products):
        self._products = {} # maps int Product ID ==> Product instance
        for product in starting_products:
            self.add(product)

    def add(self, product) -> Product:
        '''overwrites `product_id` in this inventory'''
        self._products[product.id] = product
        return product

    def has(self, product_id) -> bool:
        '''returns `True` iff `product_id` is in this inventory'''
        return product_id in self._products

    def remove(self, product_id) -> Product:
        '''raises ValueError if `product_id` does not exist'''
        product = self._products[product_id]
        del self._products[product_id]
        return product

    def products(self) -> list[Product]:
        return self._products.values()

    def display(self):
        print('   ID            Type    Price   Total')
        print('---------------------------------------')
        for p in self.products():
            id = str(p.id).rjust(5)
            type = p.type.rjust(15)
            price = ('$' + str(p.price)).rjust(8)
            total = str(p.total).rjust(7)
            print(id, type, price, total)

class TextUserInterface:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def run(self):
        exit_now = False
        while not exit_now:
            exit_now = self.main_menu()

        print("Goodbye!")

    def input_price(self):
        while True:
            try:
                price = float(input("Enter product price: "))

                if price > 0:
                    return price
            except ValueError:
                pass

            print('Invalid price.')

    def input_total_count(self):
        while True:
            try:
                total = int(input("Enter product total count: "))

                if total > 0:
                    return total
            except ValueError:
                pass

            print('Invalid total count.')

    def input_product_id(self):
        try:
            return int(input("Enter Product ID Number to Remove: "))
        except ValueError:
            print('Invalid Product ID.')

    def add_new_product(self):
        print("\n **Adding A New Product To The Inventory**")
        print("------------------------------------")
        type = input("Enter product type (Shoes, Jacket,...): ").capitalize()
        price = self.input_price()
        total = self.input_total_count()
        new_product = Product(type, price, total)
        self.inventory.add(new_product)
        print('Added new product:')
        new_product.display()

    def remove_product(self):
        self.inventory.display()
        print("\n **Removing A Product From The Inventory**")
        print("------------------------------------")
        product_id = self.input_product_id()

        if self.inventory.has(product_id):
            product = self.inventory.remove(product_id)
            print('Removed product:')
            product.display()
        else:
            print("Product ID " + str(product_id) + " NOT FOUND.")

    def main_menu(self) -> bool:
        '''returns `True` iff the user wants to exit the program now'''
        print("\n **GenZ STORE INVENTORY SYSTEM**")
        print("1. View Store Inventory ")
        print("2. Add A New Product")
        print("3. Remove Products")
        print("4. Exit\n")

        user_choice = input("Enter a number between 1-4: ")
        if user_choice == '1':
            self.inventory.display()
        elif user_choice == '2':
            self.add_new_product()
        elif user_choice == '3':
            self.remove_product()
        elif user_choice == '4':
            return True
        else:
            print("\nInvalid menu item: " + user_choice)

# ---------------------------------------------------------------------
# Section 5 - Running Section
# ---------------------------------------------------------------------
if __name__ == '__main__':
    inventory = Inventory([
        Product('Shoes',   100.00, 20),
        Product('Tshirts',  43.50, 32),
        Product('Pants',    34.00, 19),
        Product('Jumper',  250.00,  5),
        Product('Blouse',   24.76,  3),
        Product('Dress',    50.00, 10),
        ])
    ui = TextUserInterface(inventory)
    ui.run()
