#!/bin/bash



### SSL Certificate Expire Day Check Script ###
if [ "$1" = '' ];then
    echo "Need URL."
    exit 1;
fi
TARGET_URL=$1
EXP_DAY=`openssl s_client -connect ${TARGET_URL}:443 < /dev/null 2> /dev/null | openssl x509 -text 2> /dev/null | grep "Not After" | sed -e 's/^ *//g' | cut -d " " -f 4,5,6,7,8`
NOW_TIME=`date +%s`
EXP_TIME=`date +%s -d "${EXP_DAY}"`
if [ "${EXP_DAY}" != '' -a ${NOW_TIME} -lt ${EXP_TIME} ]; then
    echo $(((EXP_TIME-NOW_TIME)/(60*60*24)))
else
    echo "ERROR"
    exit 1;
fi
