#!/bin/bash
python /oscupdate/bestbuy.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
