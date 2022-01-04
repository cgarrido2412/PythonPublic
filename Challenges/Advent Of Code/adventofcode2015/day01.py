#! /usr/bin/env python3
'''
Author: Charles Garrido

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the
directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the
instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down
one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?
'''

def file_test(file):
    try:
        open(file)
    except FileNotFoundError:
        print('Unable to open:', file)
        exit()

def main():
    file_test(r'C:\Users\cgarrido\Desktop\lab.txt')
    file = open(r'C:\Users\cgarrido\Desktop\lab.txt').read()
    floor = 0
    for x in file:
        if x == '(':
            floor += 1
        elif x == ')':
            floor -= 1
    print(floor)

if __name__ == '__main__':
    main()
