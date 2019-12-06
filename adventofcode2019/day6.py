#!Python3
file = input('Enter file path and file name: \n')

def file_test(file):

    try:
        open(file)

    except:
        print('Unable to open', file)

file_test(file)

obj = {}
with open(file) as working_file:
    
    for ix, line in enumerate(working_file):
        data = [str(x.strip()) for x in line.split(')')]
        a = data[0]
        b = data[1]
        
        if a in obj:
            obj[a].append(b)
            
        else:
            obj[a] = [b]

    num = 0
    q = ['COM']
    count = 0
    
    while q:
        l = len(q)
        
        for i in range(l):
            count += num
            
            if q[i] in obj:
                
                for j in obj[q[i]]:
                    q.append(j)

        for i in range(l):
            q.pop(0)

        num += 1
        
    print(count)
    
working_file.close()
