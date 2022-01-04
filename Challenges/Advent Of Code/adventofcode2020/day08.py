#! /usr/bin/env python3

import os 

def execute(instruction):
    global accumulator
    global line_number 

    operation, argument = instruction.split(' ')

    if operation == 'acc':
        accumulator += int(argument)
        line_number += 1

    elif operation == 'jmp':
        line_number += int(argument)

    else:
        line_number += 1

if __name__ == '__main__':
    boot_code = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()  
    instructions = boot_code.split('\n')

    accumulator = 0
    line_number = 0

    finished_lines = set()
    while line_number not in finished_lines:
        finished_lines.add(line_number) 
        execute(instructions[line_number])

    print(accumulator)
