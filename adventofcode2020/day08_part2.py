#! /usr/bin/env python3

import os 

def run(program):
    accumulator = 0
    line_number = 0

    def execute(instruction):
        operation, argument = instruction.split(' ')
        if operation == 'acc':
            return int(argument), 1
        elif operation == 'jmp':
            return 0, int(argument)
        else:
            return 0, 1

    finished_lines = set()
    while line_number not in finished_lines and line_number < len(program):
        finished_lines.add(line_number)
        acc, jmp = execute(program[line_number])
        accumulator += acc
        line_number += jmp
    if line_number >= len(program):
        return accumulator

if __name__ == '__main__':
    boot_code = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()  
    instructions = boot_code.split('\n')

    for i in range(len(instructions)):
        if instructions[i].startswith('acc'):
            continue
        if instructions[i].startswith('nop'):
            copy = instructions.copy()
            copy[i] = 'jmp' + copy[i][3:]
        else:
            copy = instructions.copy()
            copy[i] = 'nop' + copy[i][3:]

        x = run(copy)
        if x:
            print(x)
            break
