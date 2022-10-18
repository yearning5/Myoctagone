#!/bin/bash
if (( $(ps -ef | grep -v grep | grep oscam_emu | wc -l) > 0 ))
then
service=oscam_emu
killall -9 $service
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
$startcam
fi