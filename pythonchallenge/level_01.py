#http://www.pythonchallenge.com/pc/def/274877906944.html
string1 = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj.'''

def caesar_decrypt(message):
    #message = input('Please enter the message to be decrypted: \n')
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

caesar_decrypt(string1)
caesar_decrypt_result = '''
Key # 24: i hope you didnt translate it by hand.
thats what computers are for. doing it in by hand is inefficient and that's why this text is so long.
using string.maketrans() is recommended. now apply on the url.'''

#solution = string1.maketrans(x[, y[, z]])
'''
x - If only one argument is supplied, it must be a dictionary.
The dictionary should contain 1-to-1 mapping from a single character string to its translation OR
a unicode number (97 for 'a') to its translation.
'''

'''
y - If two arguments are passed, it must be two strings with equal length.
Each character in the first string is a replacement to its corresponding index in the second string.
'''

'''
z - If three arguments are passed, each character in the third argument is mapped to None.
'''

url = 'http://www.pythonchallenge.com/pc/def/map.html'
caesar_decrypt(url)
solution = 'http://www.pythonchallenge.com/pc/def/ocr.html'
