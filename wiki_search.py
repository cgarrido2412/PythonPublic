#!Python3
import wikipedia

try:
    program_running = True

    while program_running is True:
        query = input('\nEnter something to lookup, type "?" for a random suggestion or press [enter] to exit:\n')

        if query == "":
            program_running = False

        elif query == '?':
            print(wikipedia.random(pages=1))

        else:
            search = wikipedia.page(query)
            mode = input('\n[summary] full[article] or [references]?\n')
            mode = mode.strip()
            mode = mode.lower()

            if mode == 'summary':
                print(search.summary)

            elif mode == 'article':
                print(search.content)

            elif mode == 'references':
                print(search.references)

            else:
                print('Invalid selection.')

except KeyboardInterrupt:
    print('\nProgram terminated.\n')
