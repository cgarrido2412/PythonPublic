#! Python 3
'''
Author: Charles Garrido.
Creation Date: 4 Aug. 2019.
Last Revision: 5 Dec. 2019.
Description: Takes the daily outage report from Orion and localizes all outages to local time, adds a note column for analysis. 
Saved file must be in the format 'outage_MONTH_DAY_YEAR.xls'.
'''
    
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
from datetime import date
import xlrd
import xlwt
import time

try:
    today = date.today()
    day = int(today.strftime('%d')) - 1
    day = str(day)
    month = today.strftime('%m')
    year = today.strftime('%Y')
    filename = (month + '_' + day + '_' + year + '.xls')
    print('filename is: outage_' + filename)
    storeOpen = 9
    storeClose = 21
    startTime = time.time()
    full_file = 'E:\Savers\Spreadsheets\Outage\\' + year + '\outage_' + filename
    mode = input('Is this [monthly] or [daily]? \n')
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

        else:
            print('Invalid input.')
            break

    data = data.drop(data[data.Duration == 0].index) 
    data = data.drop(data[data.Duration == 1].index)
    data = data.drop(data[data.Store == '2955-FW-1'].index)
    data = data.drop(data[data.Store == 'TDX-ESX-VPN'].index)
    data['Site DOWN'] = pd.to_datetime(data['Site DOWN']) 
    data['Site UP'] = pd.to_datetime(data['Site UP'])

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

    def apply(data):
        data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
        data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
        data.insert(6, 'During_Hours', value='')
        data.insert(10, 'Notes', value='')
        data.to_excel(full_file)

    apply(data)
    data = data.drop_duplicates('Adjusted_Up')

    def breakdown(x, y):
        #First breakdown downtime timestamp. Example string "2019-08-11 10:31:00"
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
      
        if hour and hourB in range(storeOpen, storeClose):
            
            if hourB > hour:
                sumMinutes = (hourB - hour)*60
                sumMinutes = sumMinutes + (minuteB - minute)
                print(sumMinutes)
                
            elif hourB == hour:
                sumMinutes = (minuteB - minute)
                print(sumMinutes)
                
        else:
            print(0)
        
    for index, row in data.iterrows():
        data1 = str(row['Adjusted_Down'])
        data2 = str(row['Adjusted_Up'])
        print(row['Store'], 'Adjusted_Down:', row['Adjusted_Down'], 'Adjusted_Up:', row['Adjusted_Up'], breakdown(data1, data2))
        
    endTime = time.time()
    print('The conversion function took %s seconds to calculate.' % (endTime - startTime))

except KeyboardInterrupt:
    print('Program terminated by user.')
