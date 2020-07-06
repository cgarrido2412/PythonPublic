#! /usr/bin/env python3

'''
Author: Charles Garrido
Last Modified: 6 July 2020
'''

def wiki():
    while True:
        try:
            query = input('Search:\n')
            try:
                search = wikipedia.page(query)
                print(search.summary)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e)
            except wikipedia.exceptions.PageError as e:
                print(e)
        except KeyboardInterrupt:
            print('Program terminated.')
            exit()

if __name__ == "__main__":
    wiki()
