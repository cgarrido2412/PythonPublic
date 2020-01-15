#! /usr/bin/env python3
'''
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a
password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
'''

def check_duplicates(some_list):
    if len(some_list) == len(set(some_list)):
        return False
    else:
        return True

def deduplicate(x):
    return list(dict.fromkeys(x))

puzzle = open('lab.txt', 'r').read()
puzzle = puzzle.split('\n')

new_list = []
for i in range(len(puzzle)):
    x = puzzle[i].split()
    new_list.append(x)

my_list = []
for i in range(len(new_list)):
    my_list.append(deduplicate(new_list[i]))

answer_list = []
for i in range(len(my_list)):
    x = len(my_list[i])
    answer_list.append(x)

print(sum(answer_list)) #ANSWER IS TOO HIGH
