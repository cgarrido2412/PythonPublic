#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

def first_function():
    a = 'python'
    return a

def second_function():
    b = 'is'
    return b

def third_function():
    c = 'excellent'
    return c

if __name__ == '__main__':
    try:
        x = first_function()
        y = second_function()
        z = third_function()
        print(x[0] + z[0] + x[len(x) - 1] + y)
    except:
        print('Program terminated.')
