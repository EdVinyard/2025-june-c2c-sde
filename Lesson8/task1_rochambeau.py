import random


def winner_vs(move):
    if move == 'rock':
        winner = 'paper'
    elif move == 'paper':
        winner = 'scissors'
    elif move == 'scissors':
        winner = 'rock'
    else:
        print('invalid move: ' + move)
        winner = None

    return winner

play_again = 'y'
while play_again == 'y':
    player_move = input('Move? (rock, paper, scissors) ')
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    print('The computer chose ' + computer_move + '.')
    if player_move == computer_move:
        print('Tie.')
    elif player_move == winner_vs(computer_move):
        print('You win!')
    elif computer_move == winner_vs(player_move):
        print('The computer wins.')
    else:
        print('ERROR: ' + player_move + ' vs ' + computer_move)

    play_again = input('Play again? (y/n)').lower()
