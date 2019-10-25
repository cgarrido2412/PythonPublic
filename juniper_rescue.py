import sys
from jnpr.junos import Device
from pprint import pprint
from getpass import getpass
from jnpr.junos.exception import ConnectError
from jnpr.junos.utils.config import Config

dev = Device(host='vMX-1', user='lab', passwd='lab123')

try:
    dev.open()
    
    #Try to load local configuration file
    try:
        conf_file = 'configs/junos-config-interfaces.conf'

        with Config(dev, mode='exclusive') as cu:
            cu.load(path=conf_file, merge=True)
            cu.commit()

    except:
        print('Unable to load local configuration file.')
        #Try to load rescue configuration
        try:
            
            with Config(dev, mode='exclusive') as cu:
                resue = cu.rescue(action="reload")
                
                if rescue is False:
                    print ("No existing rescue configuration.")
                    
                else:
                    cu.pdiff()
                    cu.commit()
                    
        except:
            print('Unable to utilize rescue configuration.')
    
except ConnectError as err:
    print('Cannot connect to device: {0}'.format(err))
    sys.exit(1)

print(dev.facts)
dev.close
