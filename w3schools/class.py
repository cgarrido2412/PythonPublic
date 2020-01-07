#!Python3

class Rectangle:

    def __init__(self, length, width, unit_cost=0):
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

valid_length = False
length = input('Enter rectangle length [integer]: \n')

while valid_length is False:

    try:

        if integer_check(length) is True:
            valid_length = True

        else:
            pass

    except ValueError:
        print('You must have an integer for input.')

valid_width = False
width = input('Enter rectangle width [integer]: \n')

while valid_width is False:

    if integer_check(width) is True:
        valid_width = True

    else:
        pass

length = int(length)
width = int(width)
r = Rectangle(length, width)
print('Area of Rectangle: %s cm^2' % (r.get_area()))
print('Perimeter of Rectangle: %s cm' % (r.get_perimeter()))
