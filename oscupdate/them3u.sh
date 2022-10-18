##!/bin/sh
python /oscupdate/them3u.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
