import random
import camelcase
def reverse(): 
    message = str(input('Please enter message to reverse:'))
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    print(translated) 
def generate():
    length = int(input('Please enter a password length:'))
    characters = 'abcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*()'
    password = ''.join(random.sample(characters, length))
    return password
def odd_even():
    number = int(input('Enter a number to check:'))
    if number % 2 == 0:
        print(number, 'is an even number.')
    else:
        print(number, 'is an odd number.')
def upper_case():
    message = str(input('Enter a message:'))
    message = message.upper()
    return message
def lower_case():
    message = str(input('Enter a message:'))
    message = message.lower()
    return message 
def camelcase(): #is not working 
    message = str(input('Enter a message:'))
    message = message.camelcase()
    return message
