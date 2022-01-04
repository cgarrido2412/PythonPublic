#! /usr/bin/env python3
'''
Author: Charles Garrido
Date: 5 March 2020

Description: Grabs all URL links from a webpage. 
'''

import requests
import re

def main():
    url = input('\nGrab all links from a webpage.\nEnter a URL (include http://):\n')
    website = requests.get(url)
    html = website.text
    links = re.findall('"((http|ftp)s?://.*?)"', html)
    for link in links:
        print(link[0])

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('Program terminated.')
        exit()
