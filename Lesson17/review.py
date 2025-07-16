#----------------------------------------------------------------
# (1) What will the following code print?

hearts = {'red'  : '❤️',
          'green': '💚',
          'blue' : '💙'}
print(hearts['green'] * 10)

#----------------------------------------------------------------
# (2) What will the following code print?

def widget():
    print('widget')

def doodad():
    print('doodad')

def whatzit():
    print('whatzit')

gadgets = [widget, doodad, whatzit]
gadgets[2]()
