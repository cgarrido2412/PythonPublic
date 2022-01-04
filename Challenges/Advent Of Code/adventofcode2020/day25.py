#! /usr/bin/env python3

import os 

def determine_loop(subject_number, public_key):
    for x in range(modulo):
        if pow(subject_number, x, modulo) == public_key:
            return x

if __name__ == "__main__":
    public_keys = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read().split('\n')
    card_public_key = int(public_keys[0])
    door_public_key = int(public_keys[1])
    modulo = 20201227
    card_loop_size = determine_loop(7, card_public_key)
    encryption_key = pow(door_public_key, card_loop_size, modulo)
    print(encryption_key)
