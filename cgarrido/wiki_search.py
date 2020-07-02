# /usr/bin/env python3
'''
Author: Charles Garrido
Last Modified: 2 July 2020
'''

import wikipedia

def main():
    while True:
        try:
            query = input('Search:\n')
            try:
                search = wikipedia.page(query)
                print(search.summary)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e)
        except KeyboardInterrupt:
            print('Program terminated.')
        
if __name__ == '__main__':        
    main()
