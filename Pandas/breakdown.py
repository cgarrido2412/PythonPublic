#!Python 3
storeOpen = 9
storeClose = 22
string1 = '2019-08-11 22:31:42'
string2 = '2019-08-11 23:33:51'

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
            if hourB > 22:
                hourB = 22
                minuteB = 0
                secondsB = 0
            else:
                pass

        if hour not in range(storeOpen, storeClose):
            if hour < 9:
                hour = 9
                minute = 0
                seconds = 0
            else:
                pass

        if hourB > hour:
            sumMinutes = (hourB - hour)*60
            sumMinutes = sumMinutes + (minuteB - minute)
            if sumMinutes < 0:
                sumMinutes = 0
            else:
                pass
            print(sumMinutes)

        elif hourB == hour:
            sumMinutes = minuteB - minute
            if sumMinutes < 0:
                sumMinutes = 0
            print(sumMinutes)
        
    else:
        print(0)

print(breakdown(string1,string2))
