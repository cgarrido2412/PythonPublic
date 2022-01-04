#! /usr/bin/env python3

import os

def memory_game(starting_sequence, n):
    first_time_spoken = {}
    most_recently_spoken = {}

    current_index = 0

    for number in starting_sequence:
        current_index += 1
        if number in first_time_spoken:
            most_recently_spoken[number] = first_time_spoken[number]
        first_time_spoken[number] = current_index

    previous_number = number

    while current_index < n:
        current_index += 1

        if previous_number in most_recently_spoken:
            current = first_time_spoken[previous_number] - most_recently_spoken[previous_number]
        else:
            current = 0

        if current in first_time_spoken:
            most_recently_spoken[current] = first_time_spoken[current]
        first_time_spoken[current] = current_index

        previous_number = current

    return previous_number

if __name__ == "__main__":
    #Starting numbers are: 18,8,0,5,4,1,20
    starting_numbers = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read() 

    start = [int(x) for x in starting_numbers.split(',')]

    part_one = memory_game(start, 2020)
    part_two = memory_game(start, 30000000)

    print(part_one)
    print(part_two)
