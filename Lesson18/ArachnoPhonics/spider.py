def spider_0():
    print('''
        %%%%%%%%%%%%%%%








        ''')

def spider_1():
    print('''
        %%%%%%%%%%%%%%%
               |
               |
               |





        ''')

def spider_2():
    print(r'''
        %%%%%%%%%%%%%%%
               |
               |
               |
              _|_
             /   \
             \___/
              ( )

        ''')

def spider_3():
    print(r'''
        %%%%%%%%%%%%%%%
               |
               |
               |
              _|_
             /   \
             \___/
             /( )\
             \   /
        ''')

def spider_4():
    print(r'''
        %%%%%%%%%%%%%%%
               |
               |
               |
              ___
             /   \
         \__ \___/ __/
             /( )\
             \   /
        ''')

def spider_5():
    print(r'''
        %%%%%%%%%%%%%%%
               |
               |
               |
              _|_
             /   \
         \__ \___/ __/
          _/ /( )\ \_
             \   /
        ''')

def spider_6():
    print(r'''
        %%%%%%%%%%%%%%%
               |
               |
               |
              _|_
          \_ /   \ _/
         \__ \___/ __/
          _/ /(0)\ \_
             \   /
        ''')

SPIDER_FUNCTIONS = [
    spider_0,
    spider_1,
    spider_2,
    spider_3,
    spider_4,
    spider_5,
    spider_6,
    ]

def print_spider(incorrect_guess_count):
    '''
    Prints spider from the spider drawing functions in the spiderDraw.py file.
    Takes the number of wrong guesses and the list of spider drawing functions
    as parameters.
    '''
    draw_function = SPIDER_FUNCTIONS[incorrect_guess_count]
    draw_function()

if __name__ == '__main__':
    while True:
        for i in range(len(SPIDER_FUNCTIONS)):
            print_spider(i)
            input('Press [Enter] to continue or Ctrl-C to quit.')
