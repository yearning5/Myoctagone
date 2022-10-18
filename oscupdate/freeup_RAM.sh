#!/bin/bash
echo "Total memory is : "
echo $(free -m | grep m | awk '{print $2}') MB

echo "Free memory before freeing is : ";echo
echo $(free -m | grep m | awk '{print $4}') MB

sync; echo 3 > /proc/sys/vm/drop_caches
echo;echo "Free memory After freeing is : ";echo
echo $(free -m | grep m | awk '{print $4}') MB
