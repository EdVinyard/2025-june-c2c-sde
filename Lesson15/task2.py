def find_max_min(numbers):
    try:
        min_num = numbers[0]
        max_num = numbers[0]
    except IndexError:
        return [None, None]

    for n in numbers:
        if n < min_num:
            min_num = n

        if n > max_num:
            max_num = n

    return [min_num, max_num]

if __name__ == '__main__':
    assert find_max_min([5]) == [5, 5],
    assert find_max_min([0,1,2,3,4,5,6,7,8,9,10]) == [0, 10]
    assert find_max_min([]) == [None, None]
