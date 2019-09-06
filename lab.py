import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time
import numpy as np
import xlsxwriter
from threading import Timer

def monthly_outage():
    #Columns should be in the following format before running the script:
    #STORE | REGION | DESIGN | VENDOR | TIME_ZONE | SITE DOWN | SITE UP | DURATION
    #open cli and navigate to C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\Scripts>
    #use "pip install APPLICATION" i.e., "pip install pandas" to download modules and allow them to be imported
    #Timer for the script starts, opens excel as dataframe and eliminates duplicates + durations with "0" value
    startTime = time.time()
    fileName = str(input('Please enter the filename:'))
    data = pd.read_excel(fileName)
    data = data.drop(data[data.Duration == 0].index)
    data['Site DOWN'] = pd.to_datetime(data['Site DOWN'])
    data['Site UP'] = pd.to_datetime(data['Site UP'])
    #Defines time conversion function, looks at value in "Time_Zone" and localizes it to matching dictionary value
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
    #Application of conversion function, removes duplicate adjusted_up times, then saves
    data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
    data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
    data = data.drop_duplicates('Adjusted_Up')
    data.to_excel('estimated.xls', 'a+')
    #Timer for the script stops, prints total time elapsed within python shell 
    endTime = time.time()
    print('The conversion function took %s seconds to calculate.' % (endTime - startTime))

def daily_outage():
    monthly_outage()
    #index based on local down time, drop anything outside of business hours and saves as new .xls file
    data = data.set_index('Adjusted_Down')
    filtered_data = data[(data.index > '09/05/19 09:00:00') & (data.index <= '09/05/19 21:00:00')]
    filtered_data.to_excel('estimated.xls') 

def leave():
    def timeout():
        print("15 minutes have passed!")
    t = Timer(15 * 60, timeout)
    t.start()
    t.join()

def in_business_hours():
    data = pd.read_excel('lab.xlsx')
    data['duration'] = data['Adjusted_Up'] - data['Adjusted_Down']
    data['duration'] = data['duration']/np.timedelta64(1,'m')

def conditional_formatting():
    data = pd.read_excel('lab.xlsx')
    writer = pd.ExcelWriter('lab.xlsx', engine='xlsxwriter')
    data.to_excel(writer, sheet_name='Sheet1')
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

data = pd.read_excel('lab.xlsx')
data['duration'] = data['Adjusted_Up'] - data['Adjusted_Down']
data['duration'] = data['duration']/np.timedelta64(1,'m')
dfn = data [(data.Adjusted_Down >= '09:00:00') & (data.Adjusted_Down <= '21:00:00')]
dfx = data [(data.Adjusted_Up >= '09:00:00') & (data.Adjusted_Up <= '21:00:00')]
daytime = data[(dfx-dfn).astype('timedelta64[h]')]

##site_open = data[(data.Adjusted_Down >= '09:00:00')]
##site_close = data[(data.Adjusted_Down <= '21:00:00')]
##data['daytime'] = data['site_open'] - data['site_close']
##data['daytime'] = data['daytime']/np.timedelta64(1, 'm')

##data[data.Adjusted_Down.apply(lambda x : x.split(' ')[1]) >= '09:00:00']

#Try using to_datetime to convert Adjusted_Down and Adjusted_Up column &
#then subtract them normally. You can also use dt.hour to subset the hours for each day between 9AM & 9PM
