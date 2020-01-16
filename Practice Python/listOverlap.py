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
import random
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 10)
c = [x for x in a if x in b]
print('List A:', a)
print('List B:', b)
print('Common elements:', c)

'''
