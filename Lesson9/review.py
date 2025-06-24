# (1) What will the following code print? -------------------------------------
x = 12
if x < 0:
    print('negative')
elif x > 10:
    print('two digits')

if x > 0:                    # ⬅️ Pay special attention here.
    print('positive')

# (2) What will the following code print? -------------------------------------
x = 4
while x > 2:                # 2 > 2
    print(x)                #
    x = x - 1               #

# (3) What will the following code print? -------------------------------------
places = [
    ['Buffalo', 'New York City', 'Yonkers'],
    ['Austin',  'Dallas',        'Houston'],
    ]
print(places[0])        # ['Buffalo', 'New York City', 'Yonkers']
print(places[0][1])     # 'New York City'
print(places[0][1][2])  # 'w'
