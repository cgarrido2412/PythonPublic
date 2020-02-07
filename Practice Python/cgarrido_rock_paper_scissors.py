#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import random
import time 

def return_key(choice):
    gameDictionary = {'rock':1,
                      'paper':2,
                      'scissors':3}
    return_value = gameDictionary.get(choice)
    return return_value

def compare_results(x,y):
    result = x - y
    if result in [0]:
        print("The game is a draw.\nGame resetting...\n\n\n")
        time.sleep(3)
    elif result in [-2, 1]:
        print('Player one wins!\nGame resetting...\n\n\n')
        time.sleep(3)
    elif result in [-1, 2]:
        print('Computer player wins!\nGame resetting...\n\n\n')
        time.sleep(3)

if __name__ == '__main__':
    while True:
        try:
            print('Rock, paper, scissors!\nPress [ctrl+c] to exit.')
            choice = str(input('Player one chooses:\n')).lower()
            choice = choice.strip()
            first_comparison = return_key(choice)
            computer_choice = random.sample(['rock', 'paper', 'scissors'], 1)
            time.sleep(1)
            print('Computer chooses:', computer_choice[0])
            time.sleep(1)
            second_comparison = return_key(computer_choice[0])
            compare_results(first_comparison, second_comparison)
        except TypeError:
            print('Invalid input!\nGame resetting...\n\n\n')
            time.sleep(3)
        except KeyboardInterrupt:
            print('Program termianted.')
            exit()
