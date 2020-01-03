#!Python3
import wikipedia

try:
    program_running = True

    while program_running is True:
        query = input('\nEnter something to lookup(Or press enter to exit):\n')
        if query == "":
            program_running = False
        else:
            search = wikipedia.page(query)
            print(search.summary)
        
except KeyboardInterrupt:
    print('\nProgram terminated.\n')
