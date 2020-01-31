#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

#Imports for the code to function
import pandas as pd
import subprocess

#Function attempts to open file, exits program if unable to open
def file_test(file):
        try:
                open(file)
        except:
                print('Unable to open:', file)
                exit()

#Takes string and removes non numeric characters, leaves string that can be converted to float
def float_format(a, b, c, d, e, f):
        for x in range(len(data[a])):
                data[a][x] = data[a][x].replace(' Mbps', '')
        for x in range(len(data[b])):
                data[b][x] = data[b][x].replace(' Mbps', '')
        for x in range(len(data[c])):
                data[c][x] = data[c][x].replace(' Mbps', '')                
        for x in range(len(data[d])):
                data[d][x] = data[d][x].replace(' Mbps', '')
        for x in range(len(data[e])):
                data[e][x] = data[e][x].replace(' Mbps', '')
        for x in range(len(data[f])):
                data[f][x] = data[f][x].replace(' Mbps', '')

#Defines file as raw string, uses function to test and then opens file as dataframe
file = r'Ben Test Utilization.xls'
file_test(file)
data = pd.read_excel(file, header=[2])
final_data = pd.read_excel(file, header=[2])

#Apply float formatting function to necessary columns
float_format('Average Receive bps',
               'Peak Receive bps',
               'Received Bandwidth',
               'Average Transmit bps',
               'Peak Transmit bps',
               'Transmit Bandwidth')

#Calculate avg and peak utilization for down and up bandwidth as a percentage
final_data['Average Receive Utilization %'] = (data['Average Receive bps'].astype(float)/
                                               data['Received Bandwidth'].astype(float))*100
final_data['Peak Receive Utilization %'] = (data['Peak Receive bps'].astype(float)/
                                            data['Received Bandwidth'].astype(float))*100
final_data['Average Upload Utilization %'] = (data['Average Transmit bps'].astype(float)/
                                              data['Transmit Bandwidth'].astype(float))*100
final_data['Peak Upload Utilization %'] = (data['Peak Transmit bps'].astype(float)/
                                           data['Transmit Bandwidth'].astype(float))*100

#Saves the analyzed file and opens it in excel
final_data.to_excel('lab.xlsx', 'w+')
subprocess.call([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE',
                 r'C:\Users\cgarrido\Desktop\lab.xlsx'])
