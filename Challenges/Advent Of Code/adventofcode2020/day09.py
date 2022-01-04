#! /usr/bin/env python3

import os 

def file_check(file):
    try:
        open(file)
    except FileNotFoundError:
        print('File not found.')
        exit()

def firstInvalid(sequence, preambleLength):
    #Starting range after first 25 numbers... or whatever the preamble lengh is (in case it changes)
    for i in range(preambleLength, len(sequence)):
        num = sequence[i]
        found = False 

        #Compare all the number pairings in the last n numbers to see which two create the correct sum
        for j in range(i - preambleLength, i):
            for k in range(j, i):
                if sequence[j] + sequence[k] == num:
                    found = True
                    break 

            if found:
                break 

        if not found:
            return num 

    #Return -1 if everything seems to be valid
    return -1 

#Python function to find sum between two indexes
#When there is no update
def find_ans(array, j, k):
    length = len(array)
    for index in range(1, length):
        array[index] = array[index] + array[index - 1]
        print(array[k] - array[j - 1])
        return 

if __name__ == '__main__':
    puzzle_file = os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt'
    file_check(puzzle_file)
    data =  open(puzzle_file).read()

    sequence = [int(x) for x in data.split('\n')]

    #This is the answer to part one
    invalid_number = firstInvalid(sequence, 25)  

    #Create a list of the total sum at any given index
    prefixSums = [0]
    for i in sequence:
        prefixSums.append(prefixSums[-1] + i)

    # Sum([0, all]) - Sum([0, 10]) == Sum([10, all])
    # Example: [1,2,3,4,5]
    # sum[1,2,3,4,5] - sum[1,2,3] == sum[4,5]
    for x in range(len(sequence)):
        for y in range(x + 1, len(sequence)):
            rangeSum = prefixSums[y+1] - prefixSums[x]
            if rangeSum == invalid_number:
                low = min(sequence[x:y + 1])
                hi = max(sequence[x:y + 1])
                print(hi+low)
