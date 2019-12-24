#!Python3
'''
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the
password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or
135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 272091-815432.
'''

start = 272091
stop = 815432
matches = []

for number in range(start, stop + 1):
    increasing_check = True
    double_character_check = False
    previous_character = ''

    for digit in str(number):
        
        if digit < previous_character:
            increasing_check = False
            break
        
        elif digit == previous_character:
            double_character_check = True

        previous_character = digit
        
    if increasing_check and double_character_check:
        matches.append(number)
        
print(len(matches))
