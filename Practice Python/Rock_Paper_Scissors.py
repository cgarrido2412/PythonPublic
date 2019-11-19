#module imports 
import random

#Always starts with setting the game score to zero
print('Rock, paper, scissors!')
player1score = 0
computerScore = 0

#Defines the game loop and game dictonary of choices with respective values
while True:
    gameDictionary = { 'rock': 1, 'paper': 2, 'scissors': 3 }
    player1 = (str(input('Player one please enter a choice \n')))
    player1 = player1.strip()
    player1 = player1.lower()

    #The game will only accept proper input / choices
    if player1 not in gameDictionary:
        print('Invalid input!')
        break

    #Defines choice list for "computer" and compares player choice to computer choice
    computerChoiceList = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(computerChoiceList)
    print('Computer chooses:', computerChoice)
    one = gameDictionary.get(player1)
    two = gameDictionary.get(computerChoice)
    result = one - two

    #This part of the math matrix is to address whenever there is a draw
    if result in [0]:
        print('The game is a draw')
        print('Player 1 score: ', player1score)
        print('Computer score: ', computerScore)

    #This part of the math matrix defines the win conditions for the player
    elif result in [-2, 1]:
        print('Player one wins!')
        player1score = int(player1score) + 1

	#If the player wins the game, will let the player know and print the final score
        if player1score == 3:
            print('Player 1 has won three games out of five!')
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore) 
            break

	#Will print the score if the game isn't over
        else:
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore)

    #This part of the math matrix defines the win conditions for the "computer" player
    elif result in [-1, 2]:
        print('Computer wins!')
        computerScore = int(computerScore) + 1

	#If the computer wins the game, will let the player know and print the final score
        if computerScore == 3:
            print('Computer has won three games out of five!')
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore)
            break
        
	#Will print the score if the game isn't over
        else:
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore)

#When the game loop breaks, message prints that the game is over. 
print('Game over, thanks for playing!') 
