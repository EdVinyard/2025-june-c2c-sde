store_inventory = ['milk', 'eggs', 'bread']
shopping_list = ['eggs', 'bacon']

for list_item in shopping_list:
    store_has_item = False
    for store_item in store_inventory:
        if store_item == list_item:
            store_has_item = True
            
    if store_has_item:
        print(list_item + ' is/are available in the store.')
    else:
        print(list_item + ' is/are NOT available in the store.')
