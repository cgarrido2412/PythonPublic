#Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters a-z.
#Your program should not count spaces, digits, punctuation, or anything other than letters a-z.

import string

count = 0
my_dict = {}
my_list = []
file_name = input('Enter file name: \n')

try:
    file_handle = open(file_name)

    for line in file_handle:
        #useage of line.translate():
        #Python string method translate() returns a copy of the string in which
        #all characters have been translated using table
        #(constructed with the maketrans() function in the string module),
        #optionally deleting all characters found in the string deletechars.

        #useage of str.maketrans:
        #Return a translation table suitable for passing to translate(),
        #that will map each character in from into the character at the same position in to;
        #from and to must have the same length
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()

        #Now that all digits and punctuation have been removed, continue:
        words = line.split()

        for word in words:

            for letter in word:
                count += 1

                if letter not in my_dict:
                    my_dict[letter] = 1

                else:
                    my_dict[letter] += 1

    for key, val in list(my_dict.items()):
        my_list.append((val / count, key))

    my_list.sort(reverse=True)

    for key, val in my_list:
        print(key, val)

except:
    print('File cannot be opened: \n' + file_name)
    exit()
