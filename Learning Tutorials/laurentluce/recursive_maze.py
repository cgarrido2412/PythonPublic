#!Python3
#https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/

'''
We use a nested list of integers to represent the maze. The values are the following:

0: empty cell
1: unreachable cell: e.g. wall
2: ending cell
3: visited cell
'''
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]
'''
This is a very simple algorithm which does the job even if it is not an efficient algorithm.
It walks the maze recursively by visiting each cell and avoiding walls and already visited cells.

The search function accepts the coordinates of a cell to explore. If it is the ending cell, it returns True.
If it is a wall or an already visited cell, it returns False. The neighboring cells are explored recursively and
if nothing is found at the end, it returns False so it backtracks to explore new paths.
We start at cell x=0 and y=0.
'''
def search(x, y):
    if grid[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print ('visited at %d,%d' % (x, y))
        return False
    
    print ('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

search(0, 0)
