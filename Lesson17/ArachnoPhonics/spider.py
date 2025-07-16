#spider0
def spider_0():
  print(f"""
        - - - - - - - -








        """)

#spider1
def spider_1():
  print(f"""
        - - - - - - - -
               |
               |
               |





        """)

  #spider2
def spider_2():
  print(f"""
        - - - - - - - -
               |
               |
               |
              ___
             /   \
             \___/
              ( )

        """)


  #spider3
def spider_3():
  print(f"""
        - - - - - - - -
               |
               |
               |
              ___
             /   \
             \___/
             /( )\
             \   /
        """)

  #spider4
def spider_4():
  print(f"""
        - - - - - - - -
               |
               |
               |
              ___
             /   \
         \__ \___/ __/
             /( )\
             \   /
        """)


  #spider5
def spider_5():
  print(f"""
        - - - - - - - -
               |
               |
               |
              ___
             /   \
         \__ \___/ __/
          _/ /( )\ \_
             \   /
        """)


  #spider6
def spider_6():
  print(f"""
        - - - - - - - -
               |
               |
               |
              ___
          \_ /   \ _/
         \__ \___/ __/
          _/ /(0)\ \_
             \   /
        """)

ALL_SPIDERS = [spider_0, spider_1, spider_2,
              spider_3, spider_4, spider_5,
              spider_6]

# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries):
    ALL_SPIDERS[tries]()
