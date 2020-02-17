#! /usr/bin/env python3
'''
Author: Charles Garrido.
Creation Date: 4 Aug. 2019.
Last Revision: 10 Feb. 2020.
Description: Takes the daily outage report from Orion and localizes all outages to local time, adds a note column for analysis. 
Saved file must be in the format 'outage_MONTH_DAY_YEAR.xls'.
'''

#Imports for the code to function.
#To install modules that are not native to python, navigate to C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\Scripts>
#Then, use C:\Users\cgarrido\AppData\Local\Programs\Python\Python37\Scripts>pip install MODULE
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
from datetime import date
import xlrd
import xlwt
import time
import subprocess

#Following function applies conversion_function and adds 'During_Hours' and 'Notes' columns. Then saves the file.
def apply(data):
    data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
    data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
    data.insert(5, 'During_Hours', value='')
    data.insert(9, 'Notes', value='')
    data.to_excel(full_file)

#Following function breaksdown the time formatted string for outage duration calculations
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

#Conversion function localizes outage time to PST and converts them to their local timezone
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

#Function tests if a file can be opened. 
def file_test(file):
    try:
        open(file)
    except FileNotFoundError:
        print('Unable to open:', file)
        exit()

#Validates if input / variable can be converted to integer format
def validate_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

#Driving code that runs if program is being run directly
if __name__ == '__main__':

    #Try following code, built in exception KeyboardInterrupt handling
    try:

        #Grab today's date, then assemble the expected file name and define the store hours
        today = date.today() 
        day = int(today.strftime('%d')) - 1
        day = str(day)
        month = today.strftime('%m')
        year = today.strftime('%Y')
        filename = (month + '_' + day + '_' + year + '.xls')
        print('filename is: outage_' + filename)
        storeOpen = 9
        storeClose = 21

        #Start timer for script, define mode of the script
        #Note that the default filepath is pointed towards my E:\ drive
        startTime = time.time()
        full_file = 'E:\Savers\Spreadsheets\Outage\\' + year + '\outage_' + filename
        mode = input('Is this [daily], or [manual]? \nType [filepath] if Charles is not running this script.\n')
        mode = mode.strip()
        mode = mode.lower()

        #Depending if the script is run daily or as a manual task, exectute the following
        if mode == 'daily':
            file_test(full_file)
            data = pd.read_excel(full_file, header=[2])
        elif mode == 'manual':
            manual_day = str(input('Please enter the day[integer]: \n'))
            manual_month = str(input("Please enter the month[integer]: \n"))
            manual_year = str(input('Please enter the year[integer]: \n'))
            if validate_integer(manual_day) and validate_integer(manual_month) and validate_integer(manual_year) is True:
                new_file = (manual_month + '_' + manual_day + '_' + manual_year + '.xls')
                full_file = 'E:\Savers\Spreadsheets\Outage\\' + manual_year + '\outage_' + new_file
                file_test(full_file)
                data = pd.read_excel(full_file, header=[2])
            else:
                exit()
        elif mode == 'filepath':
            full_file = input('Enter full file path:\n')
            file_test(full_file)
            data = pd.read_excel(full_file, header=[2])
        else:
            print('Invalid input.')
            exit()

        #Start by removing outages < 1min. Even though Duration == 1, the way pandas interprets the line becomes < 1
        data = data.drop(data[data.Duration == 0].index)
        data = data.drop(data[data.Duration == 1].index)

        #Remove the following lab environment and TDX VPN, these should not be included in the retail outage report
        data = data.drop(data[data.Store == '2955-FW-1'].index)
        data = data.drop(data[data.Store == 'TDX-ESX-VPN'].index)
        data['Site DOWN'] = pd.to_datetime(data['Site DOWN']) 
        data['Site UP'] = pd.to_datetime(data['Site UP'])
        apply(data)

        #Drop duplicate adjusted_up times and save file. End timer
        data = data.drop_duplicates('Adjusted_Up')
        data.to_excel(full_file)
        endTime = time.time()
        print('The conversion function took %s seconds to calculate.' % (endTime - startTime))

        #Use subprocess to open saved file
        subprocess.call([r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE", full_file])

        #After the file is closed, the rest of the script runs to start an outage calculator on the terminal
        program_running = True
        while program_running is True:
            print('Outage calculator\nHit [ctrl+c] to quit.\n')
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
            string1 = year + '-' + month + '-' + day + ' ' + outage_start
            string2 = year + '-' + month + '-' + day + ' ' + outage_end
            print(breakdown(string1,string2))

    #Exception handling for keyboardInterrupt
    except KeyboardInterrupt:
        print('Program terminated by user.')
