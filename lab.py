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
site_open = data[(data.Adjusted_Down >= '09:00:00')]
site_close = data[(data.Adjusted_Down <= '21:00:00')]
data['daytime'] = data['site_open'] - data['site_close']
data['daytime'] = data['daytime']/np.timedelta64(1, 'm')
