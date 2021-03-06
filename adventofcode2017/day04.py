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

def remove_duplicates(list_one):
    list_two = []
    if list_one:
        for item in list_one:
            if item not in list_two:
                list_two.append(item)
    else:
        return list_one
    return list_two

def between_lists(li1, li2):
    li3 = []
    if li1:
        for item in li1:
            if item not in li2:
                li3.append(item)
    else:
        return li1
    return li3 #between_lists([1, 2, 3], [1, 2, 4]) only returns [3]

puzzle = open('lab.txt', 'r').read()
puzzle = puzzle.split('\n')

new_list = []
for i in range(len(puzzle)):
    x = puzzle[i].split()
    new_list.append(x)

my_list = []
for i in range(len(new_list)):
    my_list.append(deduplicate(new_list[i]))  

my_list = set(x for l in my_list for x in l) 
print(len(my_list)) #3671 incorrect, too high
