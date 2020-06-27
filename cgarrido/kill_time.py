#! /usr/bin/env python3

'''
Author: Charles Garrido
Last modified: 26 June 2020

This script will run until a specific designated time.
Additional future functionality may include automated cursor movement to keep
machine from idling. 
'''

from datetime import datetime

def main():
        time = str(input('Enter script end time:\n')).strip()
        time = time.split(':')
        hour = str(time[0]).strip()
        minute = str(time[1]).strip()
        while True:
                current_time = str(datetime.now()) 
                current_time = current_time.split(' ')
                current_time[1] = current_time[1].split(':') 
                if current_time[1][0] == hour:
                        if current_time[1][1] == minute:
                                exit()
                        else:
                                pass
                else:
                        pass

if __name__ == '__main__':
        try:
                main()
        except KeyboardInterrupt:
                print('Program terminated.')
        except IndexError:
                print('Invalid input, please enter time in format XX:XX')
