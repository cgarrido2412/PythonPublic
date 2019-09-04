import random
import time
print('rock, paper, scissors!')
player1 = str(input('Player 1 enter a choice:'))
gameDict = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
computerChoices = ['rock', 'paper', 'scissors']
computer = random.choice(computerChoices)
print('computer is thinking...')
time.sleep(5)
print('computer chooses:', computer) 
p1 = gameDict.get(player1)
c1 = gameDict.get(computer)
result = p1 - c1 
if result in [0]:
    print('Draw')
elif result in [-2, 1]:
    print('You win!')
elif result in [-1, 2]:
    print('Computer wins')
