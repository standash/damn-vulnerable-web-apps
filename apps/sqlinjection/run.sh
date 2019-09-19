#!/bin/bash
mysqld_safe &
sleep 5
mysql < mysqlData.sql
mysqlimport --local SQLInjection users.txt

mysqladmin -u root password toor

nodejs /var/www/server.js
