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
/usr/sbin/cli -c 'configure;set system host-name RESCUE;set system root-authentication encrypted-password "$1$0i/HauA1$z62xODFQj5Hny2jflhH53/";set system scripts op file test.slax;commit'
logger "STARTING sleep 120s to finish commit changes and start .SLAX script"
sleep 120
logger "AFTER 120s"
#WHY WON'T THIS PART WORK
/usr/sbin/cli -c 'op test'
/usr/sbin/cli -c 'op test'
/usr/sbin/cli -c 'op test'
