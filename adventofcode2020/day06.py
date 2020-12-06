#! /usr/bin/env python3

def deduplicate(x):
    return list(set(x))

if __name__ == '__main__':
    forms = open(r'C:\Users\I539067\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    groups = forms.split('\n\n')
    people = []
    for x in range(len(groups)):
        person = groups[x].split('\n')
        people.append(person)

    answered = 0

    for x in range(len(people)):
        uniques = ''.join(people[x])
        uniques = deduplicate(uniques)
        answered += len(uniques)

    print(answered)
