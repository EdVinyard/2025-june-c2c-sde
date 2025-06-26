# ------------------------------------------------------------------------
# (1) How can we include an apostrophe in a string literal?

# See Python Documentation on String Literals
# https://docs.python.org/3/tutorial/introduction.html#text

s = 'can't'
s = "can't"

# -----------------------------------------------------------------------
# (2) What will the following code print?
import random

def coin_toss():
    possible_outcomes = ['heads', 'tails']
    outcome = random.choice(possible_outcomes)
    print(outcome)

# flip a coin twice
coin_toss()
coin_toss()
