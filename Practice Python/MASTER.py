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

def string_lists():
    word = input("Please enter a word:\n")
    reverse_word = worrd[::-1]
    if word == reverse_word:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")

def list_comprehensions():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0]
    print(b)

def rock_paper_scissors():
    import random
    print('Rock, paper, scissors!')
    while True:
        gameDictionary = {'rock':1,
                          'paper':2,
                          'scissors':3}
        player1 = str(input('Player one chooses:\n')).lower()
        player1 = player1.strip()
        one = gameDictionary.get(player1)
        computer_choice_list = ['rock', 'paper', 'scissors']
        computer_choice = random.sample(computer_choice_list, 1)
        print('Computer chooses:', computer_choice[0])
        two = gameDictionary.get(computer_choice[0])
        result = one - two
        if result in [0]:
            print('The game is a draw.')
            break
        elif result in [-2, 1]:
            print('Player one wins!')
            break
        elif result in [-1, 2]:
            print('Computer wins!')
            break
    print('Game over.')

def guessing_game_one():
    import random
    random_number = random.randint(1,9)
    correct_guess = False
    while correct_guess is False:
        guess = int(input('Guess a number:\n'))
        if guess == random_number:
            print('That is the right number!')
            correct_guess = True
        else:
            print('That is not the right number.')
            pass

def list_overlap_comprehensions():
    import random
    a = random.sample(range(1, 100), 25)
    b = random.sample(range(1, 100), 25)
    c = [x for x in a if x in b]
    print('List A:', a)
    print('List B:', b)
    print('Common items:', c)
