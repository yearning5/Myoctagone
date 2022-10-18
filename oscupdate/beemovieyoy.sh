#!/bin/bash

rm /tmp/beemovieyoy.txt
echo $(date +"%T") >> /tmp/beemovieyoy.txt

python /oscupdate/beemovieyoy.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2 &&


file2cop="userbouquet.nilesat__tv_.tv"
folder2cop="/etc/enigma2/"

printf "%s\n %s\n" $file2cop $folder2cop | /oscupdate/coy_fileall.sh