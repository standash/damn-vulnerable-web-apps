#!/bin/bash

nodejs &

export logpath=/var/log/mongodb
export logfile=$logpath/mongodb.log
touch $logfile
mongod --quiet --logpath $logfile --logappend &

COUNTER=0
grep -q 'waiting for connections on port' $logfile
while [[ $? -ne 0 && $COUNTER -lt 10 ]] ; do
    sleep 1
    let COUNTER+=1
    grep -q 'waiting for connections on port' $logfile
done

mongoimport --db honeypot --collection users --jsonArray mongoData.json 
nodejs /var/www/server.js
