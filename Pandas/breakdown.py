#!Python 3
storeOpen = 9
storeClose = 22
string1 = '2019-08-11 06:31:00'
string2 = '2019-08-11 23:00:00'

def breakdown(x,y):
    string1 = x.split() 
    variable2 = string1[1] 
    dateVariable2 = variable2.split(':') 
    hour = int(dateVariable2[0]) 
    minute = int(dateVariable2[1]) 
    seconds = int(dateVariable2[2])

    #For uptime
    string1B = y.split()
    variable2B = string1B[1]
    dateVariable2B = variable2B.split(':')
    hourB = int(dateVariable2B[0])
    minuteB = int(dateVariable2B[1])
    secondsB = int(dateVariable2B[2])

    if hour or hourB in range(storeOpen, storeClose):

        if hourB not in range(storeOpen, storeClose):
            hourB = 22
            minuteB = 0
            secondsB = 0

        if hour not in range(storeOpen, storeClose):
            hour = 9
            minute = 0
            seconds = 0

        if hourB > hour:
            sumMinutes = (hourB - hour)*60
            sumMinutes = sumMinutes + (minuteB - minute)
            print(sumMinutes)

        elif hourB == hour:
            sumMinutes = (minuteB - minute)
            print(sumMinutes)
        
    else:
        print(0)

print(breakdown(string1,string2))
