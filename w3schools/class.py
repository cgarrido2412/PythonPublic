#!Python3

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

def integer_check(x):

    try:
        int(x)
        return True

    except ValueError:
        return False

length = input('Enter rectangle length [integer]: \n')    
width = input('Enter rectangle width [integer]: \n')

if integer_check(length) and integer_check(width) is True:
    length = int(length)
    width = int(width)
    r = Rectangle(length, width)
    print('Area of Rectangle: %s in^2' % (r.get_area()))
    print('Perimeter of Rectangle: %s in' % (r.get_perimeter()))

else:
    print('Invalid input parameters, only integers will work.')
