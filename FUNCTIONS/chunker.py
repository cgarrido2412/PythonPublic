#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list = list(chunker(l, 3))
    print(my_list) #Will print: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
