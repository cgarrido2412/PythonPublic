#!/usr/bin/env python

program_running = True

while program_running is True:

    try:
        storeOpen = 9
        storeClose = 21
        outage_start = input('Enter outage start time:\n')
        outage_end = input('Enter outage end time:\n')
        string1 = '2019-08-11 ' + outage_start
        string2 = '2019-08-11 ' + outage_end

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

                    if hourB > 21:
                        hourB = 21
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

    except KeyboardInterrupt:
        print('Program terminated.')
