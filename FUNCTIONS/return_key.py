#!/usr/bin/env python3

'''
Return key for key, value in dictionary
'''

import random

#Function to return key
def return_key(some_dictionary, value):
    return list(some_dictionary.keys())[list(some_dictionary.values()).index(value)]

if __name__ == "__main__":
    #Define dicitonary
    characters = {'evangelo':1, 'walker':2, 'holly':3, 'mom':4, 'doc':5, 'hoffman':6, 'jim':7, 'karlee':8, 'heng':9, 'sharice':10, 'dan':11, 'tala':12}

    #Select a random value
    number = random.randint(1,12)

    #Print key from value
    selected_character = return_key(characters, number)
    print(selected_character)