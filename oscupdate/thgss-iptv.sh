#!/bin/bash
python /oscupdate/thgss-iptv.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
