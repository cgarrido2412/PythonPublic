#!Python3
'''
You land on Eris, your last stop before reaching Santa.
As soon as you do, your sensors start picking up strange life forms moving around: Eris is infested with bugs!
With an over 24-hour roundtrip for messages between you and Earth,
you'll have to deal with this problem on your own.

Eris isn't a very large place; a scan of the entire area fits into a 5x5 grid (your puzzle input).
The scan shows bugs (#) and empty spaces (.).

Each minute, The bugs live and die based on the number of bugs in the four adjacent tiles:

A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
Otherwise, a bug or empty space remains the same.
(Tiles on the edges of the grid have fewer than four adjacent tiles; the missing tiles count as empty space.)
This process happens in every location simultaneously; that is, within the same minute,
the number of adjacent bugs is counted for every tile first, and then the tiles are updated.

Here are the first few minutes of an example scenario:

Initial state:
....#
#..#.
#..##
..#..
#....

After 1 minute:
#..#.
####.
###.#
##.##
.##..

After 2 minutes:
#####
....#
....#
...#.
#.###

After 3 minutes:
#....
####.
...##
#.##.
.##.#

After 4 minutes:
####.
....#
##..#
.....
##...
To understand the nature of the bugs,
watch for the first time a layout of bugs and empty spaces matches any previous layout.
In the example above, the first layout to appear twice is:

.....
.....
.....
#....
.#...
To calculate the biodiversity rating for this layout, consider each tile left-to-right in the top row,
then left-to-right in the second row, and so on.
Each of these tiles is worth biodiversity points equal to increasing powers of two: 1, 2, 4, 8, 16, 32, and so on.
Add up the biodiversity points for tiles with bugs; in this example,
the 16th tile (32768 points) and 22nd tile (2097152 points) have bugs,
a total biodiversity rating of 2129920.

What is the biodiversity rating for the first layout that appears twice?
'''

petri_dish = '''#.##.
###.#
#...#
##..#
.#...'''
lines = petri_dish.rstrip().split('\n') #['#.##.', '###.#', '#...#', '##..#', '.#...']
row_length = 5 #the x of the puzzle
column_length = 5 #the column_length of the puzzle
directions = [(0, -1),(0, 1),(-1, 0),(1, 0)] #down, right, left, up
current_status = {}

while True:
    state = "\n".join(lines) #Start as "#.##.\n###.#\n#...#\n##..#\n.#..."

    if state in current_status:
        break

    current_status[state] = lines #Start as ['#.##.', '###.#', '#...#', '##..#', '.#...']
    new_lines = ['']*column_length #Start as ['', '', '', '', '']

    for y in range(column_length):

        for x in range(row_length):
            count = 0

            for direct_x, direct_y in directions:
                new_x, new_y = x + direct_x, y + direct_y

                if new_x < 0 or new_y < 0 or new_x >= row_length or new_y >= column_length:
                    continue

                if lines[new_y][new_x] == '#':
                    count += 1

            char = '.'

            if lines[y][x] == '#':

                if count == 1:
                    char = '#'

            else:

                if count == 1 or count == 2:
                    char = '#'

            new_lines[y] += char

    lines = new_lines

result = 0

for y in range(column_length):

    for x in range(row_length):

        if lines[y][x] == '#':
            result += 2**(y * row_length + x)

print(result)
    
