#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import random

def return_key(choice):
    gameDictionary = {'rock':1,
                      'paper':2,
                      'scissors':3}
    first_return = gameDictionary.get(choice)
    return first_return

def compare_results(x,y):
    result = x - y
    if result in [0]:
        print("The game is a draw.\n")
    elif result in [-2, 1]:
        print('Player one wins!\n')
    elif result in [-1, 2]:
        print('Computer player wins!\n')

if __name__ == '__main__':
    while True:
        try:
            print('Rock, paper, scissors!\nPress [ctrl+c] to exit.')
            choice = str(input('Player one chooses:\n')).lower()
            choice = choice.strip()
            one = return_key(choice)
            computer_choices = ['rock', 'paper', 'scissors']
            computer_choice = random.sample(computer_choices, 1)
            print('Computer chooses:', computer_choice[0])
            two = return_key(computer_choice[0])
            compare_results(one, two)
        except KeyboardInterrupt:
            print('Program termianted.')
            exit()
