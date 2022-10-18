#!/bin/bash
init 4
cd /tmp
rm -rf *.ipk
wget --no-check-certificate -O e2ip.zip https://gitlab.com/mosz_nowy/e2iplayer/-/archive/master/e2iplayer-master.zip
unzip -d /tmp e2ip.zip
rm -rf *.zip
/bin/cp -Rdf /tmp/e2iplayer-master/IPTVPlayer/* /usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/
rm -rf /tmp/e2iplayer-master
sync
opkg update
opkg remove enigma2-plugin-extensions-serviceapp exteplayer3 ffmpeg
opkg install ffmpeg exteplayer3 enigma2-plugin-systemplugins-serviceapp
cd /usr/bin
ln -s gstplayer gstplayer_gst-1.0
opkg install gstplayer
reboot