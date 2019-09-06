import pandas as pd
from pandas import Timestamp
import pytz
from pytz import all_timezones
import datetime
import xlrd
import xlwt
import time
import numpy as np

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

##data[data.Adjusted_Down.apply(lambda x : x.split(' ')[1]) > == '09:00:00']
