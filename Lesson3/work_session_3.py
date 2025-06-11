cart_prices = [] # floating point prices

def add_to_cart(price):
    cart_prices.append(price)

def calculate_total():
    total_price = 0
    for price in cart_prices:
        total_price = total_price + price

    print('Total price: $' + str(total_price))

def remove_from_cart(price):
    cart_prices.remove(price)

add_to_cart(1.23)
add_to_cart(45.67)
add_to_cart(8.90)
calculate_total()

remove_from_cart(45.67) # too expensive
calculate_total()
