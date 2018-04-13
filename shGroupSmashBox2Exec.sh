#!/bin/bash
re="^[0-9]+$"
inicio=1
if  [[ "$1" =~ $re ]]; 
then
    for (( i=$inicio; i<=$1; i++ ))
    do
       docker run -d  --name "exec$i"  -h "exec$i"  -v /home/NB24146/smashbox2/saida:/saida python:smashbox2
    done
else
   echo "ERROR: PARAMETER MUST BE AN INTEGER - $1"
fi
