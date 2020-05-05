#! /usr/bin/env python3

'''
Author: Charles Garrido
Last Updated: 4 May 2020

This script will allow the user to choose between adding keyphrases to a list
or generating a passowrd.

If the user chooses to add a keyphrase, their typed input will be converted to a simple leet string
then added to the existing list.

If the user chooses to generate a password,
they have to designate how many keyphrases to use
then a password will be randomly created from the keyphrase list.
'''

import random

def leet_conversion(string):
    overwrite = (('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('t', '7'))
    for old, new in overwrite:
        string = string.replace(old, new)
    return string

def generate_password(some_list):
    keyphrase_number = int(input('Please enter an integer number for the number of keyphrases to string together:\n'))
    password = '_'.join(random.sample(some_list, keyphrase_number))
    return password

if __name__ == "__main__":
    try:
        keyphrases = ['d3f4ul7', 'p4ssw0rd']
        print('Welcome to the password generator. Type [ctrl + c] to exit.')
        while True:
            mode = str(input('\nType [k] to add keyphrases.\nType [g] to generate a password.\n')).lower().strip()
            if mode == 'k':
                new_phrase = str(input('Please enter a new phrase:\n'))
                converted_new_phrase = leet_conversion(new_phrase)
                print('This will be encrypted into', converted_new_phrase)
                keyphrases.append(converted_new_phrase)
            elif mode == 'g':
                print(generate_password(keyphrases))
    except KeyboardInterrupt:
        print('Program terminated.')
