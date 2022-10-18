#!/bin/bash
wget --no-check-certificate "https://gitlab.com/Rgysoft/iptv-host-e2iplayer/-/archive/master/iptv-host-e2iplayer-master.zip" -O /tmp/iptv.zip && unzip /tmp/iptv.zip -d /tmp/ && cp -rf /tmp/iptv-host-e2iplayer*/IPTVPlayer /usr/lib/enigma2/python/Plugins/Extensions
killall -9 enigma2
