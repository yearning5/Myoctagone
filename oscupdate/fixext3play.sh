#!/bin/bash
opkg update
python /oscupdate/ffinstall.py
killall -9 enigma2