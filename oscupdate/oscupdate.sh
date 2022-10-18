#!/bin/bash
if ping -q -c 1 -W 1 google.com >/dev/null; then
echo "The network is up ...proceed with free CCCAM Updater.."
python /oscupdate/oscupdate.py && 

#service=$(ps -ef | grep -v grep | grep cam | tail -1 |  tr -s " " | cut -d " " -f 8-)
service=$(ps -ef | grep -v grep | grep cam | tail -1 |  tr -s " " | cut -d " " -f 8- | sed  's/ --daemon//g' )

if (( $(ps -ef | grep -v grep | grep cam | wc -l) > 0 ))
then
echo "------------------"
echo "killing the process ....."
echo "...  $service    ...." 
echo "------------------"

ps -ef | grep -v grep | grep cam | tail -1 | awk {'print $2'} | xargs  kill -9

echo "------------------"
echo "Starting the process ....."
echo "...  $service    ...." 
echo "------------------"
startcam=$service
else
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
fi
$startcam --daemon

else
echo "The network is down"
if (( $(ps -ef | grep -v grep | grep cam | wc -l) > 0 ))
then

echo "------------------"
echo "killing the process ....."
echo 
echo "...  $service    ...." 
echo
echo "------------------"

ps -ef | grep -v grep | grep cam | tail -1 | awk {'print $2'} | xargs  kill -9

echo "------------------"
echo "Starting the process ....."
echo 
echo "...  $service    ...." 
echo
echo "------------------"
startcam=$service
else
startcam='/usr/bin/cam/oscam_emu -b -r 2 -c /etc/tuxbox/oscam-emu'
fi
$startcam --daemon
fi

python /oscupdate/copy_oscam.py