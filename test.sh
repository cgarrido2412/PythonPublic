#!bin/sh
#to create new .sh file while in shell
#vi (filename)
#shift A
#type
#arrow down
#:wq (enter)
logger "STARTING sleep 120s to complete boot process"
sleep 120
logger "AFTER 120s"
cp /var/root/test.slax /var/db/scripts/op/
logger "STARTING move file and configuration using script"
#The following line DOES work.
/usr/sbin/cli -c 'configure;set system host-name RESCUE;set system auto-snapshot;set system domain-name savers.com;set system time-zone America/Los_Angeles;set system root-authentication encrypted-password "$1$YgpGVOl8$X2OYPQqveUQ/4AKZlZYQ.1";set system services ssh;set interfaces ge-0/0/22 unit 0 family ethernet-switching port-mode trunk;set interfaces ge-0/0/22 unit 0 family ethernet-switching vlan members all;set interfaces ge-0/0/23 unit 0 family ethernet-switching port-mode trunk;set interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members all;set interfaces me0 unit 0 family inet dhcp vendor-id Juniper-ex2200-24p-4g;set interfaces vlan description "Management interface";set interfaces vlan unit 0 family inet dhcp vendor-id Juniper-ex2200-24p-4g;set interfaces vlan unit 128 family inet dhcp;set vlans MGMT vlan-id 128;set vlans MGMT l3-interface vlan.128;set vlans default l3-interface vlan.0;commit'
