#Columns should be in the following format before running the script:
#STORE | REGION | DESIGN | VENDOR | TIME_ZONE | SITE DOWN | SITE UP | DURATION

#open cli and navigate to C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\Scripts>
#use "pip install APPLICATION" i.e., "pip install pandas" to download modules and allow them to be imported
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time

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
data.to_excel('python_analyzed_report.xls', 'a+')

#Timer for the script stops, prints total time elapsed within python shell 
endTime = time.time()
print('The conversion function took %s seconds to calculate.' % (endTime - startTime))
