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
data['duration'] = data['duration']/np.timedelta64(1, 'm')
