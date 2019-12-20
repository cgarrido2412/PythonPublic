#!Python3
'''
--- Day 18: Many-Worlds Interpretation ---
As you approach Neptune, a planetary security system detects you and activates a giant tractor beam on Triton!
You have no choice but to land.

A scan of the local area reveals only one interesting feature: a massive underground vault.
You generate a map of the tunnels (your puzzle input). The tunnels are too narrow to move diagonally.

Only one entrance (marked @) is present among the open passages (marked .) and stone walls (#),
but you also detect an assortment of keys (shown as lowercase letters) and doors (shown as uppercase letters).
Keys of a given letter open the door of the same letter: a opens A, b opens B, and so on.
You aren't sure which key you need to disable the tractor beam, so you'll need to collect all of them.

For example, suppose you have the following map:

#########
#b.A.@.a#
#########
Starting from the entrance (@), you can only access a large door (A) and a key (a).
Moving toward the door doesn't help you, but you can move 2 steps to collect the key, unlocking A in the process:

#########
#b.....@#
#########
Then, you can move 6 steps to collect the only other key, b:

#########
#@......#
#########
So, collecting every key took a total of 8 steps.

Here is a larger example:

########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
The only reasonable move is to take key a and unlock door A:

########################
#f.D.E.e.C.b.....@.B.c.#
######################.#
#d.....................#
########################
Then, do the same with key b:

########################
#f.D.E.e.C.@.........c.#
######################.#
#d.....................#
########################
...and the same with key c:

########################
#f.D.E.e.............@.#
######################.#
#d.....................#
########################
Now, you have a choice between keys d and e. While key e is closer,
collecting it now would be slower in the long run than collecting key d first,
so that's the best choice:

########################
#f...E.e...............#
######################.#
#@.....................#
########################
Finally, collect key e to unlock door E, then collect key f, taking a grand total of 86 steps.

Here are a few more examples:

########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
Shortest path is 132 steps: b, a, c, d, f, e, g

#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
Shortest paths are 136 steps;
one is: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m

########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
Shortest paths are 81 steps; one is: a, c, f, i, d, g, b, e, h

How many steps is the shortest path that collects all of the keys?
'''

