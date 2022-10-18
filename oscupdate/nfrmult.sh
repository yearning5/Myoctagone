#!/bin/sh
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}

image=PurE2-6.5

extfolder=$bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
extlocal=/usr/lib/enigma2/python/Plugins/Extensions/
local=/
file=sf8008-PurE2-6.5-20220211_mmc.zip
echo "Copying File " $file " to tmp directory ......"
#if [ -f /tmp/$file ]
#then
#echo "File "$file"  already exists will be deleted " ; sleep 1
#rm /tmp/$file
#fi 
#cp $bb1/NFR4XBootUpload/$file /tmp &&
#echo "File " $file " copied to tmp directory with success"

#cd /tmp
cd $bb1/NFR4XBootUpload
echo "Unzip  " $file " tmp directory"
unzip -o $file &&
echo "File " $file " Unzipped to tmp directory with success"
echo "Make directory  " $image " into $bb1/NFR4XBootI "
if [ -d $bb1/NFR4XBootI/$image ];then echo $image "already exists it will be deleted"; sleep 2; rm -Rf $bb1/NFR4XBootI/$image  ;fi

echo $image "Has been deleted" ; sleep 2
echo "Directory  " $image " Will be Created into $bb1/NFR4XBootI " ; sleep 2
mkdir $bb1/NFR4XBootI/$image
echo "Directory  " $image " Created into $bb1/NFR4XBootI " ; sleep 2

echo "tar files needed   " $image 

tar -jxf $bb1/NFR4XBootUpload/octagon/sf8008/rootfs.tar.bz2 -C $bb1/NFR4XBootI/$image &&

rm -r $bb1/NFR4XBootUpload/octagon
echo "Copying nucessary file needed   " $image 
cp -fr /etc/network $bb1/NFR4XBootI/$image/etc/
cp -f /etc/passwd $bb1/NFR4XBootI/$image/etc/
cp -f /etc/shadow $bb1/NFR4XBootI/$image/etc/
cp -f /etc/resolv.conf $bb1/NFR4XBootI/$image/
cp -f /etc/wpa_supplicant.conf $bb1/NFR4XBootI/$image/etc/
cp -f /etc/wpa_supplicant.wlan0.conf  $bb1/NFR4XBootI/$image/etc/
cp -f /etc/inadyn.conf $bb1/NFR4XBootI/$image/etc/


rm -Rf $extfolder"HbbTV"
echo "Copying directory  NFR4XBoot_client"
if [[ "${image,,}" =~ "py3" ]]; then
echo "Python 3 Image   "; sleep 2
cp -R /media/usb/MetrixHDmod/pyth3/NFR4XBoot_client $extfolder

cp -R /media/usb/MetrixHDmod/pyth3/xtra/xtraEvent $extfolder
cp -R /media/usb/MetrixHDmod/pyth3/xtra/Converter/xtra* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/
cp -R /media/usb/MetrixHDmod/pyth3/xtra/Renderer/xtra* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer/
cp -R /media/usb/MetrixHDmod/xtra/xtra $bb1/NFR4XBootI/$image/usr/share/enigma2/

else
echo "Python 2 Image   "; sleep 2
cp -R /media/usb/MetrixHDmod/NFR4XBoot_client $extfolder

cp -R /media/usb/MetrixHDmod/xtra/xtraEvent $extfolder
cp -R /media/usb/MetrixHDmod/xtra/Converter/xtra* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/
cp -R /media/usb/MetrixHDmod/xtra/Renderer/xtra* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer/
cp -R /media/usb/MetrixHDmod/xtra/xtra $bb1/NFR4XBootI/$image/usr/share/enigma2/

fi
#cp -R /media/usb/MetrixHDmod/pyth3/NFR4XBoot_client/.nfr4xboot_location $extfolder"NFR4XBoot_client"/.nfr4xboot_location

echo "Copying Python 3 plugins ....." ; sleep 1

