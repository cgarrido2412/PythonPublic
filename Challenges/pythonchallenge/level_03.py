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
'''
[^A-Z]+ will match anything NOT an uppercase letter
[A-Z]{3} followed by exactly three uppercase letters
([a-z]) then a lower case letter
[A-Z]{3} and exactly three upppercase letters
[^A-Z]+ followed by anything NOT an uppercase letter 
'''
print(''.join(re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', data)))
