#############
#Section 1 - Import Modules and Global Variables
#############


#############
#Section 2 - Functions Definition
#############

"""
To start, we are going to create the first 2 functions to handle the main menu of the program. The first one, display_menu() needs to display the main menu for the program. The second one, user_selection() needs to process user input selection.
Once you are done, uncomment the 2 function calls from the main function section
"""
#------------------display_menu() Function-----------
### Create main menu function
# 1- Define a function named 'display_menu()'
# 2- print a program name as the first message to the User
# 3- print all four user options numbered 1 to 4

def display_menu():
    print('\n **GenZ STORE INVENTORY SYSTEM')
    print('1. view store inventory')
    print('2. add new product')
    print('3. remove product')
    print('4. exit')

#------------------user_selection Function-----------
###Create user selection function
#1- define function: call it user_selection()
#2- prompt user to enter a number between 1 to 4
#3- create flow control (if-elif-else) to process user input
#4- add a print statement as a placeholder under each condition
#4a.Example of a placeholder [print(“show store inventory”) if user enter 1]
#5 - Uncomment the very last line of the program to test the function (user_selection())

def user_selection():
    choice = input('\nEnter a number between 1-4: ')

    if choice == '1':
        print('view store inventory')
    elif choice == '2':
        print('add new product')
    elif choice == '3':
        print('remove product')
    elif choice == '4':
        print('exit')
    else:
        print('invalid input: ' + choice)

#############
#Section 3 - Class Definition
#############
class Product:
    



#############
#Section 4 - Running Section
#############

####Do Not Change this code, only uncomment to test your code
display_menu()
user_selection()
