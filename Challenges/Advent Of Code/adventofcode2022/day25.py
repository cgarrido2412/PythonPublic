#!/usr/bin/env python3

'''
    #print(snafu[0]) #1=21
    #print(snafu[0][::-1]) #12=1

    #print(dec_to_base(decimal_total, 5)) #13243241311032143100 the len == 20
    #With the given length above, 5 ** 19 should be the largest exponent needed to convert this total to snafu format 
'''

import os 

def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num

def int_to_snafu(n):
    #String to digit
    s2d = {
        "0": 0,
        "1": 1,
        "2": 2,
        "-": -1,
        "=": -2
    }

    d2s = {d: s for s, d in s2d.items()}

    res = ""
    while n > 0:
        d = ((n + 2) % 5) - 2
        res += d2s[d]
        n -= d
        n //= 5
    return res[::-1]

if __name__ == "__main__":

    with open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day25_input.txt') as file:
        fuel_list = file.read()

    snafu = fuel_list.split('\n')

    decimal_total = 0

    for x in range(len(snafu)):

        #First reverse the string
        backwards = snafu[x][::-1]

        total = 0
        for i in range(len(backwards)):
            if i == 0:
                if backwards[i] == '1':
                    total += 1
                elif backwards[i] == '2':
                    total += 2
                elif backwards[i] == '=':
                    total -= 2
                elif backwards[i] == '-':
                    total -= 1
                elif backwards[i] == '0':
                    total += 0
            else:
                if backwards[i] == '1':
                    total += 5 ** i
                elif backwards[i] == '2':
                    total += (5 ** i) * 2
                elif backwards[i] == '=':
                    total += (5 ** i) * -2
                elif backwards[i] == '-':
                    total += (5 ** i) * -1
                elif backwards[i] == '0':
                    total += 0

        #Check decimal conversion of each line
        print('Line number', x+1, 'is:', total)
        decimal_total += total

    print('The final fuel total in decimal is:', decimal_total)

    #Convert decimal total to snafu format
    print('The snafu total is', int_to_snafu(decimal_total)) #Part one correct and complete
