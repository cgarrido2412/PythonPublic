#! /usr/bin/env python3
'''
Author: Charles Garrido.
Creation Date: 4 Aug. 2019.
Last Revision: 15 Jan. 2020.
Description: Takes the daily outage report from Orion and localizes all outages to local time, adds a note column for analysis. 
Saved file must be in the format 'outage_MONTH_DAY_YEAR.xls'.
'''

#imports for code to function
#Use C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\Scripts>pip install MODULE to install module on your machine
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
from datetime import date
import xlrd
import xlwt
import time

#Function only returns True with an integer input
def validate_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

#Program starts
try:
    #Uses date module to grab today's date, and subtract one day for yesterday's outage report. 
    today = date.today() 
    day = int(today.strftime('%d')) - 1
    day = str(day)
    month = today.strftime('%m')
    year = today.strftime('%Y')

    #Compiles expected filename based on date. 
    filename = (month + '_' + day + '_' + year + '.xls')
    print('filename is: outage_' + filename)

    #Defines store open hours and closing hours
    storeOpen = 9
    storeClose = 21

    #Begins timer to determine how long the data analysis takes. 
    startTime = time.time()

    #Adds file pathway to filename
    full_file = 'E:\Savers\Spreadsheets\Outage\\' + year + '\outage_' + filename

    #Asks for user input on what outage is being calculated. 
    mode = input('Is this [monthly],[daily] or [manual]? \n')
    mode = mode.strip()
    mode = mode.lower()
    acceptable_answer = False
    while acceptable_answer is False:
        if mode == 'monthly':
            try:
                data = pd.read_excel(full_file, header=[2], names = ['Store', 'Region', 'Design', 'Vendor', 'Time_Zone', 'Site DOWN',
                                                                     'Site UP', 'Duration'])
                acceptable_answer = True
            except:
                print('Unable to open:', full_file)
        elif mode == 'daily':
            try:
                data = pd.read_excel(full_file, header=[2])
                acceptable_answer = True
            except:
                print('Unable to open:', full_file)
        elif mode == 'manual':
            try:
                day_integer = False
                day = input('Please enter the day[integer]: \n')
                while day_integer is False:
                    try:
                        if validate_integer(day) is True:
                            day_integer = True
                        else:
                            pass
                    except ValueError:
                        print('You need to type an integer.')
                month_integer = False
                month = input("Please enter the month[integer]: \n")
                while month_integer is False:
                    try:
                        if validate_integer(month) is True:
                            month_integer = True
                        else:
                            pass
                    except ValueError:
                        print('You need to type an integer.')
                year_integer = False
                year = input('Please enter the year[integer]: \n')
                while year_integer is False:
                    try:
                        if validate_integer(year) is True:
                            year_integer = True
                        else:
                            pass
                    except ValueError:
                        print('You need to type an integer.')
                filename = (month + '_' + day + '_' + year + '.xls')
                full_file = 'E:\Savers\Spreadsheets\Outage\\' + year + '\outage_' + filename
                data = pd.read_excel(full_file, header=[2])
                acceptable_answer = True
            except:
                print('Unable to open:', full_file)
        else:
            print('Invalid input.')
            break

    #Drop any outage durations =< 1, also remove anything from 2955-FW-1 and TDX-ESX-VPN.     
    data = data.drop(data[data.Duration == 0].index) 
    data = data.drop(data[data.Duration == 1].index)
    data = data.drop(data[data.Store == '2955-FW-1'].index)
    data = data.drop(data[data.Store == 'TDX-ESX-VPN'].index)

    #Change Site DOWN and Site UP to datetime objects. 
    data['Site DOWN'] = pd.to_datetime(data['Site DOWN']) 
    data['Site UP'] = pd.to_datetime(data['Site UP'])

    #Define conversion function
    def conversion_function(x: pd.Series) -> pd.Timestamp:
        zones = {'Atlantic': 'Canada/Atlantic',
                 'Central': 'US/Central',
                 'Eastern': "US/Eastern",
                 'Mountain': 'US/Mountain',
                 'Pacific': 'US/Pacific',
                 'Australia': 'Australia/Melbourne',
                 'Arizona': 'US/Arizona',
                 'Alaska': 'US/Alaska',
                 'Hawaii' : 'US/Hawaii'}
        raw_time = pd.Timestamp(x[1])
        loc_raw_time = raw_time.tz_localize("US/Pacific")
        return loc_raw_time.tz_convert(zones[x[0]]).replace(tzinfo=None)

    #Using fucntion to apply conversion function and insert During Hours and Notes columns. Also saves excel file. 
    def apply(data):
        data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
        data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
        data.insert(5, 'During_Hours', value='')
        data.insert(9, 'Notes', value='')
        data.to_excel(full_file)
    apply(data)

    #Drops any duplicate Adjusted_Up times and saves file again. 
    data = data.drop_duplicates('Adjusted_Up')
    data.to_excel(full_file)

    #Ends timer for data analysis.
    endTime = time.time()
    print('The conversion function took %s seconds to calculate.' % (endTime - startTime))

    #Starts second part of program, an outage minute calculator. 
    program_running = True
    while program_running is True:

        #Exception handling allows for a ctrl+c exit (see last lines of code)
        print('Outage calculator\nHit [ctrl+c] to quit.\n')
        storeOpen = 9
        storeClose = 21
        outage_start = input('Enter outage start time:\n')
        if outage_start == '':
            program_running = False
        else:
            pass
        outage_end = input('Enter outage end time:\n')
        if outage_end == '':
            program_running = False
        else:
            pass
        string1 = '2019-08-11 ' + outage_start
        string2 = '2019-08-11 ' + outage_end
        def breakdown(x,y):
            #For downtime, time format 'YEAR-MONTH-DAY HOUR:MINUTE:SECOND'
            string1 = x.split() 
            variable2 = string1[1] 
            dateVariable2 = variable2.split(':') 
            hour = int(dateVariable2[0]) 
            minute = int(dateVariable2[1]) 
            seconds = int(dateVariable2[2])

            #For uptime
            string1B = y.split()
            variable2B = string1B[1]
            dateVariable2B = variable2B.split(':')
            hourB = int(dateVariable2B[0])
            minuteB = int(dateVariable2B[1])
            secondsB = int(dateVariable2B[2])
            if hour or hourB in range(storeOpen, storeClose):
                if hourB not in range(storeOpen, storeClose):
                    if hourB > 21:
                        hourB = 21
                        minuteB = 0
                        secondsB = 0
                    else:
                        pass
                if hour not in range(storeOpen, storeClose):
                    if hour < 9:
                        hour = 9
                        minute = 0
                        seconds = 0
                    else:
                        pass
                if hourB > hour:
                    sumMinutes = (hourB - hour)*60
                    sumMinutes = sumMinutes + (minuteB - minute)
                    if sumMinutes < 0:
                        sumMinutes = 0
                    else:
                        pass
                    print(sumMinutes)
                elif hourB == hour:
                    sumMinutes = minuteB - minute
                    if sumMinutes < 0:
                        sumMinutes = 0
                    print(sumMinutes)
            else:
                print(0)
        print(breakdown(string1,string2))

#Exception handling for ctrl+c exit. 
except KeyboardInterrupt:
    print('Program terminated by user.')
