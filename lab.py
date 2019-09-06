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

#only for leave function
from threading import Timer

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
