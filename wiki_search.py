import wikipedia

try:
    program_running = True

    while program_running is True:
        query = input('\nEnter something to lookup:\n')
        search = wikipedia.page(query)
        print(search.summary)
        
except KeyboardInterrupt:
    print('\nProgram terminated.\n')
