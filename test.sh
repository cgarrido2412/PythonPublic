#!bin/sh
logger "STARTING sleep 120s to complete boot process"
sleep 120
logger "AFTER 120s"
cp /var/root/test.slax /var/db/scripts/op/
logger "STARTING move file and configuration using script"
/usr/sbin/cli -c 'configure;set system scripts op file test.slax;commit comment "Commit by script"'
logger "STARTING sleep 120s to finish commit changes and start .SLAX script"
sleep 120
logger "AFTER 120s"
/usr/sbin/cli -c  'op test'