maze = '''#################################################################################
#.................#...#.#...............#...#.........#.......#.......#.....#...#
#######.#.#######.#.#.#.#.#######.#######.#.#.###.#####.#####.#.#.###C###.#.#.#.#
#.E...#.#.#.....#...#...#.#.....#.......#.#.#t#.#.....#.#...#...#.#.#.#...#.#.#.#
#.###.###.#.###.#######.#.#.###.#######.#.###.#.#####.#.#.#.#####.#.#.#.###.#.#.#
#.#.......#...#...#...#.#.#.#.......#...#.#.........#...#.#.....#f#.....#...#a#.#
#.#########.#.#####.#.#.#.###.#####.#.###.#.#######.#####.#.###.#.#######.###.###
#...#.....#.#.....#.#...#...#.#.....#...#...#...#.#.....#.#...#.#...#h..#...#...#
#.#.#.###.#####.#.#.#######.#.#.#######.#.###.#.#.#####.###.#.#####.#.#.###.###.#
#.#.#...#.....#.#...#...#...#.#...#...#.#...#.#.#.....#...#.#.#.....#.#...#.L.#.#
###.#.#######.#.#####.#.#.###.###.###.#.#####.#.#.###.###.###.#.#####.###.###.#.#
#...#.#...#...#...#...#.#...#...#.....#.#...#.#.#...#.........#.#.......#...#...#
#.###.#.#.#.#####.#.###.###.#.#.#####.#.#.#.#.#.###.###########.#.#####.###.###.#
#.....#.#...#.....#...#...#.#.#.#.....#.#.#...#.#.....#.....#...#...#.#.#...#...#
#.#####.###.#####.###.###.#.###.#.#####.#.#####.#.#####.###.#.#####.#.#.###.#.###
#...#.#...#.#...#.#...#.#.#.#...#.....#.#.#.....#.#.....#...#...#.#.#.#...#.#...#
###.#.###.###.#.###.###.#.#.#.#.#######.#.#.#######.#####.#####.#.#.#.###.#####.#
#.#.....#.....#.....#...#.#...#.#.......#.#.......#...#.#.#.....#.#.#...#.......#
#.#####.#############.#.#.#.#####.#####.#.#######.###.#.#.###.###.#.#.###########
#.....#.#.#...........#.#...#.....#.....#.#...#...#...#.#.....#...#.#...........#
#.#.###.#.#.#.#####.#########.#####.#####.#.#.#.###.###.#.#####.#.#.###.#########
#.#.#...#...#.....#.#.......#.#.........#...#.#.....#.....#.X.#.#.#...#.#...#...#
###.#.###########.#########.#.#########.#.###.#######.#####.###.#####D#.#.#.#.#.#
#...#.#...........#.......#.#.....#.....#...#...#...#...#.#...#.......#...#...#.#
#.#.#.###.#######.#.#.#.###.#.###.#####.#.#####.###.###.#.###.#######.###.#####.#
#.#.#....k#...#...#.#.#.#...#...#.....#.#.#.....#.....#.#...#.#...V.#...#...#...#
#.#.#########.#.###.#.#.#.#####.#####.###.#.#####.#####.###.#.#.###.###.###.#.###
#.#...#.......#.#...#.#.#...#.......#...#.#.#.....#.....#...#...#...#.#.#.#.#...#
#.###.#.#######.#.###.#####.#.#########.#.#.###.#.#.#####.#######.###.#.#.#.###.#
#...#...#.......#.#.#.....#.#.#.#.......#.#.#...#.#.#.#...#.......#...R.#...#...#
#.#.#####.#######.#.#####.#.#.#.#.#####.###.#.#####.#.#.#.#W#######.#####S###.#.#
#.#......j#...#...#...I.#...#...#.#.....#...#.......#...#.#.#.....#...#.#.#.#.#.#
#.#########.###.###.###.#########.#####.#.#######.#######.#.#.###.###.#.#.#.#.#.#
#.......#.....#.....#.#.#...#.....#...#.#.......#.........#...#.#.#.#.#.#.#.#.#.#
#######.###.#.#######U#.#.#.#.#####.#.#########.###.###########.#.#.#.#.#.#.#.###
#...Y.#...#.#.........#...#.#.......#...#.#...#.#...#.............#.#.#.....#...#
#.#######.#.###.#####.#####.#########.#.#.#.#.#.#####.#############.#.#########B#
#...#.Q...#.#...#.#...#...#.#...#...#.#.#...#.#.......#i..#.....#...#.........#.#
#.#.#.#######.###.#.#####.#.#.#.#.#.###.#.###.#########.#.#.#.###.#.#########.#.#
#.#...........#p..........#...#...#.........#...........#...#.....#...N.........#
#######################################.@.#######################################
#.#.....#.#.........#.........#.....#.......#...#.......#...#.....#...G.....#...#
#.#.#.#.#.#.#####.#.#######.#.#.###.#.###.#.#.#.#.#####.#.###.###.#.#####.#.#.#.#
#...#r#.#.#.#...#n#.........#...#.#.#...#.#.#.#.#...#...#...#.#.#...#...#.#...#.#
#.###.#.#.#.#.###.###############.#.###.#.#.#.#.#.#.#.#####.#.#.#######.#.#####.#
#.#d#.#.#.....#...#.........#.....#.....#.#..m#.#.#.#.....#.#.#.....#...#...#...#
#.#.#.#.#######.#########.###.#.#######.#.#####.#.#.#####.#.#.###.#.#.#####.#.###
#...#.#.#..b....#.....#...#...#.#.....#.#.#...#.#.#.#.......#.....#...#.....#...#
#.###.#.#.#######.###.#.###.###.#.###.#.#.#.#.#.#.#.#################.#.#######.#
#.#...#...#.......#...#.#...#.#...#.#...#.#.#.#.#.#.#.....#.......#...#...#.K.#.#
###.#######.###.###.###.#.###.#####.#####.#.#.#.#.#.#.###.#.#####.#.#####.#.#.#.#
#...#.......#.#...#.....#...#.......#...#.#.#...#.#.#.#.#...#...#.....#...#.#.#.#
#.#####.#####.###.#####.###.###.#.#.###.#.###.#####.#.#.#####.#########.###.###.#
#.#...#..z#.....#...#.#.#.#...#.#.#.....#...#.#.....#.....#...#.........#.....#.#
#.#.#.###.###.#.###.#.#.#.###.###.#####.###.#.#.#.#######.###.#.#########.###.#.#
#.#.#..s#.....#.#...#.......#...#.#.#...#...#...#.#.....#.....#...#.#.....#.#.#.#
#.#.###.#######.#.#############.#.#.#.###.#########.#.#######.###.#.#.#####.#.#.#
#.....#.#.....#.#.............#...#...#.#.M...#.....#...#...#.#...#...#.....#...#
#######.#.###.#######.#####.#.#####.###.#####.#.#######.#.#.#.#.#####.###.#.#####
#...#...#.#.#.......#.....#.#...#...#...#.....#.#.....#.#.#...#.....#.....#...#.#
#O###.###.#.#######.###.###.#####.#####.#.#####.#.###.#.#.#####.###.#########.#.#
#...#.....#.....#...#.#.#...#.....#.....#.....#...#.#.#.#...#.#...#......o#...#.#
###.#########.#.#.#.#.#.#.#.#.#######.#.#####.#####.#.#.###.#.###.#######.#.###J#
#...#.........#.#.#.#.#.#.#.#.#.......#.#.......#.....#.#...#..x#.#.....#.#.....#
#.#.#.#########.#.###.#.#.###.###.#.#####.#####.#.#####.#.#####.#.#.#####.#.#####
#.#...#....g#.#.#.....#.#...#...#.#.....#.....#.#.#...#.....#...#...#.....#.#...#
#.###.#.###.#.#.###########.###.#######.#.###.###.#.#######.#.#####.#.###.###.#.#
#.#.#.#...#.#.................#.#...#...#.#.#.....#.#....v#.#.#.....#.#.#.#...#.#
#.#.#.###.#.###########.#####.#.#.#.#.#.#.#.#######.#.###.###.#.#####.#.#.#.###.#
#.#.#...#.#...F...#.....#...#.#.#.#...#.#.#.....#...#...#.....#.....#.#...#q#.#.#
#.#.###.#.#######.#.#####.#.###.#.#######.###.#.#.#.###.###########.#.#####.#.#.#
#.#...#.#.#...#...#.#...#.#.....#.......#.....#...#.#.#w#.........#.#.....#.#.#.#
#.#.#.#.#.#.#.#.#.###.#.#.#########.###.###########.#.#.#.#.#####.#######.#.#.#.#
#.#.#...#.#.#...#.#...#.#...#.....#...#.#...#.......#.#.#.#.#...#.P.#...#.#...#y#
#.#######.#.#.#####.###.###.#.###.#####.#.###.#######.#.###.#.#.###.#.#.#.#.###.#
#.#.....#.#c#.#...#.#l..#...#...#.#.A.#.#.....#.......#...Z.#.#...#.#.#.#...#...#
#.#.###T#.#.###.#.#.#.###.###.#.#.#.#.#.#.#########.#.###########.#.#.#.#####.###
#.#...#.#.#.....#...#...#.H.#.#.#.#.#...#...#.......#.....#.......#...#.....#..u#
#.###.#.#.#############.###.###.#.#.###.###.###.#########.###.###.#########.###.#
#.....#..........e....#.........#...#...#.......#.............#...........#.....#
#################################################################################'''

maze = maze.replace('#', '1')
maze = maze.replace('.', '0')
maze = maze.replace('m', '2')
maze = maze.replace('@', '0')
delete = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for character in maze:

    if character in delete:
        maze = maze.replace(character, '0')

    else:
        pass

for i in maze:

    try:
        int(i)

    except:
        pass
    
rows = maze.split('\n')

#Using list comprehension - split a list having single integer 
rows = [int(x) if x.isdigit() else x for z in rows for x in str(z)]

#subset of list by splitting the orginal list into chunks of 81
rows = [rows[x:x+81] for x in range(0, len(rows), 81)] 
grid = rows

#Solving maze using recursivity 
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

search(40, 40)
