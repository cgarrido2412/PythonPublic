import sys
from jnpr.junos import Device
from pprint import pprint
from getpass import getpass
from jnpr.junos.exception import ConnectError
from jnpr.junos.utils.config import Config

dev = Device(host='vMX-1', user='lab', passwd='lab123')

try:
    dev.open()
    with Config(dev, mode='exclusive') as cu:
        resue = cu.rescue(action="reload")
        if rescue is False:
            print ("No existing rescue configuration.")
        else:
            cu.pdiff()
            cu.commit()
    
except ConnectError as err:
    print('Cannot connect to device: {0}'.format(err))
    sys.exit(1)

print(dev.facts)
dev.close
