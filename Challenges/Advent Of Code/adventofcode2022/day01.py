#!/usr/bin/env python3

'''
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. 
As your boats approach land, the Elves begin taking inventory of their supplies. 
One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. 
Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

import os 

if __name__ == "__main__":

    #Read Puzzle Input. Split by line break. 
    calories_carried = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day01_input.txt').read().split('\n\n')
    
    #Split data into what each elf is carrying. 
    elf_loads = []
    for elf in range(len(calories_carried)):
        elf_load = calories_carried[elf].split('\n')
        elf_loads.append(elf_load)

    #Determine the total number of calories carried by each elf. 
    total_calories = []
    for each_elf in range(len(elf_loads)):
        calorie_count = [int(x) for x in elf_loads[each_elf]]
        caloric_total = sum(calorie_count)
        total_calories.append(caloric_total)

    #Sort list, print largest number of calories carried. 
    total_calories.sort()
    print(total_calories[-1]) #Day01 Correct and Complete. 

    '''
    Part 2 needs the sum of the larges three values
    '''

    #Print sum of largest three values 
    print(sum(total_calories[-3:])) #Day01 Part 2 Correct and Complete. 
