ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

for suit in suits:
    for rank in ranks:
        print(rank + ' of ' + suit)
