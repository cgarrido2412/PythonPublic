import time, os, sys
import case_sensitive_caesar

def caesar_encrypt():  
    message = str(input('Please enter the message to be encrypted: \n')) #when running asks for this argument!!!
    text = ''
    key = int(input('Please enter a number key: \n'))
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

def main():
    inputFilename = 'test.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    outputFilename = 'test_encrypted.txt'
    myKey = int(input('Please enter a number key: \n'))
    myMode = str(input("set to 'encrypt' or 'decrypt'")) # set to 'encrypt' or 'decrypt'
    myMode = myMode.strip()

    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes.
    startTime = time.time()
    if myMode == 'encrypt':
        translated = case_sensitive_caesar.caesar_encrypt()
    elif myMode == 'decrypt':
        translated = case_sensitive_caesar.caesar_decrypt(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
