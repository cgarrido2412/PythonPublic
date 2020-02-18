#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import numpy as np

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input('More?')
    
if __name__ == '__main__':
    try:
        grid = [[4,0,7,0,0,8,0,0,3],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,9,0,5,2,0],
                [0,0,8,7,3,0,0,0,2],
                [0,6,0,0,0,0,0,0,0],
                [1,0,0,6,0,0,0,0,0],
                [0,0,0,0,2,0,4,0,5],
                [0,4,0,8,0,1,0,7,0],
                [0,0,6,0,0,0,0,8,0]]
        grid[0] = list(input('Enter first row:\n'))
        grid[0] = [int(x) for x in grid[0]]
        
        grid[1] = list(input('Enter second row:\n'))
        grid[1] = [int(x) for x in grid[1]]

        grid[2] = list(input('Enter thrid row:\n'))
        grid[2] = [int(x) for x in grid[2]]

        grid[3] = list(input('Enter fourth row:\n'))
        grid[3] = [int(x) for x in grid[3]]

        grid[4] = list(input('Enter fifth row:\n'))
        grid[4] = [int(x) for x in grid[4]]

        grid[5] = list(input('Enter sixth row:\n'))
        grid[5] = [int(x) for x in grid[5]]

        grid[6] = list(input('Enter seventh row:\n'))
        grid[6] = [int(x) for x in grid[6]]

        grid[7] = list(input('Enter eigth row:\n'))
        grid[7] = [int(x) for x in grid[7]]

        grid[8] = list(input('Enter ninth row:\n'))
        grid[8] = [int(x) for x in grid[8]]
        print(np.matrix(grid))
        solve()
    except KeyboardInterrupt:
        print('Program terminated.')
