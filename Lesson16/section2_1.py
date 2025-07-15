import time as tm                           # aliased import

def spider1():
    print('┈┈🕷️')

def spider2():
    print('┈┈┈┈┈┈🕷️')

def spider3():
    print('┈┈┈┈┈┈┈┈┈┈┈┈🕷️')

ALL_SPIDERS = [spider1, spider2, spider3]   # functions in a list

def print_spider(index):
    print_function = ALL_SPIDERS[index]     # function as a variable value
    print_function()

i = 0
while True:
    tm.sleep(1)                             # pause for N seconds
    print_spider(i)
    i = i + 1

    if i > 2:
        i = 0
