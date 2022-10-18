#!/bin/bash
python /oscupdate/iptv.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
