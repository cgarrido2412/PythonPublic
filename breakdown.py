import pandas as pd

def breakdown(x, y):
    #First breakdown downtime timestamp. Example string "2019-08-11 10:31:00"
    string1 = x.split() #"2019-08-11" "10:31:00"
    variable1 = string1[0] #"2019-08-11"
    dateVariable = variable1.split('-') #"2019" "08" "11"
    variable2 = string1[1] #"10:31:00"
    dateVariable2 = variable2.split(':') #"10" "31" "00"
    hour = int(dateVariable2[0]) #"10"
    minute = int(dateVariable2[1]) #"31"
    seconds = int(dateVariable2[2]) #"00"

    #For uptime
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

data = pd.read_excel('E:\Savers\Python\Python3 - Master\lab.xlsx')

for index, row in data.iterrows():
    data1 = str(row['Adjusted_Down'])
    data2 = str(row['Adjusted_Up'])
    breakdown(data1, data2)
