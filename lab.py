import pandas as pd

data = pd.read_excel('E:\Savers\Python\Python3 - Master\lab.xlsx')

def breakdown(x, y):
    string1 = x.split()
    variable1 = string1[0]
    dateVariable = variable1.split('-')
    variable2 = string1[1]
    dateVariable2 = variable2.split(':')
    hour = int(dateVariable2[0])
    minute = int(dateVariable2[1])
    seconds = int(dateVariable2[2])

    string1B = y.split()
    variable1B = string1B[0]
    dateVariableB = variable1B.split('-')
    variable2B = string1B[1]
    dateVariable2B = variable2B.split(':')
    hourB = int(dateVariable2B[0])
    minuteB = int(dateVariable2B[1])
    secondsB = int(dateVariable2B[2])

    if hourB > hour:
        sumMinutes = (hourB - hour)*60
        sumMinutes = sumMinutes + (minuteB - minute)
        print(sumMinutes)
    elif hourB == hour:
        sumMinutes = (minuteB - minute)
        print(sumMinutes)
