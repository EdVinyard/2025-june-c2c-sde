values = [0,1,2,3,4,5,6,7,8,9,10]

i = 11
while i > 0:
    print(values[:i])
    i = i - 1

for i in range(11, 0, -1):
    print(values[:i])
