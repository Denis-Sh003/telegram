#!/bin/bash
ping -c 1 10.1.2.10  >> /dev/null 

if [ "$?" = "0" ]; then
 echo " server on ✅"
else 
 echo " server off ❌"
fi

exit 0 
