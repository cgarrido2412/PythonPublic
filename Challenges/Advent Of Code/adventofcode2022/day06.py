#!/usr/bin/env python3

import os

def signal_lock(packet_size):
    for (x, character) in enumerate(data):
        if len(set(data[x:(x+packet_size)])) == packet_size:
            return x + packet_size 

if __name__ == "__main__":
    
    data = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day06_input.txt').read()

    print('Part one:', signal_lock(4)) #Part one correct and comlete 
    print('Part two:', signal_lock(14)) #Part two correct and complete
