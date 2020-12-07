#! /usr/bin/env python3

import os

'''
You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

#Separating these multi-line strings so that my thinking notes are separate from the problem description. 

'''
Notes:

>>> x = list(range(11,21))
>>> x
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> mode = 'F'
>>> if mode == 'F':
...     i = list(range((int(len(x)/2)),len(x)))
...     for n in i:
...         while n <= len(x)-1:
...             del x[n]
...
>>> x
[11, 12, 13, 14, 15]



>>> x = list(range(11,21))
>>> x
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> mode = 'B'
>>> if mode == 'B':
...     x = x[len(x)//2:]
...
>>> x
[16, 17, 18, 19, 20]
'''

def find_row(boarding_pass):
    row = list(range(0,128))
    for letter in boarding_pass:
        if letter == 'F':
            i = list(range((int(len(row)/2)),len(row)))
            for n in i:
                while n <= len(row)-1:
                    del row[n]
        elif letter == 'B':
            row = row[len(row)//2:]
        else:
            pass
    return row 

def find_column(boarding_pass):
    column = list(range(0,8))
    for letter in boarding_pass:
        if letter == 'L':
            i = list(range((int(len(column)/2)),len(column)))
            for n in i:
                while n <= len(column)-1:
                    del column[n]
        elif letter == 'R':
            column = column[len(column)//2:]
        else:
            pass
    return column 

def find_missing(number_list):
    return [x for x in range(number_list[0], number_list[-1]+1) if x not in number_list]

if __name__ == '__main__':
    boarding_passes = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read().splitlines()
    seat_ids = []
    for x in range(len(boarding_passes)):
        row = find_row(boarding_passes[x])
        column = find_column(boarding_passes[x])
        seat_id = row[0] * 8 + column[0]
        seat_ids.append(seat_id)
        announcement = 'Your seat is row {}, column {}, seat ID {}'.format(row, column, seat_id)
        #print(announcement)
    
    #Answer to part 1
    #print('The highest seat ID is:', max(seat_ids))

    #Answer to part 2
    empty_seats = find_missing(sorted(seat_ids))
    print(empty_seats)
