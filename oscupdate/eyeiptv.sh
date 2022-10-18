#!/bin/bash
python /oscupdate/eyeiptv.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2 &&

file2cop="userbouquet.eye_3days__tv_.tv"
folder2cop="/etc/enigma2/"

printf "%s\n" $file2cop $folder2cop | /oscupdate/coy_file.sh