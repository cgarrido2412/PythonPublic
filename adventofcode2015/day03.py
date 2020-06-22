#! /usr/bin/env python3

'''
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls
him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v),
east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
'''

def file_test(file):
    try:
        open(file)
    except FileNotFoundError:
        print('Unable to open file.')
        exit()

def main():
    puzzle = r'C:\Users\I539067\Desktop\lab.txt'
    file_test(puzzle)
    file = open(puzzle).read()
    
    x = 0
    y = 0
    location = (x,y)
    
    visited_locations = {}
    visited_locations[location] = 1
    print(visited_locations)

    for i in file:
        if i == "^":
            location = (x,y+1)
            if location not in visited_locations:
                visited_locations[location] = 1
            else:
                visited_locations[location] += 1
        elif i == '>':
            location = (x+1,y)
            if location not in visited_locations:
                visited_locations[location] = 1
            else:
                visited_locations[location] += 1
        elif i == 'v':
            location = (x,y-1)
            if location not in visited_locations:
                visited_locations[location] = 1
            else:
                visited_locations[location] += 1
        elif i == '<':
            location = (x-1,y)
            if location not in visited_locations:
                visited_locations[location] = 1
            else:
                visited_locations[location] += 1

    print(visited_locations) #{(0, 0): 1, (0, 1): 1981, (-1, 0): 2051, (0, -1): 2068, (1, 0): 2092}

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Program terminated.')
