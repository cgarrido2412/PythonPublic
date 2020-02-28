#! /usr/bin/env Python3

def validate_integer(x):

    try:
        int(x)
        return True

    except ValueError:
        return False

def caesar_encrypt():  
    message = str(input('Please enter the message to be encrypted: \n'))
    text = ''
    integer_check = False

    while integer_check is False:

        try:
            key = int(input('Please enter a number key: \n'))

            if validate_integer(key) is True:
                integer_check = True

            else:
                pass

        except ValueError:
            print('You need to type an integer.')
    L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'

    for symbol in message:

        if symbol in L:
            n = L.find(symbol)
            n = n + key

            if n >= len(L):
                n = n - len(L)

            elif n < 0:
                n = n + len(L)
            text = text + L[n]

        elif symbol in l:
            n = l.find(symbol)
            n = n + key

            if n >= len(l):
                n = n - len(l)

            elif n < 0:
                n = n + len(l)
            text = text + l[n]

        else:
            text = text + symbol
    print('Your encrypted message is: \n' + text)

def caesar_decrypt():
    message = input('Please enter the message to be decrypted: \n')
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(LETTERS)):
        translated = ''

        for symbol in message:

            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]

            elif symbol in letters:
                num = letters.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]

            else:
                translated = translated + symbol
        print('Key # %s: %s' % (key, translated))

try:
    mode = str(input('What would you like to do?\n[encrypt][decrypt]\n'))
    mode = mode.strip()
    mode = mode.lower()
    completed = False

    while completed is False:

        if mode == 'encrypt':
            caesar_encrypt()
            check = input('Encrypt another message?[y/n]')

            if check == 'y':
                pass

            else:
                print('Exiting...')
                completed = True

        elif mode == 'decrypt':
            caesar_decrypt()
            check = input('Decrypt another message?[y/n]')

            if check == 'y':
                pass

            else:
                print('Exiting...')
                completed = True

        else:
            print('Invalid selection, only choose between [encrypt][decrypt]\nProgram stopping...')
            break

except KeyboardInterrupt:
    print('Program terminated by user.\nExiting...')
    
