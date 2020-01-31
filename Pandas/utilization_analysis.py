#! /usr/bin/env python3
import pandas as pd

def file_test(file):
        try:
                open(file)
        except:
                print('Unable to open:', file)
                exit()

file = r'Ben Test Utilization.xls'
file_test(file)
data = pd.read_excel(file, header=[2])
final_data = pd.read_excel(file, header=[2])

for x in range(len(data['Average Receive bps'])):
        data['Average Receive bps'][x] = data['Average Receive bps'][x].replace(' Mbps', '')

for x in range(len(data['Peak Receive bps'])):
        data['Peak Receive bps'][x] = data['Peak Receive bps'][x].replace(' Mbps', '')

for x in range(len(data['Received Bandwidth'])):
        data['Received Bandwidth'][x] = data['Received Bandwidth'][x].replace(' Mbps', '')

for x in range(len(data['Average Transmit bps'])):
        data['Average Transmit bps'][x] = data['Average Transmit bps'][x].replace(' Mbps', '')

for x in range(len(data['Peak Transmit bps'])):
        data['Peak Transmit bps'][x] = data['Peak Transmit bps'][x].replace(' Mbps', '')

for x in range(len(data['Transmit Bandwidth'])):
        data['Transmit Bandwidth'][x] = data['Transmit Bandwidth'][x].replace(' Mbps', '')

final_data['Average Receive Utilization %'] = (data['Average Receive bps'].astype(float)/data['Received Bandwidth'].astype(float))*100
final_data['Peak Receive Utilization %'] = (data['Peak Receive bps'].astype(float)/data['Received Bandwidth'].astype(float))*100
final_data['Average Upload Utilization %'] = (data['Average Transmit bps'].astype(float)/data['Transmit Bandwidth'].astype(float))*100
final_data['Peak Upload Utilization %'] = (data['Peak Transmit bps'].astype(float)/data['Transmit Bandwidth'].astype(float))*100

final_data.to_excel('lab.xls', 'w+')
