#!/usr/bin/env python3

'''
Provides the doomsday index day for a given year 
where year is between the 17th and 25th centuries
'''

import random

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

if __name__ == "__main__":
    #Establish random year 
    year = str(random.randint(1600,2500))

    #Establish Random Month
    month = [
        'January',
        'February',
        'March',
        'April', 
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    month_choice = random.sample(month, 1)

    #Establish day
    months_31 = [
        'January',
        'March',
        'May',
        'July',
        'August',
        'October',
        'December'
    ]
    months_30 = [
        'April',
        'June',
        'september',
        'November'
    ]

    #Establish specific year
    year = input('Enter year:\n')

    #Establish known century mapping
    known_centuries = {
        '1600' : 'Tuesday',
        '1700' : 'Sunday',
        '1800' : 'Friday',
        '1900' : 'Wednesday',
        '2000' : 'Tuesday',
        '2100' : 'Sunday',
        '2200' : 'Friday',
        '2300' : 'Wednesday',
        '2400' : 'Tuesday'
    }

    #Establish day mapping
    days = {
        'Sunday' : 0,
        'Monday' : 1,
        'Tuesday' : 2,
        'Wednesday' : 3,
        'Thursday' : 4,
        'Friday' : 5,
        'Saturday' : 6
    }

    #Separate year (i.e., 2021) into century '20' and generation '21'
    century = year[0:2] + '00'
    generation = int(year[2:4])

    #Doomsday calculations
    calc_div = int(generation/12)
    calc_sub = generation - calc_div * 12
    calc_leap = int(calc_sub/4)

    #Index by year
    reference_day = known_centuries.get(century)
    reference_number = days.get(reference_day)

    #Final calculation
    key_day = (reference_number + calc_div + calc_sub + calc_leap) % 7
    print(year)
    print(get_key(days, key_day))