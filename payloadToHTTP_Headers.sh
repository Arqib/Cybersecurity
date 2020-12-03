#!/bin/bash
payload="$1"
if [ -z "$payload" ]
then
      echo "Provide a payload file"
else
      sed -z 's/\n/\r\n/g' $payload
fi
