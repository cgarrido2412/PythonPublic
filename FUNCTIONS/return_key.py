#!/usr/bin/env python3

'''
Return key for key, value in dictionary
'''

import random

#Function to return key
def return_key(some_dictionary, value):
    return list(some_dictionary.keys())[list(some_dictionary.values()).index(value)]

#Simpler method
def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

if __name__ == "__main__":
    #Define dicitonary
    characters = {'evangelo':1, 'walker':2, 'holly':3, 'mom':4, 'doc':5, 'hoffman':6, 'jim':7, 'karlee':8, 'heng':9, 'sharice':10, 'dan':11, 'tala':12}

    #Print key from value
    selected_character = return_key(characters, random.randint(1,12))
    second_character = get_key(characters, random.randint(1,12))
    print(selected_character, second_character)