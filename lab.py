import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
from datetime import time
from threading import Timer
import time as t
import xlrd
import xlwt
import numpy as np
import xlsxwriter

data = pd.read_excel('lab.xlsx')

#creates new column 'duration' by indexing difference between up and down time. returns float
data['duration'] = data['Adjusted_Up'] - data['Adjusted_Down']
data['duration'] = data['duration']/np.timedelta64(1,'m')

#returns a minute by minute breakdown in between Adjusted_Down and Adjusted_Up
s = data.apply(lambda row: pd.date_range(row['Adjusted_Down'], row['Adjusted_Up'], freq='T'), axis=1).explode()

#returns total amount of downtime between 9-21 but not by store 
total = s.dt.time.between(time(9), time(21)).sum()  

#range of index[0] for s 
slist = range(0, 227) #already includes the +1 

#due to thy this loop itterates, it returns the same thing as 'duration' column 
for num in slist:
    Duration = s[num].count()
    print(Duration)  

#secondary function to test
def by_month():
    s = data.apply(lambda row: pd.date_range(row['Adjusted_Down'], row['Adjusted_Up'], freq='T'), axis=1).explode()
    downtime = pd.DataFrame({
        'Month': s.astype('datetime64[M]'),
        'IsDayTime': s.dt.time.between(time(9), time(21))
    })
    downtime.groupby('Month')['IsDayTime'].sum()

#data.to_excel('delete.xls', 'a+')
