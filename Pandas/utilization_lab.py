import pandas as pd

file1 = input('Enter file path: \n')

try:
    open(file1)
    
except:
    print('Unable to open:', file1)
    exit()
    
file2 = input('Enter second file path: \n')

try:
    open(file2)
    
except:
    print('Unable to open:', file2)
    exit()
    
def utilization_report(file1, file2):
    data1 = pd.read_excel(file1, header=[2], usecols=range(1,4))
    data2 = pd.read_excel(file2, header=[2], usecols=range(1,4))
    data3 = pd.merge(data2, data1, on='Full Name')
    print(data3)
    data3.to_excel('lab3.xls', 'a+')
    
utilization_report(file1, file2)
