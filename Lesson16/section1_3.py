import time as tm       # aliased import

i = 0
while True:
    web = '┉' * i       # duplicate a string with operator *
    print(web + '🕷️')
    tm.sleep(1)         # pause program for N seconds
    i = i + 1

    if i > 10:
        break           # "break out" of the loop

print('done')
