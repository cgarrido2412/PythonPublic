#Make a one-player Rock-Paper-Scissors game
#import modules
import random

#the function that defines the game 
def game():
    print('Rock, paper, scissors!')
    player1score = 0
    computerScore = 0
    
	#The game repeats and assumes true, once the game is played to best 3 out of 5 this loop breaks
	while True:
        gameDictionary = { 'rock': 1, 'paper': 2, 'scissors': 3 }
        player1 = (str(input('Player one please enter a choice \n')))
        player1 = player1.strip()
        player1 = player1.lower()
        
		#game will only accept "correct" answers
		if player1 not in gameDictionary:
            print('Invalid input!')
            break
        
		#defines the choices the computer can make, also has the computer randomly select one of the choices
		#these are compared along with the player chocie to the gameDictionary and the numberical difference is calculated
		computerChoiceList = ['rock', 'paper', 'scissors']
        computerChoice = random.choice(computerChoiceList)
        print('Computer chooses:', computerChoice)
        one = gameDictionary.get(player1)
        two = gameDictionary.get(computerChoice)
        result = one - two
        
		#Since we are working with three different values, the math matrix works to define win/ loss conditions
		if result in [0]:
            print('The game is a draw')
            print('Player 1 score: ', player1score)
            print('Computer score: ', computerScore)
        
		#Conditions in which the human player wins 
		elif result in [-2, 1]:
            print('Player one wins!')
            player1score = int(player1score) + 1
            
			#If you win 3 out of 5 games, the game is over 
			if player1score == 3:
                print('Player 1 has won three games out of five!')
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore) 
                break
            
			#otherwise, print the current match scores 
			else:
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
        
		#conditions in which the computer wins 
		elif result in [-1, 2]:
            print('Computer wins!')
            computerScore = int(computerScore) + 1
            
			#likewise, if the computer wins 3 out of 5 times, the game is over 
			if computerScore == 3:
                print('Computer has won three games out of five!')
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
                break
            
			#again, will just print match score if 3 out of 5 hasn't been reached
			else:
                print('Player 1 score: ', player1score)
                print('Computer score: ', computerScore)
    
	#if while True breaks, game will end and then restart 
	print('Game over, thanks for playing!') 
