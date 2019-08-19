#https://www.codementor.io/packt/the-python-api-for-juniper-networks-pr5rdl08c
from ncclient import manager

  conn = manager.connect(
      host='192.168.24.252',
      port='830',
      username='netconf',
      password='juniper!',
      timeout=10,
      device_params={'name':'junos'},
      hostkey_verify=False)

  result = conn.command('show version', format='text')
  print(result)
  conn.close_session()
