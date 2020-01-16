#write a program that returns a list that contains only the elements that are common between the lists
import random 
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 10)
commonList = set();
[commonList.add(x) for x in a for y in b if x == y]
print('List A:', list(a))
print('List B:', list(b))
print('Common between A and B:', list(commonList))

'''
Another way:

#! /usr/bin/env python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in b if x in a]
print(c)
'''
