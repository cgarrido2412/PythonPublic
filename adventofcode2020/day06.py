#! /usr/bin/env python3

from functools import reduce

def deduplicate(x):
    return list(set(x))

if __name__ == '__main__':
    forms = open(r'C:\Users\I539067\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    groups = forms.split('\n\n')
    people = []
    for x in range(len(groups)):
        person = groups[x].split('\n')
        people.append(person)

    def part_one():
        answered = 0
        for x in range(len(people)):
            uniques = ''.join(people[x])
            uniques = deduplicate(uniques)
            answered += len(uniques)
        print(answered)

    unanimous = 0
    for x in range(len(people)):
        res = list(reduce(lambda i, j: i & j, (set(y) for y in people[x]))) #https://www.geeksforgeeks.org/python-find-common-elements-in-list-of-lists/
        unanimous += len(res)

    print(unanimous)
