#!/usr/bin/env python3

import os 


if __name__ == "__main__":
    depth_measurements = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    measurements = depth_measurements.split('\n')
    measurements = [int(x) for x in measurements]
    increased = 0

    for x in range(len(measurements)):
        if x == 0:
            pass
        else:
            if measurements[x-1] < measurements[x]:
                increased += 1
            else:
                pass 

    print(increased)
