# Prints the word to the console containing "_" for any letter not guessed by
# the user. Takes in the correct word and the list of correct guesses as
# parameters.
#
# For example, given the word "red" and the guessed letters `['e','x']`, this
# function returns "_e_".
def hide_unguessed_letters(target_word: str, guessed_letters: list[str]) -> None:
    result = ''

    # for each letter in the target_word
        # Add the letter to the result string if it is in target_word.
        # Add a "_" to the result string if the letter is NOT in target_word.

    return result

print('expecting "___"; ', hide_unguessed_letters('the', []))
print('expecting "t__"; ', hide_unguessed_letters('the', ['t']))
print('expecting "_he"; ', hide_unguessed_letters('the', ['h', 'e']))
print('expecting "the"; ', hide_unguessed_letters('the', ['t', 'h', 'e']))
