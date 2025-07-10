import random

words = ['red', 'green', 'blue']

def generate_random_word(all_words):
    return random.choice(all_words)

print(generate_random_word(words))
