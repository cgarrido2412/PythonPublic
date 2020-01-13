#!Python3

def start():
    import wikipedia

    try:
        program_running = True

        while program_running is True:
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
        
start()

