#!/bin/bash
python /oscupdate/freeiptvgen.py &&

file2cop="userbouquet.freeiptvgen__tv_.tv"
folder2cop="/etc/enigma2/"

printf "%s\n" $file2cop $folder2cop | /oscupdate/coy_fileall.sh