lis="Hijri FootOnSat IPAudio EPGImport IPtoSAT PermanentClock PermanentEvent Prayertimes Quran Quran1 Quran2 SubsSupport XStreamity"
if [[ "${image,,}" =~ "py3" ]]; then
echo "Python_3 Image   "; sleep 2
for line in $lis
do 
cp -R /media/usb/MetrixHDmod/pyth3/$line  $extfolder
echo $line" plugin has been copied ....." ; sleep 1
done
else
echo "Python_2 Image   "; sleep 2
for line in $lis
do 
cp -R $extlocal$line  $extfolder
echo $line" plugin has been copied ....." ; sleep 1
done
fi

echo "Copying channel list "

rm -fr $bb1/NFR4XBootI/$image/etc/enigma2/

cp -fR /etc/enigma2/ $bb1/NFR4XBootI/$image/etc/
cp -fR /media/usb/MetrixHDmod/epgimport $bb1/NFR4XBootI/$image/etc/
#export image
#export bb1
#bash /oscupdate/a-nfrmult.sh

# set no case match
shopt -s nocasematch

#if [[ $image == *"atv"* ]];then cp -f /etc/enigma2/MyMetrixLiteBackup.dat $bb1/NFR4XBootI/$image/etc/enigma2/ ; cp -f /usr/lib/enigma2/python/Components/Renderer/MetrixHDXPicon.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer; fi
# unset case match
shopt -u nocasematch
#cp -Rf /etc/enigma2/xstreamity $bb1/NFR4XBootI/$image/etc/enigma2/
echo "channel list copied"
echo "copying /oscupdate..........."
cp -R /media/usb/MetrixHDmod/oscupdate $bb1/NFR4XBootI/$image/
cp -R /media/usb/MetrixHDmod/cron $bb1/NFR4XBootI/$image/etc/
# ======       Openvix  =============
if [[ "${image,,}" =~ "vix" ]]; then
echo " VIX IMAGE SOFTCAMS COPYING"
#cp -R $bb1/NFR4XBootI/openvix-5.3/usr/softcams $bb1/NFR4XBootI/$image/usr/
cp -a /media/usb/MetrixHDmod/cam/. $bb1/NFR4XBootI/$image/usr/softcams/
#chmod 755 $bb1/NFR4XBootI/$image/usr/softcams/*.*
cp -R /etc/tuxbox/config $bb1/NFR4XBootI/$image/etc/tuxbox/
cp -f /etc/tuxbox/oscam-emu/*.* $bb1/NFR4XBootI/$image/etc/tuxbox/config
cp -f /media/usb/MetrixHDmod/vixoscupdate.sh $bb1/NFR4XBootI/$image/oscupdate/oscupdate.sh
chmod 755 $bb1/NFR4XBootI/$image/oscupdate/oscupdate.sh
elif [[ "${image,,}" =~ "hyperio" ]]; then
echo " Pkteam IMAGE SOFTCAMS COPYING"
cp -f /media/usb/MetrixHDmod/pktoscupdate.sh $bb1/NFR4XBootI/$image/oscupdate/oscupdate.sh
chmod 755 $bb1/NFR4XBootI/$image/oscupdate/oscupdate.sh
cp -f /etc/tuxbox/config/*.* $bb1/NFR4XBootI/$image/var/keys/
cp -f /etc/tuxbox/oscam-emu/*.* $bb1/NFR4XBootI/$image/var/keys/
cp -a /media/usb/MetrixHDmod/cam/. $bb1/NFR4XBootI/$image/var/emu
elif [[ "${image,,}" =~ "penbh" ]] || [[ "${image,,}" =~ "gami" ]]; then
echo " Openbh Or Egami IMAGE SOFTCAMS COPYING"
cp -R /media/usb/MetrixHDmod/cam $bb1/NFR4XBootI/$image/usr/bin/
cp -R /etc/tuxbox $bb1/NFR4XBootI/$image/etc/
if [[ "${image,,}" =~ "penbh" ]] ; then
echo " Openbh  IMAGE SOFTCAMS COPYING"
cp -R /media/usb/MetrixHDmod/camscript/*.* $bb1/NFR4XBootI/$image/usr/camscript
chmod 755 $bb1/NFR4XBootI/$image/usr/camscript/Ncam*
else
echo "Egami IMAGE SOFTCAMS COPYING"
cp -R /media/usb/MetrixHDmod/camscript/*.* $bb1/NFR4XBootI/$image/usr/emu_scripts
rename  Ncam EGcam $bb1/NFR4XBootI/$image/usr/emu_scripts/*.sh
chmod 755 $bb1/NFR4XBootI/$image/usr/emu_scripts/EGcam*
fi
else
echo " NON VIX Or PKTeam IMAGE SOFTCAMS COPYING"
cp -R /media/usb/MetrixHDmod/cam $bb1/NFR4XBootI/$image/usr/bin/
cp -R /etc/tuxbox $bb1/NFR4XBootI/$image/etc/
cp /etc/init.d/softcam.* $bb1/NFR4XBootI/$image/etc/init.d/
chmod 755 $bb1/NFR4XBootI/$image/etc/init.d/softcam.*
fi
if [ -d $bb1/NFR4XBootI/$image/usr/script ]; then cp -f /usr/script/*.* $bb1/NFR4XBootI/$image/usr/script/ ;else echo "create directory" ;mkdir -p $bb1/NFR4XBootI/$image/usr/script ;cp -f /usr/script/*.* $bb1/NFR4XBootI/$image/usr/script/ ; fi
mkdir -p $bb1/NFR4XBootI/$image/media/usb
# softcams vix
#fstab
cp /etc/fstab $bb1/NFR4XBootI/$image/etc/
rm $bb1/NFR4XBootI/$image/etc/init.d/tpmd
rm $bb1/NFR4XBootI/$image/etc/bhversion
cp -r /etc/samba/ $bb1/NFR4XBootI/$image/etc/
# ====================== MetrixHD Skin ===============
if [[ ! "${image,,}" =~ "atv" ]]; then
echo " COPYING MetrixHD Skin " ; sleep 1

cp -R /media/usb/MetrixHDmod/MetrixHD $bb1/NFR4XBootI/$image/usr/share/enigma2/
echo " COPYING MetrixHD Skin Converters " ; sleep 1
if [[ "${image,,}" =~ "py3" ]]; then
echo "Python_3 Image   "; sleep 2
cp -R /media/usb/MetrixHDmod/pyth3/Converter/*.py* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/
echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R /media/usb/MetrixHDmod/pyth3/Renderer/*.py* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R /media/usb/MetrixHDmod/pyth3/MyMetrixLite $extfolder
cp -R /media/usb/MetrixHDmod/pyth3/AutoBouquetsMaker $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R /media/usb/FileCommander $extfolder; fi
cp -R /media/usb/MetrixHDmod/pyth3/My_ScriptRunner $extfolder

#cp -R /media/usb/MetrixHDmod/poster/*.png $bb1/NFR4XBootI/$image/usr/share/
cp -R /media/usb/MetrixHDmod/pyth3/Converter/RouteInfo.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/

else
echo "Python_2 Image   "; sleep 2

cp -R /media/usb/MetrixHDmod/Converter/*.py* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/

echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R /media/usb/MetrixHDmod/Renderer/*.py* $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R /media/usb/MetrixHDmod/MyMetrixLite $extfolder
cp -R /media/usb/MetrixHDmod/AutoBouquetsMaker $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R /media/usb/FileCommander $extfolder; fi
cp -R /media/usb/MetrixHDmod/My_ScriptRunner $extfolder

#cp -R /media/usb/MetrixHDmod/poster/*.png $bb1/NFR4XBootI/$image/usr/share/
cp -R /media/usb/MetrixHDmod/Converter/RouteInfo.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/

fi
fi
cp  /media/usb/MetrixHDmod/Renderer/fhdlPoster.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Renderer/
cp  /media/usb/MetrixHDmod/Converter/mypic.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/
cp  /media/usb/MetrixHDmod/Converter/Kitte888infoMovie.py $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Components/Converter/