def hide_unguessed_letters(target_word: str, guessed_letters: list[str]) -> None:
    '''
    Prints the word to the console containing "_" for any letter not guessed by
    the user. Takes in the correct word and the list of correct guesses as
    parameters.

    For example, given the word "red" and the guessed letters `['e','x']`, this
    function returns "_e_".
    '''
    result = ''

    for letter in target_word:
        if letter in guessed_letters:
            blank_or_letter = letter
        else:
            blank_or_letter = '_'

        result = result + blank_or_letter

    return result

print(hide_unguessed_letters('the', []))
print(hide_unguessed_letters('the', ['t']))
print(hide_unguessed_letters('the', ['h', 'e']))
print(hide_unguessed_letters('the', ['t', 'h', 'e']))
