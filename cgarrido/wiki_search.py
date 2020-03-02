# /usr/bin/env python3
'''
Author: Charles Garrido
'''

import wikipedia

def main():
    try:
        program_running = True
        while program_running:
            query = input('''
Type [?] for a random article summary.
Include [article] at the end of your search to print the full article.
Enter something to lookup:\n''')
            if query == "":
                program_running = False
            elif query == '?':
                result = (wikipedia.random(pages=1))
                result = wikipedia.page(result)
                print(result.summary)
            elif '[article]' in query:
                search = wikipedia.page(query)
                print(search.content)
            else:
                search = wikipedia.page(query)
                print(search.summary)
    except KeyboardInterrupt:
        print('\nProgram terminated.\n')
        
if __name__ == '__main__':        
    main()
