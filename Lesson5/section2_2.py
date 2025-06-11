import random

options = ['paper', 'pencil', 'computer', 'glasses', 'shirt', 'shoes']
correct_password = random.choice(options)

for word in options:
  if word == correct_password:
    print(word + ' 😉')
  else:
    print(word)
