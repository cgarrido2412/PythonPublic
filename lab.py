import random
while True:
    print('Rock, Paper, Scissors!')
    print('Press ctrl+c to quit.')
    print('Are you playing alone? [y/n]')
    gameModeEntry = str(input())
    if gameModeEntry == 'y':
        print('Game Start!')
        print('Choose: Rock, Paper, or Scissors')
        gameChoices = {'rock':1, 'paper':2, 'scissors':3}
        player1choice = str(input('Player one chooses:'))
        player1choice = player1choice.lower()
        computerChoices = ['rock', 'paper', 'scissors']
        computerDecision = random.choice(computerChoices)
        print('Computer chooses:', computerDecision)
        player1compare = gameChoices.get(player1choice)
        computerCompare = gameChoices.get(computerDecision)
        result = player1compare - computerCompare
        if result == 0:
            print('The game is a draw!')
        elif result in [-2, 1]:
            print('Player 1 wins!')
        elif result in [-1, 2]:
            print('Computer wins!')
    elif gameModeEntry == 'n':
        print('Game Start!')
        print('Choose: Rock, Paper, or Scissors')
        gameChoices = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
        player1choice = str(input('Player one chooses:'))
        player1choice = player1choice.lower()
        player2choice = str(input('Player two chooses:'))
        player2choice = player2choice.lower()
        player1compare = gameChoices.get(player1choice)
        player2compare = gameChoices.get(player2choice)
        result = player1compare - player2compare
        if result == 0:
            print('The game is a draw!')
        elif result in [-2, 1]:
            print('Player one wins!')
        elif result in [-1, 2]:
            print('Player two wins!')
    else:
        print('Invalid choice! Please choose either "y" or "n"')
