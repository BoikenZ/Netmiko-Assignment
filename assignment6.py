from netmiko import ConnectHandler
from getpass import getpass
R1 = {"host": "192.168.144.11", "username":"boiken", "password": getpass() , "device_type": "cisco_ios_telnet", "secret": "0477"}
R2 = {"host": "192.168.144.12", "username":"boiken", "password": getpass() , "device_type": "cisco_ios_telnet", "secret": "0477"}

session = ConnectHandler(**R1)
session.enable()
output = session.send_config_from_file(config_file='R1.conf')
print(output)
session.disconnect()

session = ConnectHandler(**R2)
session.enable
output = session.send_config_from_file(config_file='R2.conf')
print(output)
session.disconnect()
