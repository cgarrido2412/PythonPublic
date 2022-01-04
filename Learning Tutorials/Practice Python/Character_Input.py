#Create a program that asks the user to enter their name and their age
#Print out a message addressed to them that tells them the year that they will turn 100 years old
name = str(input('Welcome! What is your name?'))
age = int(input('How old are you?'))
year = 2019 + (100 - age)
print('Okay', name, '. You will turn one hundred years old in the year', year)
