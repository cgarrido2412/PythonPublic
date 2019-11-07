import re
file = input('Enter file path: \n')

try:
    open_file = open(file)
    ask = input('Enter a word to search: \n')
    query = ('(' + ask + ')')
    query = query.strip()
    
    for line in open_file:
        the_sentences = line.split('.')
        
    for item in the_sentences:
        result = re.split(query,item)
        print(result)
        
except:
    print('File cannot be opened:', open_file)
    exit()
