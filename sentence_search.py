file = input('Enter file path:')

try:
    open_file = open(file)
    
    while True:    
        open_file = open(file)
        counted = dict()
        
        for line in open_file:
            the_sentences = line.split('.')
            the_words = line.split()
            
            for word in the_words:
                
                if word not in counted:
                    counted[word] = 1
                
                else:
                    counted[word] += 1
                    
        print(counted)
        ask = input('Enter a word to search or type "done" to quit: \n')
        
        if ask == 'done':
            break
            
        else:
            print('Searching...')
            print(counted.get(ask))
            
except:
    print('File cannot be opened:', open_file)
    exit()
