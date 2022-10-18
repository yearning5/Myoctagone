#!/bin/bash
if ping -q -c 1 -W 1 google.com >/dev/null; then
echo "The network is up ...proceed with free CCCAM Updater.."
python /oscupdate/khaledsat_up.py && 
if (( $(ps -ef | grep -v grep | grep boscam | wc -l) > 0 ))
then
service=boscam
killall -9 $service
startcam='/usr/bin/cam/boscam -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep gcam.arm | wc -l) > 0 ))
then
service=gcam.arm
killall -9 $service
startcam='/usr/bin/cam/gcam.arm -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep ncam | wc -l) > 0 ))
then
service=ncam
killall -9 $service
startcam='/usr/bin/cam/ncam -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep oscam_emu | wc -l) > 0 ))
then
service=oscam_emu
killall -9 $service
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
elif (( $(ps -ef | grep -v grep | grep oscammodern | wc -l) > 0 ))
then
service=oscammodern
killall -9 $service
startcam='/usr/bin/cam/oscammodern -b -r 2 -c /etc/tuxbox/oscammodern'
elif (( $(ps -ef | grep -v grep | grep wicardd19 | wc -l) > 0 ))
then
service=wicardd19
killall -9 $service
startcam='/usr/bin/cam/wicardd19 -d -c  /etc/tuxbox/config/wicardd.conf'
else
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
fi
$startcam
else
echo "The network is down"
if (( $(ps -ef | grep -v grep | grep boscam | wc -l) > 0 ))
then
service=boscam
killall -9 $service
startcam='/usr/bin/cam/boscam -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep gcam.arm | wc -l) > 0 ))
then
service=gcam.arm
killall -9 $service
startcam='/usr/bin/cam/gcam.arm -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep ncam | wc -l) > 0 ))
then
service=ncam
killall -9 $service
startcam='/usr/bin/cam/ncam -c /etc/tuxbox/config &'
elif (( $(ps -ef | grep -v grep | grep oscam_emu | wc -l) > 0 ))
then
service=oscam_emu
killall -9 $service
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
elif (( $(ps -ef | grep -v grep | grep oscammodern | wc -l) > 0 ))
then
service=oscammodern
killall -9 $service
startcam='/usr/bin/cam/oscammodern -b -r 2 -c /etc/tuxbox/oscammodern'
elif (( $(ps -ef | grep -v grep | grep wicardd19 | wc -l) > 0 ))
then
service=wicardd19
killall -9 $service
startcam='/usr/bin/cam/wicardd19 -d -c  /etc/tuxbox/config/wicardd.conf'
else
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
fi
$startcam
fi

python /oscupdate/copy_oscam.py