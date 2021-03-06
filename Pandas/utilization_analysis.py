#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import pandas as pd
import subprocess

def analyze_data(r1, r2, r3, r4, r5, t1, t2, t3, t4, t5):
        final_data[r4] = (data[r1].astype(float)/
                          data[r3].astype(float))*100
        final_data[r5] = (data[r2].astype(float)/
                          data[r3].astype(float))*100
        final_data[t4] = (data[t1].astype(float)/
                          data[t3].astype(float))*100
        final_data[t5] = (data[t2].astype(float)/
                          data[t3].astype(float))*100

def file_test(file):
        try:
                open(file)
        except:
                print('Unable to open:', file)
                exit()

def float_check(x):
        try:
                float(x)
                return True
        except ValueError:
                return False

def float_format(a, b, c, d, e, f):
        for x in range(len(data[a])):
                if float_check(data[a][x][:-5]) is True:
                        data[a][x] = float(data[a][x][:-5])
                else:
                        exit()
        for x in range(len(data[b])):
                if float_check(data[b][x][:-5]) is True:
                        data[b][x] = float(data[b][x][:-5])
                else:
                        exit()
        for x in range(len(data[c])):
                if float_check(data[c][x][:-5]) is True:
                        data[c][x] = float(data[c][x][:-5])
                else:
                        exit()
        for x in range(len(data[d])):
                if float_check(data[d][x][:-5]) is True:
                        data[d][x] = float(data[d][x][:-5])
                else:
                        exit()
        for x in range(len(data[e])):
                if float_check(data[e][x][:-5]) is True:
                        data[e][x] = float(data[e][x][:-5])
                else:
                        exit()
        for x in range(len(data[f])):
                if float_check(data[f][x][:-5]) is True:
                        data[f][x] = float(data[f][x][:-5])
                else:
                        exit()

if __name__ == '__main__':
        try:
                file = r'C:\Users\cgarrido\Desktop\Ben Test Utilization.xls'
                file_test(file)
                data = pd.read_excel(file, header=[2])
                final_data = pd.read_excel(file, header=[2])

                float_format('Average Receive bps',
                               'Peak Receive bps',
                               'Received Bandwidth',
                               'Average Transmit bps',
                               'Peak Transmit bps',
                               'Transmit Bandwidth')

                analyze_data('Average Receive bps',
                          'Peak Receive bps',
                          'Received Bandwidth',
                          'Average Receive Utilization %',
                          'Peak Receive Utilization %',
                          'Average Transmit bps',
                          'Peak Transmit bps',
                          'Transmit Bandwidth',
                          'Average Upload Utilization %',
                          'Peak Upload Utilization %')

                final_data.to_excel('lab.xlsx', 'w+')
                subprocess.call([r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE',
                                 r'C:\Users\cgarrido\Desktop\lab.xlsx'])
        except KeyboardInterrupt:
                print('Program terminated.')
else:
        print('utilization_analysis.py successfully imported.')
