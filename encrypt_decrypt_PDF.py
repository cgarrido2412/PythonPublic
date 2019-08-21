import PyPDF2
import random

def generate():
    length = int(input('Please enter a password length:'))
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
    password = ''.join(random.sample(characters, length))
    print(password)
def encrypt():
    pdfFile = open('ExamplePDF.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range (pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt('REDACTED')
    resultPdf = open('encrypted_passwords_file.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
def decrypt():
    pdfReader = PyPDF2.PdfFileReader(open('encrypted_passwords_file.pdf', 'rb'))
    pdfReader.isEncrypted
    pdfReader.decrypt('REDACTED')
    pageObj = pdfReader.getPage(0)
    return pageObj.extractText()
def extract():
    pdfFileObj = open('ExamplePDF.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    pageObj.extractText()
    return pageObj.extractText()
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
