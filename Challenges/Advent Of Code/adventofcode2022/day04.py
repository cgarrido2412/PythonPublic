#!/usr/bin/env python3

import os 

if __name__ == "__main__":

    sections = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day04_input.txt').read().split('\n')

    full_overlap_count = 0
    any_overlap_count = 0

    for x in range(len(sections)):
        section = sections[x].split(',')
        first_elf = section[0].split('-')
        second_elf = section[1].split('-')
        first_range = range(int(first_elf[0]), int(first_elf[1])+1)
        second_range = range(int(second_elf[0]), int(second_elf[1])+1)
        first_list = []
        second_list = []
        for y in first_range:
            first_list.append(y)
        for z in second_range:
            second_list.append(z)
        overlap = [c for c in first_list if c in second_list]
        if overlap == first_list:
            full_overlap_count += 1
        elif overlap == second_list:
            full_overlap_count += 1
        if len(overlap) > 0:
            any_overlap_count += 1

    print(full_overlap_count) #Part one correct and complete 
    print(any_overlap_count) #Part two correct and complete 
