#!/usr/bin/env python3

import random 

def re_key():
    for x in range(1,6):
        bottom_pin = random.randint(1,9)
        output = 'bottom key pin {} is {}'.format(x,bottom_pin)
        print(output) 

if __name__ == "__main__":
    running = True
    while running:
        try:
            new_lock = input('Create new lock?\n[y/n]\n')
            new_lock = new_lock.lower().strip()
            if new_lock == 'y':
                re_key()
            else:
                exit() 
        except KeyboardInterrupt:
            print('Goodbye.')
            exit()
        except Exception as e:
            print(e)