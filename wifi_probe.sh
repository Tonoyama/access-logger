#!/bin/bash

url='https://www.google.com/'

status=`/usr/bin/curl -LI $url -o /dev/null -w '%{http_code}' -s`

if test $status -ne 200; then
  echo $status && sudo ifconfig wlan0 up && sleep 20s && sudo /usr/bin/python3 /home/pi/access-logger/connect.py
fi