#!/bin/bash
cat hosts.txt >> /etc/hosts &
mysqld_safe &
sleep 5
mysql < database.sql
mysqladmin -u root password toor
apache2ctl start

while :;
do
:;
done
