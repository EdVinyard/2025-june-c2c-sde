def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[1]

    for n in numbers:
        if n < min_num:
            min_num = n

        if n > max_num:
            max_num = n

    return min_num, max_num

print(find_max_min([0,1,2,3,4,5,6,7,8,9,10]))
