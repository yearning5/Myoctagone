#!/bin/bash
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
service=0
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
fi
if [ "$service" = "0" ]
then
echo "There were no Cam running And Oscam_emu will be started"
sleep 3
service=oscam_emu
$startcam
else
echo "$service was running and killed"
sleep 3
echo "Now starting $service"
sleep 3
fi
echo " $service Started Successfully"
