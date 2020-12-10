#! /usr/bin/env python3

import os 

def count_difference(adapters):
    adapters.sort()
    ones = 0
    threes = 0

    for x in range(len(adapters) -1):
        difference = adapters[x+1] - adapters[x]
        if difference == 1:
            ones += 1
        elif difference == 3:
            threes += 1

    #threes + 1 because our device's built-in joltage adapter is rated 3 higher than the highest-rated adapter
    return ones, threes + 1

if __name__ == '__main__':
    adapters = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()

    #Remembering that the charging outlet itself has an effective rating of 0 jolts, including a 0 at the start of our list
    adapters = [0] + [int(x) for x in adapters.split('\n')]

    ones, threes = count_difference(adapters)

    print(ones * threes)
