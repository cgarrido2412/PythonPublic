#Make a one-player Rock-Paper-Scissors game
import random
def game():
    print('Rock, paper, scissors!')
    player1score = 0
    computerScore = 0
    while True:
        gameDictionary = { 'rock': 1, 'paper': 2, 'scissors': 3 }
        player1 = (str(input('Player one please enter a choice \n')))
        player1 = player1.strip()
        player1 = player1.lower()
        if player1 not in gameDictionary:
            print('Invalid input!')
            break
        computerChoiceList = ['rock', 'paper', 'scissors']
        computerChoice = random.choice(computerChoiceList)
        print('Computer chooses:', computerChoice)
        one = gameDictionary.get(player1)
        two = gameDictionary.get(computerChoice)
        result = one - two
        if result in [0]:
            print('The game is a draw')
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore)
        elif result in [-2, 1]:
            print('Player one wins!')
            player1score = int(player1score) + 1
            if player1score == 3:
                print('Player 1 has won three games out of five!')
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore) 
                break
            else:
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
        elif result in [-1, 2]:
            print('Computer wins!')
            computerScore = int(computerScore) + 1
            if computerScore == 3:
                print('Computer has won three games out of five!')
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
                break
            else:
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
    print('Game over, thanks for playing!') 
