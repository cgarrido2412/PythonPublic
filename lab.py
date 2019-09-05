import random
print('Rock, Paper, Scissors!')
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
