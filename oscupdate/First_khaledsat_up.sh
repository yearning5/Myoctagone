#!/bin/bash
if ping -q -c 1 -W 1 google.com >/dev/null; then
echo "The network is up ...proceed with free CCCAM Updater.."
python /oscupdate/First_khaledsat_up.py && 
if (( $(ps -ef | grep -v grep | grep boscam | wc -l) > 0 ))
then
service=boscam
killall -9 $service
startcam='/usr/softcams/boscam -b &'
elif (( $(ps -ef | grep -v grep | grep gcam.arm | wc -l) > 0 ))
then
service=gcam.arm
killall -9 $service
startcam='/usr/softcams/gcam.arm -b &'
elif (( $(ps -ef | grep -v grep | grep ncam | wc -l) > 0 ))
then
service=ncam
killall -9 $service
startcam='/usr/softcams/ncam -b &'
elif (( $(ps -ef | grep -v grep | grep oscam_emu | wc -l) > 0 ))
then
service=oscam_emu
killall -9 $service
startcam='/usr/softcams/oscam_emu -b'
elif (( $(ps -ef | grep -v grep | grep oscammodern | wc -l) > 0 ))
then
service=oscammodern
killall -9 $service
startcam='/usr/softcams/oscammodern -b'
elif (( $(ps -ef | grep -v grep | grep wicardd19 | wc -l) > 0 ))
then
service=wicardd19
killall -9 $service
startcam='/usr/softcams/wicardd19 -d'
else
startcam='/usr/softcams/oscam_emu -b'
fi
$startcam
else
echo "The network is down"
if (( $(ps -ef | grep -v grep | grep boscam | wc -l) > 0 ))
then
service=boscam
killall -9 $service
startcam='/usr/softcams/boscam -b &'
elif (( $(ps -ef | grep -v grep | grep gcam.arm | wc -l) > 0 ))
then
service=gcam.arm
killall -9 $service
startcam='/usr/softcams/gcam.arm -b &'
elif (( $(ps -ef | grep -v grep | grep ncam | wc -l) > 0 ))
then
service=ncam
killall -9 $service
startcam='/usr/softcams/ncam -b &'
elif (( $(ps -ef | grep -v grep | grep oscam_emu | wc -l) > 0 ))
then
service=oscam_emu
killall -9 $service
startcam='/usr/softcams/oscam_emu -b'
elif (( $(ps -ef | grep -v grep | grep oscammodern | wc -l) > 0 ))
then
service=oscammodern
killall -9 $service
startcam='/usr/softcams/oscammodern -b'
elif (( $(ps -ef | grep -v grep | grep wicardd19 | wc -l) > 0 ))
then
service=wicardd19
killall -9 $service
startcam='/usr/softcams/wicardd19 -d'
else
startcam='/usr/softcams/oscam_emu -b'
fi
$startcam
fi


python /oscupdate/copy_oscam.py