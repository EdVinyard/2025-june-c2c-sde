# (1) What will the following code print? -------------------------------------

places = [
  ['Bakersfield', 'San Francisco', 'Los Angeles', 'Redding'],
  ['Waco', 'Austin', 'Marfa', 'Dallas', 'Abilene'],
]
print(places[0])
print(places[0][1])
print(places[0][1][2])

# (2) What will the following code print? -------------------------------------

room = ['xxxxx',
        'x.p.x',
        'xd.ex',
        'xxxxx']
row = 2
col = 3

if room[row][col] == 'd':
    print('choose a door')
elif room[row][col] == 'p':
    print('guess the password')
elif room[row][col] == 'e':
    print('You escaped!')
