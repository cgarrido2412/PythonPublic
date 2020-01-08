#!Python3

import re
store_number = '2100'

def split_store_number (store_number):
    first_number = re.findall('^(\d{1})', store_number)
    second_number = re.findall('^\d(\d)', store_number)
    third_number = re.findall('^\d\d(\d)', store_number)
    fourth_number = re.findall('^\d\d\d(\d)', store_number)
    print(first_number, second_number, third_number, fourth_number)
    
split_store_number(store_number)

