#! /usr/bin/env python3
def integer_check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def character_input():
    from datetime import date
    today = date.today()
    year = today.strftime("%Y")
    name = input('What is your name?\n')
    age = input('How old are you [integer]?\n')
    if integer_check(age) is False:
        print('Invalid input.')
        exit()
    birth_year = int(year) - int(age)
    lifespan = int(birth_year) + 100
    print('Hello', name + '! You will turn 100 years old in the year', lifespan)

def odd_or_even():
    number = input('Enter a number:\n')
    if integer_check(number) is False:
        print('Invalid input.')
        exit()
    number = int(number)
    if number % 2 == 0:
        print('That is an even number.')
    elif number % 2 != 0:
        print('That is an odd number.')

def list_less_than_ten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if i < 5:
            b.append(i)
        else:
            pass
    print(b)

def divisor_list():
    number = int(input('Enter a number:\n'))
    divisor_list = []
    for x in range(1, number+1):
        if number % x == 0:
            divisor_list.append(x)
        else:
            pass
    print(divisor_list)

def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [x for x in a if x in b]
    print(c)
