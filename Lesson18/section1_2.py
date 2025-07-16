player_name = input('What is your name? ')

intro_message = f'''

     ▗▄▄ ▄▄▄ ▗▞▀▜▌▗▞▀▘▐▌   ▄▄▄▄   ▄▄▄  ▗▄▄▖ ▐▌    ▄▄▄  ▄▄▄▄  ▄ ▗▞▀▘ ▄▄▄
    ▐▌ ▐▌█   ▝▚▄▟▌▝▚▄▖▐▌   █   █ █   █ ▐▌ ▐▌▐▌   █   █ █   █ ▄ ▝▚▄▖▀▄▄
    ▐▛▀▜▌█            ▐▛▀▚▖█   █ ▀▄▄▄▀ ▐▛▀▘ ▐▛▀▚▖▀▄▄▄▀ █   █ █     ▄▄▄▀
    ▐▌ ▐▌             ▐▌ ▐▌            ▐▌   ▐▌ ▐▌            |
                                                            🕷️
Welcome, {player_name}!

ArachnoPhonics is a guess-the-word game where the user guesses one letter at a
time.

After each turn, you'll see a picture of a spider forming.  Every time you
guess a letter that is NOT in the word, more of the spider will be visible.
If you run out of guesses, the spider will get you!

Press [Enter] to start.
'''

input(intro_message) # wait for [Enter], then discard what the user types
