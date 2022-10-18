#!/bin/bash
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}

init 4 
rm -rf /tmp/channels 
mkdir /tmp/channels 
cp $bb/.backup/channels_b/* /tmp/channels/ 
cp $bb1/.backup/channels_b/* /tmp/channels/
rm -rf /etc/enigma2/*.tv /etc/enigma2/*.radio /etc/enigma2/lamedb /etc/enigma2/lamedb5 /etc/tuxbox/satellites.xml
cp /tmp/channels/*.tv /etc/enigma2/
cp /tmp/channels/*.radio /etc/enigma2/
cp /tmp/channels/lamedb /etc/enigma2/
cp /tmp/channels/lamedb5 /etc/enigma2/
cp /tmp/channels/satellites.xml /etc/tuxbox/satellites.xml
sed -i -e '/config.Nims/d' /etc/enigma2/settings
awk '/config.Nims/' /tmp/channels/diseqcayar.txt >> /etc/enigma2/settings
init 3
