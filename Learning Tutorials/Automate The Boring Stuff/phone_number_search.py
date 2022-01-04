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
    
voice_mail = 'Hey this is store 1080 please give us a call back at 425-123-1234 today or 425-321-4321 tomorrow!'
foundNumber = False

for i in range(len(voice_mail)):
    chunk = voice_mail[i:i+12]
    
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
        
if not foundNumber:
    print('Could not find any phone numbers.')
