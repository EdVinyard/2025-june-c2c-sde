def count_vowels1(words: str) -> int:
    words = words.lower()
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

print(count_vowels1('Hello, World!'))
