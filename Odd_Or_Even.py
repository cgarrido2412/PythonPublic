#Ask the user for a number
#Depending on whether the number is even or odd, print out an appropriate message to the user
number = int(input('Please enter a number: '))
if number % 2 == 0:
    print(number, 'is an even number.')
else:
    print(number, 'is an odd number.')
