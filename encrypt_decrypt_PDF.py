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
