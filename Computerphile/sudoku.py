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
    clean_grid = '''
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    ------+------+------
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    ------+------+------
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    {} {} {} |{} {} {} |{} {} {} 
    '''.format(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], grid[0][5], grid[0][6], grid[0][7], grid[0][8],
               grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], grid[1][5], grid[1][6], grid[1][7], grid[1][8],
               grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], grid[2][5], grid[2][6], grid[2][7], grid[2][8],
               grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], grid[3][5], grid[3][6], grid[3][7], grid[3][8],
               grid[4][0], grid[4][1], grid[4][2], grid[4][3], grid[4][4], grid[4][5], grid[4][6], grid[4][7], grid[4][8],
               grid[5][0], grid[5][1], grid[5][2], grid[5][3], grid[5][4], grid[5][5], grid[5][6], grid[5][7], grid[5][8],
               grid[6][0], grid[6][1], grid[6][2], grid[6][3], grid[6][4], grid[6][5], grid[6][6], grid[6][7], grid[6][8],
               grid[7][0], grid[7][1], grid[7][2], grid[7][3], grid[7][4], grid[7][5], grid[7][6], grid[7][7], grid[7][8],
               grid[8][0], grid[8][1], grid[8][2], grid[8][3], grid[8][4], grid[8][5], grid[8][6], grid[8][7], grid[8][8])
    print(clean_grid)
    input('More?')

def main():
    try:
        grid = [[] for x in range(9)]
        for i in range(len(grid)):
            grid[i] = list(input('Enter row:\n'))
            if len(grid[i]) != 9:
                print('You have missed a number.')
                break
            try:
                grid[i] = [int(x) for x in grid[i]]
            except ValueError:
                print('One of your inputs could not be converted to an integer.')
                exit()
        print(np.matrix(grid))
        solve()
    except IndexError:
        print('The puzzle could not be solved.')
    except KeyboardInterrupt:
        print('Program terminated.')
    
if __name__ == '__main__':
    main()
