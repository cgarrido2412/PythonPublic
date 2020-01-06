#!Python3

def start():
    import wikipedia

    try:
        program_running = True

        while program_running is True:
            query = input('\nEnter something to lookup, type [?] for a random article summary or press [enter] to exit:\n')

            if query == "":
                program_running = False

            elif query == '?':
                result = (wikipedia.random(pages=1))
                result = wikipedia.page(result)
                print(result.summary)

            else:
                search = wikipedia.page(query)
                print(search.summary)

    except KeyboardInterrupt:
        print('\nProgram terminated.\n')

start()
