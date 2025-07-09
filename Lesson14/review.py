#------------------------------------------------------------------------------
# (1) What will the following code print?
# indexes     0  1  2  3  4  5   6
fibbonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fibbonacci[4]) # prints "5"

#------------------------------------------------------------------------------
# (2) What will the following code print?

logo_colors = {
    'foreground': 'blue',
    'accent'    : 'orange',
    'background': 'grey',
    }
print(logo_colors['accent']) # prints "orange"

#------------------------------------------------------------------------------
# (3) What will the following code print?

grades = {
    #             0    1    2
    'Frank'   : [90,  95, 100],
    'June Bug': [91,  95,  99],
    'Bubbles' : [92,  95,  98],
    }
print(grades['Bubbles'][2])
