#! /usr/bin/env pytyhon3
#DOES NOT WORK YET
'''
For each row, determine the difference between the largest value and the smallest value; the checksum is the sum
of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
'''
puzzle = open('lab.txt', 'r').read()
lines = puzzle.split('\n')
list_rows = []
for i in range(len(lines)):
    numbers = lines[i].split('\t')
    list_rows.append(numbers)

new_list = []
for i in range(len(list_rows)):
    new_list.append([int(x) for x in list_rows[i]])