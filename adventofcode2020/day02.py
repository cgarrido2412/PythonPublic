#! /usr/bin/env python3

'''
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

import os 

if __name__ == "__main__":
    #Load the puzzle
    password_manifest = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    
    #Method, split by lines and spaces. Range length indexing for comparing numbers to letter to string. 

    #Split into lines for each password policy (use grouper)
    passwords = password_manifest.split('\n')
    #print(passwords[0]) '14-15 v: vdvvvvvsvvvvvfpv'

    parameters = []
    for x in range(len(passwords)):
        parameter = passwords[x].split(' ')
        parameters.append(parameter)

    #print(parameters[0]) ['14-15', 'v:', 'vdvvvvvsvvvvvfpv']
    #print(parameters[0][0]) '14-15'

    number_frequency_list = []
    letter_list = []
    password_string_list = []
    for x in range(len(parameters)):
        number_frequency = parameters[x][0]
        number_frequency_list.append(number_frequency)
        letter = parameters[x][1]
        letter_list.append(letter)
        password_string = parameters[x][2]
        password_string_list.append(password_string)

    #print(number_frequency_list[0]) 14-15
    #print(letter_list[0][:-1]) 'v'
    '''
    test = 'the quick brown fox jumped over the lazy dogs'
    new = test.count('e')
    print(new) 4
    '''

    #Part one is to find number of occurences of letter within range parameters for each password. 
    def part_one():
        valid_count = 0
        for x in range(len(number_frequency_list)):
            range_parameters = number_frequency_list[x].split('-')
            low_end = int(range_parameters[0]) 
            low_check = 'Low end value: {}'.format(low_end)
            print(low_check)

            high_end = int(range_parameters[1])
            high_check = 'High end value: {}'.format(high_end)
            print(high_check)

            match_character = letter_list[x][:-1]
            match_check = 'Match character: {}'.format(match_character)
            print(match_check)

            test_password = password_string_list[x]
            password_check = 'Password: {}'.format(test_password)
            print(password_check)

            occurences = test_password.count(match_character)
            occur_check = 'Occurences: {}'.format(occurences)
            print(occur_check)

            '''
            Low end value: 16
            High end value: 20
            Match character: j
            Password: vjkjjcjjrjjmtnbjjjnj
            Occurences: 11
            '''

            if occurences in range(low_end, high_end+1):
                valid_count += 1
                print('The valid count is:', valid_count)
            else:
                pass 

        print('The final valid count is:', valid_count) #Correct answer! 

    #Part two is to compare the positional indecies of the password string according to the match letter
    valid_count = 0 
    for x in range(len(number_frequency_list)):
        index_parameters = number_frequency_list[x].split('-')

        if int(index_parameters[0]) - 1 < 0:
            first_index = 0
        else:
            first_index = int(index_parameters[0]) - 1

        second_index = int(index_parameters[1]) - 1

        match_character = letter_list[x][:-1]
        match_check = 'Match character: {}'.format(match_character)
        print(match_check)

        test_password = password_string_list[x]
        password_check = 'Password: {}'.format(test_password)
        print(password_check)

        if test_password[first_index] == test_password[second_index]:
            pass
        elif test_password[first_index] == match_character:
            valid_count += 1
        elif test_password[second_index] == match_character:
            valid_count += 1

    print('The final valid count is:', valid_count) #Correct answer!
