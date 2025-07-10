# access libraries and py files
import spiderDraw as sd
import functions as md

# Initialize variables and setup
# Need to keep track of correct letters, incorrect letters and tries

correct = []  # List of correct letters guessed
incorrect = []  # List of incorrect letters guessed
tries = 0  # Number of incorrect guesses
game = True

# Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2,
              sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]


# Print intro statements (welcome to game, etc)


# generate a random word from word list
word = md.generate_word()
print(word)


# Game Loop
while game:
    md.print_spider(tries, spiderList)

    # This is where you'll call all of your functions. Just need to decide the proper order.

    # You will also need to specify your win and lose conditions in here
    # game
