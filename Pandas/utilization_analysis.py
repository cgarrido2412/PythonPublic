#! /usr/bin/env python3
import pandas as pd
import subprocess

def file_test(file):
        try:
                open(file)
        except:
                print('Unable to open:', file)
                exit()

def integer_format(y):
        for x in range(len(data[y])):
                data[y][x] = data[y][x].replace(' Mbps', '')

file = r'Ben Test Utilization.xls'
file_test(file)
data = pd.read_excel(file, header=[2])
final_data = pd.read_excel(file, header=[2])

integer_format('Average Receive bps')
integer_format('Peak Receive bps')
integer_format('Received Bandwidth')
integer_format('Average Transmit bps')
integer_format('Peak Transmit bps')
integer_format('Transmit Bandwidth')

final_data['Average Receive Utilization %'] = (data['Average Receive bps'].astype(float)/data['Received Bandwidth'].astype(float))*100
final_data['Peak Receive Utilization %'] = (data['Peak Receive bps'].astype(float)/data['Received Bandwidth'].astype(float))*100
final_data['Average Upload Utilization %'] = (data['Average Transmit bps'].astype(float)/data['Transmit Bandwidth'].astype(float))*100
final_data['Peak Upload Utilization %'] = (data['Peak Transmit bps'].astype(float)/data['Transmit Bandwidth'].astype(float))*100

final_data.to_excel('lab.xlsx', 'w+')
subprocess.call([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE', r'C:\Users\cgarrido\Desktop\lab.xlsx'])
