#! /usr/bin/env python3

def find_missing_number(x):
        length = len(x)
        total = (length + 1)*(length + 2)/2
        list_sum = sum(x)
        return total - list_sum

if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 7, 8, 9, 10]
        missed_number = find_missing_number(x)
        print(int(missed_number))
