#!/bin/bash
python /oscupdate/iptv-hls.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
