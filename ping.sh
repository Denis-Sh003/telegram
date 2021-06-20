#!/bin/bash
ping -c 4 10.1.2.10  >> /dev/null 

if [ "$?" = "0" ]; then
 echo " Сервер запущен"
else 
 echo " Сервер выключен"
fi

exit 0 
