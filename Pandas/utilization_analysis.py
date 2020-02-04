#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import pandas as pd
import subprocess

def analyze(x, y, z):
        final_data[z] = (data[x].astype(float)/
                         data[y].astype(float))*100

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

file = r'Ben Test Utilization.xls'
data = pd.read_excel(file, header=[2])
final_data = pd.read_excel(file, header=[2])

float_format('Average Receive bps',
               'Peak Receive bps',
               'Received Bandwidth',
               'Average Transmit bps',
               'Peak Transmit bps',
               'Transmit Bandwidth')

analyze('Average Receive bps',
        'Received Bandwidth',
        'Average Receive Utilization %')
analyze('Peak Receive bps',
        'Received Bandwidth',
        'Peak Receive Utilization %')
analyze('Average Transmit bps',
        'Transmit Bandwidth',
        'Average Upload Utilization %')
analyze('Peak Transmit bps',
        'Transmit Bandwidth',
        'Peak Upload Utilization %')

final_data.to_excel('lab.xlsx', 'w+')
subprocess.call([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE',
                 r'C:\Users\cgarrido\Desktop\lab.xlsx'])
