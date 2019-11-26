#Loop through the lines of a file to read the whole file, line by line
file = input('Enter a file path: \n')

try:
    fhand = open(file)
    
except:
    print('Unable to open file.')
    
for x in fhand:
    print(x)
