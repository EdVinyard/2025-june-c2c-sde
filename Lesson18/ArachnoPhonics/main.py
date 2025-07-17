import spiderDraw as sd
import functions as md
import time


def play_arachnophonics():
    correct = []                # list of correct letters guessed
    incorrect = []              # list of WRONG letters guessed
    wrong_count = 0             # number of incorrect guesses
    game_in_progress = True     # game is over when this is False
    word = 'frank'              # for testing
    #word = md.generate_word()   # word the user is trying to guess

    md.introduction()

    while game_in_progress:
        sd.print_spider(wrong_count)
        print(f'{wrong_count} incorrect guesses {incorrect}')
        word_with_blanks = md.hide_unguessed_letters(word, correct)
        print('Word: ', word_with_blanks)
        wrong_count = md.check_word(correct, incorrect, word, wrong_count)
        time.sleep(1)
        md.clear_screen()

        # End the game if the player made too many incorrect guesses.

        # End the game if the player guessed all the letters of the word.


if __name__ == '__main__':
    play_arachnophonics()
