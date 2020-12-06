#! /usr/bin/env python3

'''
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

if __name__ == '__main__':
    boarding_passes = open(r'C:\Users\I539067\Desktop\Prisma API\Documents\puzzle_input.txt').read().splitlines()
    seat_ids = []
    for x in range(len(boarding_passes)):
        row = find_row(boarding_passes[x])
        column = find_column(boarding_passes[x])
        seat_id = row[0] * 8 + column[0]
        seat_ids.append(seat_id)
        announcement = 'Your seat is row {}, column {}, seat ID {}'.format(row, column, seat_id)
        print(announcement)
    print('The highest seat ID is:', max(seat_ids))
