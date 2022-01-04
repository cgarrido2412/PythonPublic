#pip install junos-eznc
import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")

try:
    with Device(mode='serial', port='port', user=junos_username, passwd=junos_password) as dev:
        print (dev.facts)
        cu = Config(dev)
        cu.lock()
        cu.load(path='/tmp/config_mx.conf')
        cu.commit()
        cu.unlock()

except Exception as err:
    print (err)
    sys.exit(1)
