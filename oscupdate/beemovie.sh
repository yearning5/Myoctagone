#!/bin/bash
python /oscupdate/beemovie.py && wget -qO - http://127.0.0.1/web/servicelistreload?mode=2
