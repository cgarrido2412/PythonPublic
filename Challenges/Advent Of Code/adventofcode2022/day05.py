#!/usr/bin/env python3

import os

def part_one(cargo):
    #Part 1
    for line in cargo[1].split('\n'):
        instructions = line.split(' ')
        amount, source, destination = map(int, [instructions[1], instructions[3], instructions[5]])
        source -= 1
        destination -= 1

        for _ in range(amount):
            pop = stacks[source].pop()
            stacks[destination].append(pop)

    tops = [stack[-1] for stack in stacks]
    answer = ''.join(tops)
    return answer

if __name__ == "__main__":

    cargo = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day05_input.txt').read()[:-1].split('\n\n') #Separate diagram from instructions
    
    #print(cargo[0])
    '''
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9
    '''

    #cargo[1] 
    #move 3 from 6 to 2\nmove 5 from 6 to 7\nmove 6 from 2 to 5\nmove 1 from 9 to 7\n.... Will be addressed later. 

    columns = 9 
    rows = 8

    drawing = cargo[0].split('\n')
    stacks = [[] for _ in range(columns)]
    
    for x in range(rows):
        row = drawing[x]
        crates = row[1::4]
        for y in range(len(crates)):
            if crates[y] != ' ':
                stacks[y].append(crates[y])

    #print(stacks) #[['C', 'Q', 'B'], ['Z', 'W', 'Q', 'R'], ['V', 'L', 'R', 'M', 'B'],.... We need to reverse so that stacks[0][0] == 'B'

    stacks = [stack[::-1] for stack in stacks]
    #print(stacks[0]) #['B', 'Q', 'C']

    #part_one = part_one(cargo) #YOU CAN'T RUN PART ONE AND TWO IN THE SAME SCRIPT, IT CHANGES THE STACKS (I'm dumb)
    #print(part_one) #Part one correct and complete

    #Part 2
    for line in cargo[1].split('\n'):
        instructions = line.split(' ')
        amount, source, destination = map(int, [instructions[1], instructions[3], instructions[5]])
        source -= 1
        destination -= 1

        stacks[destination].extend(stacks[source][-amount:])
        stacks[source] = stacks[source][:-amount]

    tops = [stack[-1] for stack in stacks]
    print(''.join(tops)) #Part 2 correct and complete
