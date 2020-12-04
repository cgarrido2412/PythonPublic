#! /usr/bin/env python3

import ast
import os 

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
        print(passports[x])
        output = ""
        quoting = False
        for char in passports[x]:
            if char.isalnum():
                if not quoting:
                    output += '"'
                    quoting = True
            elif quoting:
                output += '"'
                quoting = False 
            output += char
        passports[x] = output 
        passports[x] = ast.literal_eval(passports[x])

    print(passports[2]) #{"ecl":"gry", "hcl":#"888785", "eyr":"2023", "cid":"63", "iyr":"2019", "hgt":"177cm", "pid":"656793259"}

    '''
    The problem right now is that I wrapped quotes around alphanumeric characters
    Which has caused:
        "hcl":#"888785",
    Instead of:
        "hcl":"#888785", 
    '''
