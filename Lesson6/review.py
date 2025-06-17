# Read the following code.  Be ready to answer the 3 questions on the right.

import random                           # (1) WHAT DOES THIS LINE DO?

all_colors = ['red', 'green', 'blue']
random_color = random.choice(all_colors)

#color = 'orange'                        # (2) IS THIS LINE NECESSARY?
for color in all_colors:
    print(color)

x = random.random()                     # (3) WHAT DOES THIS LINE DO?
print(x)
