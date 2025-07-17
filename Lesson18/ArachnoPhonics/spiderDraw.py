  #spider0
def spider_0():
  print(r"""
        %%%%%%%%%%%%%%%








        """)

#spider1
def spider_1():
  print(r"""
        %%%%%%%%%%%%%%%
               |
               |
               |





        """)

  #spider2
def spider_2():
  print(r"""
        %%%%%%%%%%%%%%%
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
  print(r"""
        %%%%%%%%%%%%%%%
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
  print(r"""
        %%%%%%%%%%%%%%%
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
  print(r"""
        %%%%%%%%%%%%%%%
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
  print(r"""
        %%%%%%%%%%%%%%%
               |
               |
               |
              ___
          \_ /   \ _/
         \__ \___/ __/
          _/ /(0)\ \_
             \   /
        """)

spiderList = [
    spider_0, spider_1, spider_2,
    spider_3, spider_4, spider_5,
    spider_6]

# Prints spider from the spider drawing functions in the
# spiderDraw.py file. Takes the number of wrong guesses
# and the list of spider drawing functions as parameters.
def print_spider(tries):
    spiderList[tries]()
