import os
import time

def clear_screen():
    if os.name == 'nt':
        # Windows; see
        # https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cls
        os.system('cls')
    else:
        # Mac OS, Linux; see
        # https://manpages.debian.org/bookworm/ncurses-bin/clear.1.en.html
        os.system('clear')

if __name__ == '__main__':
    print('Clear screen in... ')

    i = 3
    while i > 0:
        print(i)
        time.sleep(1)
        i = i - 1

    clear_screen()
