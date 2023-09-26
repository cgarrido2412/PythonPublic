#!/usr/bin/env python3

'''
s = "8-Mar-2017, 23:42:42.314"

d = datetime.strptime(s, '%d-%b-%Y, %H:%M:%S.%f')

test = '07-19 15:56'
d = datetime.strptime(test, '%m-%d %H:%M')
'''

from datetime import datetime 
from humanfriendly import format_timespan
import pandas as pd 

def time_between(d1, d2):
    d1 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    diff = abs((d2 - d1).seconds)
    return diff 

if __name__ == "__main__":
    d1 = '2023-09-19 04:33:27'
    d2 = '2023-09-20 02:23:47'

    #print(format_timespan(time_between(d1, d2))) #21 hours, 50 minutes and 20 seconds

    df = pd.read_csv('sc_task.csv')
    #print(df)

    resolution_times = []
    for x in range(len(df['opened_at'])):
        resolution_time = time_between(df['opened_at'][x], df['closed_at'][x])
        resolution_times.append(resolution_time)

    #print(resolution_times) #[62306, 82198, 77399, 64896, 27321, 83926, 78620]

    avg_resolve = sum(resolution_times) / len(resolution_times)

    print(format_timespan(avg_resolve))