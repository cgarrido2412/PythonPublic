#! /usr/bin/env python3
'''
[Santa's] elves are running low on wrapping paper, and so they need to submit an order for more. They have a list
of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as
they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of
slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot
of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the
length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any
one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect
bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of
ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of
ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
'''

class Gift:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def wrapper(self):
        dimensions = [(self.length * self.width),
                      (self.width * self.height),
                      (self.height * self.length)]
        minimum = min(dimensions)
        area = ((2 * self.length * self.width) +
                (2 * self.width * self.height) +
                (2 * self.height * self.length) + minimum)
        return area
    def smallest_side(self):
        side_one = (self.length*2) + (self.width*2)
        side_two = (self.length*2) + (self.height*2)
        side_three = (self.width*2) + (self.height*2)
        side_list = [side_one, side_two, side_three]
        smallest_side = min(side_list)
        return smallest_side
    def ribbon(self):
        perimeter = self.smallest_side()
        volume = self.length * self.width * self.height
        total_ribbon = perimeter + volume
        return total_ribbon

def file_test(file):
    try:
        open(file)
    except FileNotFoundError:
        print('Unable to open:', file)
        exit()

if __name__ == '__main__':
    file_test(r'C:\Users\cgarrido\Desktop\lab.txt')
    file = open(r'C:\Users\cgarrido\Desktop\lab.txt').read()
    lines = file.split('\n')
    numbers = []
    for x in range(len(lines)):
        extracted_numbers = lines[x].split('x')
        numbers.append(extracted_numbers)

    integers = []
    for x in range(len(numbers)):
        extracted_integers = [int(y) for y in numbers[x]]
        integers.append(extracted_integers)

    list_of_square_feet = []
    total_ribbon = []
    for x in range(len(integers)):
        present = Gift(integers[x][0], integers[x][1], integers[x][2])
        area = present.wrapper()
        ribbon_amount = present.ribbon()
        list_of_square_feet.append(area)
        total_ribbon.append(ribbon_amount)

    total_square_feet = sum(list_of_square_feet)
    total_length_of_ribbon = sum(total_ribbon)
    print(total_square_feet)
    print(total_length_of_ribbon)
