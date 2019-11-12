#given two .txt files that have lists of numbers in them,
#find the numbers that are overlapping
#one text file has all prime numbers under 1,000
#the other has happy numbers (real mathematical concept) up to 1,000

prime_list = []
with open('prime_numbers.txt') as prime_file:
    line = prime_file.readline()
    while line:
        prime_list.append(int(line))
        line = prime_file.readline()

happy_list = []
with open('happy_numbers.txt') as happy_file:
    line = happy_file.readline()
    while line:
        happy_list.append(int(line))
        line = happy_file.readline()

overlap_list = []
for elem in prime_list:
    if elem in happy_list:
        overlap_list.append(elem)

print(overlap_list) 
