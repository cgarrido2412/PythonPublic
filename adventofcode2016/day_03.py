#! /usr/bin/env python3
'''
Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up
this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications
for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle"
given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
'''
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

puzzle = open(r'C:\Users\cgarrido\Desktop\lab.txt').read()
lines = puzzle.split('\n')

rows = []
for i in range(len(lines)):
    number_line = lines[i].split(' ')
    rows.append(number_line)

next_list = []
for i in range(len(rows)):
    for x in rows[i]:
        if x == '':
            pass
        else:
            next_list.append(x)

integer_list = [int(x) for x in next_list]

final_list = []
for group in chunker(integer_list, 3):
    final_list.append(group)

triangle_count = 0
for x in range(len(final_list)):
    results = []
    results.append(final_list[x][0] + final_list[x][1] > final_list[x][2])
    results.append(final_list[x][2] + final_list[x][1] > final_list[x][0])
    results.append(final_list[x][2] + final_list[x][0] > final_list[x][1])
    if sum(results) == 3:
        triangle_count += 1
    else:
        pass
print(triangle_count)
