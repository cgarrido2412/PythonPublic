#!/usr/bin/env python3

'''
>>> test_str = 'mjpsHcssDzLTzMsz'
>>> res_first = test_str[0:len(test_str)//2]
>>> res_second = test_str[len(test_str)//2 if len(test_str)%2 == 0 else ((len(test_str)//2)+1):]
>>> print(res_first)
mjpsHcss
>>> print(res_second)
DzLTzMsz
>>> len(res_first)
8
>>> len(res_second)
8
'''

import os 

def deduplicate(x):
    return list(dict.fromkeys(x))

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == "__main__":

    #Read Puzzle Input. Split by line. 
    rucksacks = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day03_input.txt').read().split('\n')

    #Create alphabet string to represent item priority
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #Maintain a list of each rucksacks' priority
    rucksack_priority_manifest = []

    #Iterate through all the rucksacks
    for x in range(len(rucksacks)):

        #Split string of rucksack contents into halves
        first_compartment = rucksacks[x][0:len(rucksacks[x])//2]
        second_compartment = rucksacks[x][len(rucksacks[x])//2 if len(rucksacks[x])%2 == 0 else ((len(rucksacks[x])//2)+1):] #Each string is even but wrote this out for odd length strings just in case

        #List comprehension for the common elements between strings, then deduplicate as there is only one unique matching element between compartments of the rucksacks
        common_item = [x for x in first_compartment if x in second_compartment]
        common_item = deduplicate(common_item)

        #Rucksack priority starts at 0
        rucksack_priority = 0

        #Compare the common element to where it falls alphabetically in the priority list, then assign the rucksack priority
        for y in range(len(priority)):
            if common_item[0] == priority[y]:
                rucksack_priority = y+1 

        #Add the final rucksack priority to our list 
        rucksack_priority_manifest.append(rucksack_priority)

    #Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
    print(sum(rucksack_priority_manifest)) #Part one correct and complete 

    '''
    Part 2 is to find the common element from each three lines of the rucksacks 
    '''

    #Use Chunker function to split lines into groups of three 
    badge_groups = list(chunker(rucksacks, 3))

    #Start a list to collect each groups' priority
    group_priority_manifest = [] 

    #Iterate through each group
    for x in range(len(badge_groups)):
        current_group = badge_groups[x]
        common = [y for y in current_group[0] if y in current_group[1] and y in current_group[2]] #Find common element in a three way comparison
        common = deduplicate(common) #Ensure it's only one element

        #Group priority starts at 0
        group_priority = 0

        #Compare the common element to where it falls alphabetically in the priority list, then assign the group priority
        for y in range(len(priority)):
            if common[0] == priority[y]:
                group_priority = y+1

        #Add the final group priority to our list
        group_priority_manifest.append(group_priority)
    
    #Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
    print(sum(group_priority_manifest)) #Part two correct and complete 
