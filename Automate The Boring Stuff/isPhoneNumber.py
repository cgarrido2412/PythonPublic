def isPhoneNumber(text):

    if len(text) != 12:
        return False #phone number is not long enough
        
    for i in range(0,3):
    
        if not text[1].isdecimal():
            return False #missing area code
            
        if text[3] != '-':
            return False #missing dash 
            
    for i in range(4,7):
    
        if not text[i].isdecimal():
            return False #no first three digits
            
    if text[7] != '-':
        return False
        
    for i in range(8,12):
    
        if not text[i].isdecimal():
            return False #missing last four digits
            
    return True
    
while True:
    test = input('Enter a phone number to validate (or type "done" to quit): \n')
    
    if test == 'done':
        break
    
    else:
        print(isPhoneNumber(test))
