#! /usr/bin/env python3

'''
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. 
None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''

if __name__ == "__main__":
    #Load the puzzle and split by line to get each individual expense in a list. 
    expense_report = open(r'C:\Users\\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    expenses = expense_report.split('\n')

    #Part one is to find two numbers in the list of expenses that add to 2020 and find their product. 
    def part_one():
        for x in range(len(expenses)):
            for y in range(x + 1, len(expenses)):
                if int(expenses[x]) + int(expenses[y]) == 2020:
                    first_item = expenses[x]
                    second_item = expenses[y]
                    product = int(expenses[x]) * int(expenses[y])
                    answer = 'First item: {}\nSecond item: {}\nAnswer: {}'.format(first_item, second_item, product)
                    print(answer)

    #Part two is to find three numbers in the list of expenses that add to 2020 and find their product. 
    for x in range(len(expenses)):
        for y in range(x + 1, len(expenses)):
            for z in range(x + 2, len(expenses)):
                if int(expenses[x]) + int(expenses[y]) + int(expenses[z]) == 2020:
                    first_item = expenses[x]
                    second_item = expenses[y]
                    third_item = expenses[z]
                    product = int(expenses[x]) * int(expenses[y]) * int(expenses[z])
                    answer = 'First item: {}\nSecond item: {}\nThird item: {}\nAnswer: {}'.format(first_item, second_item,third_item, product)
                    print(answer)
