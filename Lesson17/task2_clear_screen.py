import os

def clear_screen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Mac OS, Linux
        os.system('clear')

if __name__ == '__main__':
    clear_screen()
