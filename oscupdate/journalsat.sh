##!/bin/sh
python /oscupdate/journatsat_yearning55.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2

file2cop="userbouquet.journalsat__tv_.tv"
folder2cop="/etc/enigma2/"

printf "%s\n %s\n"  $file2cop $folder2cop | /oscupdate/coy_fileall.sh
