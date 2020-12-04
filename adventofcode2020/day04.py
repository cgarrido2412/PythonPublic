#! /usr/bin/env python3

import ast
import os 

def validate(passport):
    for f in fields:
        if f in passport.keys():
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    #Load the puzzle and break into individual passports based on whitespace line
    puzzle_input = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()

    #The prerequsite fields for a valid passport
    fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    #Valid passports
    count = 0

    #Separate by line breaks for each individual passport. 
    passports = puzzle_input.split('\n\n')

    #Convert each passport into a string dictionary
    for x in range(len(passports)):
        passports[x] = passports[x].replace('\n', ' ') 
        passports[x] = passports[x].replace(' ', ', ') 
        passports[x] = "'" + '{' + passports[x] + '}' + "'"
        passports[x] = {k:v for (k,v) in [s.split(':') for s in passports[x].strip('{}').split(', ')]}
        
    for x in range(len(passports)):
        for y in passports:
            if validate(passports[x]):
                count += 1

    print(count) #Fuck me, my answer is too high. :( 
