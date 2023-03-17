#!/usr/bin/env python3

import random

def select_character():
    number = random.randint(1,12)
    characters = {'evangelo':1, 'walker':2, 'holly':3, 'mom':4, 'doc':5, 'hoffman':6, 'jim':7, 'karlee':8, 'heng':9, 'sharice':10, 'dan':11, 'tala':12}
    return list(characters.keys())[list(characters.values()).index(number)]

if __name__ == "__main__":
    print(select_character())