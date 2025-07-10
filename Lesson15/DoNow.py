def count_vowels(words: str) -> int:
    try:
        words = words.lower()
    except AttributeError:
        return 0

    count = 0

    for letter in words:
        is_vowel = False

        if letter == 'a':
            is_vowel = True
        elif letter == 'e':
            is_vowel = True
        elif letter == 'i':
            is_vowel = True
        elif letter == 'o':
            is_vowel = True
        elif letter == 'u':
            is_vowel = True

        if is_vowel:
            count = count + 1

    return count

# no vowels
print('expect 0, counted', count_vowels(''))
print('expect 0, counted', count_vowels('!'))
print('expect 0, counted', count_vowels('x'))
print('expect 0, counted', count_vowels('fly'))

# some vowels
print('expect 1, counted', count_vowels('a'))
print('expect 3, counted', count_vowels('Hello, World!'))

# errors
print('expect 0, counted', count_vowels(None))
