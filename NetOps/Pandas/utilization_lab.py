import pandas as pd
from datetime import date

today = date.today()
d2 = today.strftime("%B %d, %Y")

def file_test(file):
    
    try:
        open(file)
        
    except:
        print('Unable to open:', file)
        exit()
        
file1 = input('Enter file path: \n')
file_test(file1)
file2 = input('Enter second file path: \n')
file_test(file2)

def utilization_report(file1, file2):
    data1 = pd.read_excel(file1, header=[2], usecols=range(1,4))
    data1 = data1.rename(columns={'Received Percent Utilization - Average':d2,
                                  "Received Percent Utilization - Max":d2,
                                  'Full Name':'Store'})
    data2 = pd.read_excel(file2, header=[2], usecols=range(1,4))
    data2 = data2.rename(columns={'Received Percent Utilization - Average':d2,
                                  "Received Percent Utilization - Max":d2,
                                  'Full Name':'Store'})
    data3 = pd.merge(data2, data1, on='Store')
    print(data3)
    data3.to_excel('lab3.xls', 'a+')
    
utilization_report(file1, file2)
