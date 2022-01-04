#! /usr/bin/env python3
def integer_check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def character_input(): #X (denotes difficulty rating out of five)
    '''
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old.
    '''
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

def odd_or_even(): #X
    '''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
    to the user.
    '''
    number = input('Enter a number:\n')
    if integer_check(number) is False:
        print('Invalid input.')
        exit()
    number = int(number)
    if number % 2 == 0:
        print('That is an even number.')
    elif number % 2 != 0:
        print('That is an odd number.')

def list_less_than_ten(): #XX
    '''
    Take a list, say for example this one:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [x for x in a if x < 10]
    print(b)

def divisor_list(): #XX
    '''
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
    '''
    number = int(input('Enter a number:\n'))
    print([x for x in range(1, number + 1) if number % x == 0])

def list_overlap(): #XX
    '''
    Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists
    (without duplicates). Make sure your program works on two lists of different sizes.
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [x for x in a if x in b]
    print(c)

def string_lists(): #XX
    '''
    Ask the user for a string and print out whether this string is a palindrome or not. 
    '''
    word = input("Please enter a word:\n")
    reverse_word = worrd[::-1]
    if word == reverse_word:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")

def list_comprehensions(): #XX
    '''
    Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
    Python that takes this list a and makes a new list that has only the even elements of this list in it.
    '''
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0]
    print(b)

def rock_paper_scissors(): #XXX
    '''
    Make a two-player Rock-Paper-Scissors game.
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
                print('But wait, your choice is an invalid input!\nGame resetting...\n\n\n')
                time.sleep(3)
            except KeyboardInterrupt:
                print('Program termianted.')
                exit()

def guessing_game_one(): #XXX
    '''
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
    whether they guessed too low, too high, or exactly right. 
    '''
    import random
    random_number = random.randint(1,9)
    correct_guess = False
    while correct_guess is False:
        guess = int(input('Guess a number:\n'))
        if guess == random_number:
            print('That is the right number!')
            correct_guess = True
        elif guess < random_number:
            print('That guess is too low.')
        elif guess > random_number:
            print('That guess is too high.')

def list_overlap_comprehensions(): #XX
    '''
    This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution
    in a different way.

    Take two lists, say for example these two:

            a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists
    (without duplicates). Make sure your program works on two lists of different sizes.
    '''
    import random
    a = random.sample(range(1, 100), 25)
    b = random.sample(range(1, 100), 25)
    c = [x for x in a if x in b]
    print('List A:', a)
    print('List B:', b)
    print('Common items:', c)
