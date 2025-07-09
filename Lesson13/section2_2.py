inventory = [
    { 'prod_Id': 4327,  'type': 'Shoes',   'price': 100.00, 'total': 20 },
    { 'prod_Id': 3915,  'type': 'Tshirts', 'price':  43.50, 'total': 32 },
    { 'prod_Id': 2119,  'type': 'Pants',   'price':  34.00, 'total': 19 },
    { 'prod_Id': 1194,  'type': 'Jumpers', 'price': 250.00, 'total':  5 },
    { 'prod_Id': 1300,  'type': 'Blouse',  'price':  24.76, 'total':  3 },
    { 'prod_Id': 1118,  'type': 'Dress',   'price':  50.00, 'total': 10 },
    { 'prod_Id': 1664,  'type': 'Suits',   'price': 250.00, 'total':  5 }
]

def print_inventory():
    print(' ** GEN-Z STORE INVENTORY ** ')
    for product in inventory:
        print('-----------------------------')
        for key, value in product.items():
            print(key + ': ' + str(value))

print_inventory()
