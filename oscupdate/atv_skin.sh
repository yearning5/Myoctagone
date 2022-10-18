#!/bin/sh
str="sdb"
var1=$(df -h | grep $str)
IFS=' ' read -r -a array <<< $var1
bb=${array[-1]}
cp -f $bb/skin_infobar.mySkin.xml /usr/share/enigma2/MetrixHD/skinfiles
cp -f $bb/picon_default.png /usr/share/enigma2/MetrixHD/
cp -f $bb/folder.png /usr/share/enigma2/MetrixHD/icons
cp -f $bb/bootlogo.mvi /usr/share
