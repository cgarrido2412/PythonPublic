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
data['duration'] = data['Adjusted_Up'] - data['Adjusted_Down']
data['duration'] = data['duration']/np.timedelta64(1,'m')

def explode():
    s = df.apply(lambda row: pd.date_range(row['Adjusted_Down'], row['Adjusted_Up'], freq='T'), axis=1).explode()
    s.dt.time.between(time(9), time(21)).sum()    

def by_month():
    s = data.apply(lambda row: pd.date_range(row['Adjusted_Down'], row['Adjusted_Up'], freq='T'), axis=1).explode()
    downtime = pd.DataFrame({
        'Month': s.astype('datetime64[M]'),
        'IsDayTime': s.dt.time.between(time(9), time(21))
    })
    downtime.groupby('Month')['IsDayTime'].sum()

#data.to_excel('delete.xls', 'a+')
