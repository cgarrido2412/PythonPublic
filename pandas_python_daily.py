import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time
startTime = time.time() 
data = pd.read_excel('E:\Savers\Spreadsheets\Outage\outage_10_16_2019.xls', header=[2]) 
data = data.drop_duplicates('Site UP') 
data = data.drop(data[data.Duration == 0].index) 
data = data.drop(data[data.Duration == 1].index) 
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
data.insert(9, 'Notes', value='')
data.to_excel('E:\Savers\Spreadsheets\Outage\outage_10_16_2019.xls') 
data = data.set_index('Adjusted_Down')
filtered_data = data[(data.index > '10/16/19 09:00:00') & (data.index <= '10/16/19 21:00:00')]
filtered_data.to_excel('estimated.xls') 
endTime = time.time()
print('The conversion function took %s seconds to calculate.' % (endTime - startTime))
