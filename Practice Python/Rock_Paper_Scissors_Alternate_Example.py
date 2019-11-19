#A rock paper scissors game that can be played alone against a random choice computer or "with" another person
import random
import time
while True:
    time.sleep(1)
    print('Rock, Paper, Scissors!')
    time.sleep(1)
    print('Press ctrl+c to quit.')
    time.sleep(1)
    print('Are you playing alone? [y/n]')
    gameModeEntry = str(input())
    if gameModeEntry == 'y':
        time.sleep(1)
        print('Game Start!')
        time.sleep(1)
        print('Choose: Rock, Paper, or Scissors')
        time.sleep(1)
        gameChoices = {'rock':1, 'paper':2, 'scissors':3}
        player1choice = str(input('Player one chooses:'))
        player1choice = player1choice.lower()
        computerChoices = ['rock', 'paper', 'scissors']
        computerDecision = random.choice(computerChoices)
        time.sleep(1)
        print('Computer chooses:', computerDecision)
        player1compare = gameChoices.get(player1choice)
        computerCompare = gameChoices.get(computerDecision)
        result = player1compare - computerCompare
        if result == 0:
            time.sleep(1)
            print('The game is a draw!')
            time.sleep(1)
            print('Game restarting...')
        elif result in [-2, 1]:
            time.sleep(1)
            print('Player 1 wins!')
            time.sleep(1)
            print('Game restarting...')
        elif result in [-1, 2]:
            time.sleep(1)
            print('Computer wins!')
            time.sleep(1)
            print('Game restarting...')
    elif gameModeEntry == 'n':
        time.sleep(1)
        print('Game Start!')
        time.sleep(1)
        print('Choose: Rock, Paper, or Scissors')
        time.sleep(1)
        gameChoices = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
        player1choice = str(input('Player one chooses:'))
        time.sleep(1)
        player1choice = player1choice.lower()
        player2choice = str(input('Player two chooses:'))
        time.sleep(1)
        player2choice = player2choice.lower()
        player1compare = gameChoices.get(player1choice)
        player2compare = gameChoices.get(player2choice)
        result = player1compare - player2compare
        if result == 0:
            print('The game is a draw!')
            time.sleep(1)
            print('Game resetting...')
        elif result in [-2, 1]:
            print('Player one wins!')
            time.sleep(1)
            print('Game resetting...')
        elif result in [-1, 2]:
            print('Player two wins!')
            time.sleep(1)
            print('Game resetting...')
    else:
        print('Invalid choice! Please choose either "y" or "n"')
        time.sleep(1)
        print('Game resetting...')
