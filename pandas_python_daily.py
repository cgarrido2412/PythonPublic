#Author: Charles Garrido
#Creation Date: 4 Aug. 2019
#Last Revision: 21 Oct. 2019
#Description: Takes the daily outage report from Orion and localizes all outages to local time, adds a note column for analysis
#Notes: Saved file must be in the format 'outage_MONTH_DAY_YEAR.xls'
print('Author: Charles Garrido')
print('Creation Date: 4 Aug. 2019')
print('Last Revision: 21 Oct. 2019')
print('Description: Takes the daily outage report from Orion and localizes all outages to local time, adds a note column for analysis')
print("Saved file must be in the format 'outage_MONTH_DAY_YEAR.xls'")

#import modules for code to work, for modules that are not native to python use "pip install MODULE"
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time

#define date, filename, and store open and close hours
day = str(input("Enter the day(integer): "))
month = str(input('Enter the month(integer): '))
year = str(input('Enter the year(integer): '))
filename = (month + '_' + day + '_' + year + '.xls')
print('filename is: outage_' + filename)
date = (month + '/' + day + '/' + year)
storeOpen = '09:00:00'
storeClose = '21:00:00'

#timer starts, measures time elapsed to convert time_zone information to local time
startTime = time.time()

#loads the filename as a dataframe
data = pd.read_excel('E:\Savers\Spreadsheets\Outage\outage_' + filename, header=[2]) 

#drop duplicate site up times, also removes any outages that have a 0 or 1 duration
data = data.drop_duplicates('Site UP') 
data = data.drop(data[data.Duration == 0].index) 
data = data.drop(data[data.Duration == 1].index)

#sets 'Site DOWN/UP' as date columns, then defines a conversion function to change the date series to dataframe timestamp
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

#applies the conversion function, creates an empty 'Notes' column for outage analysis
data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
data.insert(9, 'Notes', value='')

#saves the spreadsheet
data.to_excel('E:\Savers\Spreadsheets\Outage\outage_' + filename) 

#an attempt to filter store outage minutes by what happens within business hours, not necessary for script to function
#data = data.set_index('Adjusted_Down')
#try to create storeOpenParameter variable which combines 'date' and 'storeOpen'
#filtered_data = data[(data.index > '10/17/19 09:00:00') & (data.index <= '10/17/19 21:00:00')]
#filtered_data.to_excel('estimated.xls')

#timer for script ends, prints total time elapsed
endTime = time.time()
print('The conversion function took %s seconds to calculate.' % (endTime - startTime))
