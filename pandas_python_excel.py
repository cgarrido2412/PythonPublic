#C:\Users\cgarrido\AppData\Local\Programs\Python\Python37\Scripts>
import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time

startTime = time.time()
data = pd.read_excel('lab.xls')
data = data.drop(data[data.Duration == 0].index)
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

data['Adjusted_Down'] = data[['Time_Zone', 'Site DOWN']].apply(conversion_function, axis=1)
data['Adjusted_Up'] = data[['Time_Zone', 'Site UP']].apply(conversion_function, axis=1)
data = data.drop_duplicates('Adjusted_Up')
data.to_excel('final.xls', 'a+')

endTime = time.time()
print('The conversion function took %s seconds to calculate.' % (endTime - startTime))
