def reverse_a_string():
    text = str(input('Enter a message to reverse: \n'))
    text2 = ''
    i = len(text) - 1
    
    while i >= 0:
        text2 = text2 + text[i]
        i -= 1
        
    print(text2)
    
def reverse_a_string2():
    x = str(input('Enter a message to reverse: \n'))
    return x[::-1]
    
