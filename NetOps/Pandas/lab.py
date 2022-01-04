import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time

startTime = time.time()
data = pd.read_excel('E:\Savers\Python\Python3 - Master\lab_final.xls', header=[2])
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
data = data.drop_duplicates('Adjusted_Up') 
data.insert(9, 'Notes', value='')
data.to_excel('E:\Savers\Python\Python3 - Master\lab_final_copy.xls', 'a+')

def breakdown(x, y):
    #data1
    string1 = x.split() 
    variable1 = string1[0] 
    dateVariable = variable1.split('-') 
    variable2 = string1[1] 
    dateVariable2 = variable2.split(':') 
    hour = int(dateVariable2[0]) 
    minute = int(dateVariable2[1]) 
    seconds = int(dateVariable2[2]) 

    #data2
    string1B = y.split()
    variable1B = string1B[0]
    dateVariableB = variable1B.split('-')
    variable2B = string1B[1]
    dateVariable2B = variable2B.split(':')
    hourB = int(dateVariable2B[0])
    minuteB = int(dateVariable2B[1])
    secondsB = int(dateVariable2B[2])

    if hour and hourB in range(9, 21):
        
        if hourB > hour:
            sumMinutes = (hourB - hour)*60
            sumMinutes = sumMinutes + (minuteB - minute)
            print(sumMinutes)
            
        elif hourB == hour:
            sumMinutes = (minuteB - minute)
            print(sumMinutes)

    else:
        pass

for index, row in data.iterrows():
    print(str(row['Store']))
    print(str(row['Adjusted_Down']))
    print(str(row['Adjusted_Up']))
    data1 = str(row['Adjusted_Down'])
    data2 = str(row['Adjusted_Up'])
    breakdown(data1, data2)
    
endTime = time.time()
print('The conversion function took %s seconds to calculate.' % (endTime - startTime))
