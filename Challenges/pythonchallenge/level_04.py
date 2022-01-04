#http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request
import re
from collections import Counter
html = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').read().decode()
print(html)
#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
#and the next nothing is 44827
#and the next nothing is 45439
