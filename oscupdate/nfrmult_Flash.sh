#!/bin/sh
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}

image=OpenATV-6.4.0
file=openatv-6.4-sf8008-backup-20210921_1243_usb.zip
echo "Copying File " $file " to tmp directory ......"
if [ -f /media/hdd/tmp/$file ]
then
rm /media/hdd/tmp/$file
fi 
cp /media/hdd/images/$file /media/hdd/tmp &&
echo "File " $file " copied to tmp directory with success"

cd /media/hdd/tmp
echo "Unzip  " $file " tmp directory"
unzip $file &&
echo "File " $file " Unzipped to tmp directory with success"
echo "Make directory  " $image " into $bb1/NFR4XBootI "
if [ -d $bb1/NFR4XBootI/$image ]
then
echo $image "already exists it will be deleted"
rm -Rf $bb1/NFR4XBootI/$image
fi 
mkdir $bb1/NFR4XBootI/$image
echo "Directory  " $image " Created into $bb1/NFR4XBootI "

echo "tar files needed   " $image 

tar -jxf /media/hdd/tmp/octagon/sf8008/rootfs.tar.bz2 -C $bb1/NFR4XBootI/$image &&
echo "Copying nucessary file needed   " $image 
cp -fr $bb1/NFR4XBootI/openatv-6.4/etc/network $bb1/NFR4XBootI/$image/etc/
cp -f $bb1/NFR4XBootI/openatv-6.4/etc/passwd $bb1/NFR4XBootI/$image/etc/
cp -f $bb1/NFR4XBootI/openatv-6.4/etc/shadow $bb1/NFR4XBootI/$image/etc/
cp -f $bb1/NFR4XBootI/openatv-6.4/etc/resolv.conf $bb1/NFR4XBootI/$image/
cp -f $bb1/NFR4XBootI/openatv-6.4/etc/wpa_supplicant.conf $bb1/NFR4XBootI/$image/etc/
cp -f $bb1/NFR4XBootI/openatv-6.4/etc/inadyn.conf $bb1/NFR4XBootI/$image/etc/


rm -Rf $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/HbbTV
echo "Copying directory  NFR4XBoot_client"
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/

cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client/.nfr4xboot_location $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client/.nfr4xboot_location
echo "Copying directory  DreamExplorer Plugin"
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/Hijri $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying directory  Hijri Plugin"
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/IMDbFNC $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying directory  IMDbFNC Plugin"
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/WeatherPlugin $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying directory  WeatherPlugin Plugin"
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying directory  IPTVPlayer Plugin"

cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/freearhey $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/LiveFootBall $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying directory  LiveFootBall Plugin"

cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/DreamExplorer $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
#echo "Copying directory  FileCommander Plugin"
#cp -R $bb1/openvix-5.3/usr/lib/enigma2/python/Plugins/Extensions/FileCommander  $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying channel list "
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.tv 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.radio 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb5 
rm -Rf $bb1/NFR4XBootI/$image/etc/tuxbox/satellites.xml
cp /etc/enigma2/*.tv $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.radio $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb5 $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/tuxbox/satellites.xml $bb1/NFR4XBootI/$image/etc/tuxbox/
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.tv 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.radio 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb5 
rm -Rf $bb1/NFR4XBootI/$image/etc/tuxbox/satellites.xml
cp /etc/enigma2/*.tv $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.radio $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb5 $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/tuxbox/satellites.xml $bb1/NFR4XBootI/$image/etc/tuxbox/
cp -R /etc/enigma2/weather_icons $bb1/NFR4XBootI/$image/etc/enigma2/
cp -R /etc/enigma2/weather_icons_special $bb1/NFR4XBootI/$image/etc/enigma2/
cp -R /etc/enigma2/xstreamity $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.json $bb1/NFR4XBootI/$image/etc/enigma2/
# set no case match
shopt -s nocasematch

if [[ $image == *"atv"* ]];then cp -f /etc/enigma2/MyMetrixLiteBackup.dat $bb1/NFR4XBootI/$image/etc/enigma2/ ; fi
# unset case match
shopt -u nocasematch
cp -Rf /etc/enigma2/xstreamity $bb1/NFR4XBootI/$image/etc/enigma2/

echo "channel list copied"

echo "copying /oscupdate..........."
cp -R /oscupdate $bb1/NFR4XBootI/$image/
cp -R /etc/cron $bb1/NFR4XBootI/$image/etc/


# ======       Openvix  =============
if [[ "${image,,}" =~ "vix" ]]; then
echo " VIX IMAGE SOFTCAMS COPYING"
#cp -R $bb1/NFR4XBootI/openvix-5.3/usr/softcams $bb1/NFR4XBootI/$image/usr/
cp -a /usr/bin/cam/. $bb1/NFR4XBootI/$image/usr/softcams/
#chmod 755 $bb1/NFR4XBootI/$image/usr/softcams/*.*
cp -R /etc/tuxbox/config $bb1/NFR4XBootI/$image/etc/tuxbox/
cp -f /etc/tuxbox/oscam-emu/*.* $bb1/NFR4XBootI/$image/etc/tuxbox/config
cp -f $bb1/NFR4XBootI/openvix-5.3/oscupdate/oscupdate.sh $bb1/NFR4XBootI/$image/oscupdate/
else
echo " NON VIX IMAGE SOFTCAMS COPYING"
cp -R /usr/bin/cam $bb1/NFR4XBootI/$image/usr/bin/
cp -R /etc/tuxbox $bb1/NFR4XBootI/$image/etc/
cp /etc/init.d/softcam.* $bb1/NFR4XBootI/$image/etc/init.d/
chmod 755 $bb1/NFR4XBootI/$image/etc/init.d/softcam.*
fi
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/OscamStatus $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/EPGImport $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/PermanentClock $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/PermanentEvent $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
echo "Copying VPNSetup Plugin..."
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/PKT_VPNSetup $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/etc/openvpn $bb1/NFR4XBootI/$image/etc/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/XStreamity $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/IPtoSAT $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/Prayertimes $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/Quran $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/Quran1 $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/FootOnSat $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/SquarDevise $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/TMBD $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -R $bb1/NFR4XBootI/openatv-6.4/usr/lib/enigma2/python/Plugins/Extensions/IPAudio $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
if [ -d $bb1/NFR4XBootI/$image/usr/script ]; then cp -f /usr/script/*.* $bb1/NFR4XBootI/$image/usr/script/ ;else echo "create directory" ;mkdir -p $bb1/NFR4XBootI/$image/usr/script ;cp -f /usr/script/*.* $bb1/NFR4XBootI/$image/usr/script/ ; fi


mkdir -p $bb1/NFR4XBootI/$image/media/usb
# softcams vix
#fstab
cp $bb1/NFR4XBootI/openatv-6.4/etc/fstab $bb1/NFR4XBootI/$image/etc/

rm $bb1/NFR4XBootI/$image/etc/init.d/tpmd

rm $bb1/NFR4XBootI/$image/etc/bhversion
