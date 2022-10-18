#!/bin/bash
echo  "Please enter FILE NAME with full path : \n"
read file
sed -i -e 's/\r//g' $file