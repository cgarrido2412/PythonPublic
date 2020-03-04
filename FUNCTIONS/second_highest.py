def deduplicate(x):
    return list(dict.fromkeys(x))

def second_highest(x):
    x.sort()
    x = deduplicate(x)
    return x[len(x)-2]

test = [10, 9, 8, 7, 6, 5, 5, 5, 5, 4, 3, 2, 1]

print(second_highest(test))
