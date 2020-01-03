import urllib.request
import re
print('We will try to open this url, in order to get IP Address.')
url = 'http://checkip.dyndns.org'
print(url)
request = urllib.request.urlopen(url).read()
theIP = re.findall(r"[0-255]{1,3}.[0-255]{1,3}.d{1,3}.[0-255]{1,3}", request) #fix re
print('Your IP Address is:', theIP)
