#! /usr/bin/env python3
'''
Author: Charles Garrido 
'''

import wikipedia 

def caesar_encrypt(message):  
    text = ''
    L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    for symbol in message:
        if symbol in L:
            n = L.find(symbol)
            n = n + key
            if n >= len(L):
                n = n - len(L)
            elif n < 0:
                n = n + len(L)
            text = text + L[n]
        elif symbol in l:
            n = l.find(symbol)
            n = n + key
            if n >= len(l):
                n = n - len(l)
            elif n < 0:
                n = n + len(l)
            text = text + l[n]
        else:
            text = text + symbol
    return text

def validate_integer(x):
        try:
                int(x)
                return True
        except ValueError:
                return False

if __name__ == '__main__':
        try:
                while True:
                    key = input('\nPlease enter a number key:\n')
                    if validate_integer(key) is True:
                            key = int(key)
                            query = input('\nEnter something to lookup:\n')
                            search = wikipedia.page(query)
                            message = search.summary
                            print(caesar_encrypt(message))
                            with open(r'C:\Users\cgarrido\Desktop\lab.txt', 'w+') as file:
                                    file.write(caesar_encrypt(message))
                            print('\n')
                            print(r'C:\Users\cgarrido\Desktop\lab.txt has been updated.')
                    else:
                            print('You must input an integer value for the number key.')
        except KeyboardInterrupt:
                print('Program terminated.')
