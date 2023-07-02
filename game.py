import random

options = ('rock', 'paper', 'scissors')
run = True

while run:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ').lower()

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print('You Tie!')
    elif player == 'rock' and computer == 'paper':
        print('You Lose!')
    elif player == 'paper' and computer == 'scissors':
        print('You Lose!')
    elif player == 'scissors' and computer == 'rock':
        print('You Lose!')
    else:
        print('You Win!')

    if not input('Play again? (y/n): ').lower() == 'y':
        run = False

print('Thanks For Playing')
