def caesar_encrypt():  
    message = str(input('Please enter the message to be encrypted: \n'))
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
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Key # %s: %s' % (key, translated))

