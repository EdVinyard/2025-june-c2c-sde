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

def is_vowel(c: str) -> bool:
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def count_vowels2(words: str) -> int:
    count = 0
    for letter in words.lower():
        if is_vowel(letter):
            count += 1

    return count

def count_vowels3(words: str) -> int:
    return sum( 1 for c in words.lower() if c in 'aeiou' )

print(count_vowels1('Hello, World!'))
print(count_vowels2('Hello, World!'))
print(count_vowels3('Hello, World!'))
