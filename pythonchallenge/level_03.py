#http://www.pythonchallenge.com/pc/def/equality.html
'''
Based on web page, I think it'll need a re solution that looks for three capital letters that surround a
lowecase letter on either side.

Example:
AEGyUIO = True
YHEwNYH = True
NEHBxHH = False
JxehHEN = False
'''
import urllib.request
import re
from collections import Counter
html = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
c = Counter(data)
my_list = re.findall('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]{3}[abcdefghijklmnopqrstuvwxyz]{1}[ABCDEFGHIJKLMNOPQRSTUVWXYZ]{3}', data)
freq = {}
for items in my_list:
    freq[items] = my_list.count(items)
print(freq)
