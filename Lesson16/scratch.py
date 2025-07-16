def spider0():
    print('┈┈🕷️')

def spider1():
    print('┈┈┈┈┈┈🕷️')

def spider2():
    print('┈┈┈┈┈┈┈┈┈┈┈┈🕷️')

ALL_SPIDERS = [spider0, spider1, spider2]
incorrect_guess_count = 2
draw_spider = ALL_SPIDERS[incorrect_guess_count]
draw_spider()
