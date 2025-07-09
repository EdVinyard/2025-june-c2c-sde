show_menu = True
while show_menu:
    print("\n **GenZ STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")

    user_choice = input("Enter a number between 1-4: ")
    if user_choice == '1':
        print('view')
    elif user_choice == '2':
        print('add')
    elif user_choice == '3':
        print('remove')
    elif user_choice == '4':
        print('Bye!')
        show_menu = False                       # 🛑 CHANGE THE LOOP VARIABLE
    else:
        print("\nInvalid menu item: " + user_choice)
