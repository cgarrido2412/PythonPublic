#! /usr/bin/env python3

test = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8, 9]

def deduplicate_1(x):
    return list(dict.fromkeys(x))

def deduplicate_2(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def deduplicate_3(x):
    return list(set(x))

print(deduplicate_1(test))
print(deduplicate_2(test))
print(deduplicate_3(test))
