#!/bin/sh
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}

dev_null = ' > /dev/null 2>&1'
image=sf8008-PurE2-6.51
extfolder=$bb1/ImageBoot/$image/usr/lib/enigma2/python/Plugins/Extensions/
extlocal=/usr/lib/enigma2/python/Plugins/Extensions/
local=/
MEDIA="/media/hdd1/."



echo "Copying nucessary file needed   " $image 
cp -fr ${MEDIA}MetrixHDmod/conne/network /etc/
cp -f ${MEDIA}MetrixHDmod/conne/passwd /etc/
cp -f ${MEDIA}MetrixHDmod/conne/shadow /etc/
cp -f ${MEDIA}MetrixHDmod/conne/resolv.conf /etc/
cp -f ${MEDIA}MetrixHDmod/conne/wpa_supplicant.conf /etc/
cp -f ${MEDIA}MetrixHDmod/conne/wpa_supplicant.wlan0.conf  /etc/
cp -f ${MEDIA}MetrixHDmod/conne/inadyn.conf /etc/

echo "Repair ftp service "

sed -i 's/listen=NO/listen=YES/' /etc/vsftpd.conf
sed -i 's/listen_ipv6=YES/listen_ipv6=NO/' /etc/vsftpd.conf


a=$(ls /usr/lib/)


if [[ "${a,,}" =~ "python3" ]]; then
echo "Python 3 Image   "; sleep 2
#cp -R ${MEDIA}MetrixHDmod/pyth3/NFR4XBoot_client $extfolder

cp -R ${MEDIA}MetrixHDmod/pyth3/xtra/xtraEvent /usr/lib/enigma2/python/Plugins/Extensions/
cp -R ${MEDIA}MetrixHDmod/pyth3/xtra/Converter/xtra* /usr/lib/enigma2/python/Components/Converter/
cp -R ${MEDIA}MetrixHDmod/pyth3/xtra/Renderer/xtra* /usr/lib/enigma2/python/Components/Renderer/
cp -R ${MEDIA}MetrixHDmod/xtra/xtra /usr/share/enigma2/

else
echo "Python 2 Image   "; sleep 2
#cp -R ${MEDIA}MetrixHDmod/NFR4XBoot_client $extfolder

cp -R ${MEDIA}MetrixHDmod/xtra/xtraEvent /usr/lib/enigma2/python/Plugins/Extensions/
cp -R ${MEDIA}MetrixHDmod/xtra/Converter/xtra* /usr/lib/enigma2/python/Components/Converter/
cp -R ${MEDIA}MetrixHDmod/xtra/Renderer/xtra* /usr/lib/enigma2/python/Components/Renderer/
cp -R ${MEDIA}MetrixHDmod/xtra/xtra /usr/share/enigma2/

fi
#cp -R ${MEDIA}MetrixHDmod/pyth3/NFR4XBoot_client/.nfr4xboot_location $extfolder"NFR4XBoot_client"/.nfr4xboot_location



lis="AJPan Hijri Quran2 MultiStalker IPTVPlayer HistoryZapSelector SubsSupport PermanentCaid OscamStatus TMBD  PermanentClock  DreamExplorer IPtoSAT PermanentEvent WeatherPlugin EPGImport LiveFootBall   XStreamity FileCommander Prayertimes  FootOnSat MyMetrixLite Quran  My_ScriptRunner Quran1"

if [[ "${a,,}" =~ "python3" ]]; then
echo "Python_3 Image   "; sleep 2
echo "Copying Python 3 plugins ....." ; sleep 1
for line in $lis
do 
cp -R ${MEDIA}MetrixHDmod/pyth3/$line  $extlocal
echo $line" plugin has been copied ....." ; sleep 1
done
else
echo "Python_2 Image   "; sleep 2
echo "Copying Python 2 plugins ....." ; sleep 1
for line in $lis
do 
cp -R $extfolder$line  $extlocal
echo $line" plugin has been copied ....." ; sleep 1
done
fi
cp ${MEDIA}stalker.conf /home/
echo "Copying channel list "

rm -fr /etc/enigma2/*

cp -fR ${MEDIA}chlist/* /etc/enigma2/ 
#cp -fR ${MEDIA}MetrixHDmod/epgimport $bb1/ImageBoot/$image/etc/
#export image
#export bb1
#bash /oscupdate/a-nfrmult.sh

# set no case match
shopt -s nocasematch

#if [[ $image == *"atv"* ]];then cp -f /etc/enigma2/MyMetrixLiteBackup.dat $bb1/ImageBoot/$image/etc/enigma2/ ; cp -f /usr/lib/enigma2/python/Components/Renderer/MetrixHDXPicon.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer; fi
# unset case match
shopt -u nocasematch
#cp -Rf /etc/enigma2/xstreamity $bb1/ImageBoot/$image/etc/enigma2/
echo "channel list copied"
echo "copying /oscupdate..........."
cp -R ${MEDIA}MetrixHDmod/oscupdate /
cp -R ${MEDIA}MetrixHDmod/cron /etc/
# ======       Openvix  =============
if [[ "$(grep "."  /etc/issue | tail -1)" =~ "vix" ]]; then
echo " VIX IMAGE SOFTCAMS COPYING"
#cp -R $bb1/ImageBoot/openvix-5.3/usr/softcams $bb1/ImageBoot/$image/usr/
cp -a ${MEDIA}MetrixHDmod/cam/. /usr/softcams/
#chmod 755 $bb1/ImageBoot/$image/usr/softcams/*.*
cp -R /etc/tuxbox/config /etc/tuxbox/
cp -f /etc/tuxbox/oscam-emu/*.* /etc/tuxbox/config
cp -f ${MEDIA}MetrixHDmod/vixoscupdate.sh /oscupdate/oscupdate.sh
chmod 755 /oscupdate/oscupdate.sh
elif [[ "$(grep "."  /etc/issue | tail -1)" =~ "hyperio" ]]; then
echo " Pkteam IMAGE SOFTCAMS COPYING"
cp -f ${MEDIA}MetrixHDmod/pktoscupdate.sh /oscupdate/oscupdate.sh
chmod 755 /oscupdate/oscupdate.sh
cp -f ${MEDIA}MetrixHDmod/tuxbox/config/*.* /var/keys/
cp -f ${MEDIA}MetrixHDmod/tuxbox//oscam-emu/*.* /var/keys/
cp -a ${MEDIA}MetrixHDmod/cam/. /var/emu
elif [[ "$(grep "."  /etc/issue | tail -1)" =~ "pure2" ]] ; then
echo " Pure2 IMAGE SOFTCAMS COPYING"
cp -r ${MEDIA}MetrixHDmod/Puer2scripts/cam /usr/script
cp ${MEDIA}MetrixHDmod/cam/* /usr/bin/cam/
chmod 755 /usr/script/cam/*
chmod 755 /usr/bin/cam/*

elif [[ "$(grep "."  /etc/issue | tail -1)" =~ "penbh" ]] || [[ "$(grep "."  /etc/issue | tail -1)" =~ "gami" ]]; then
echo " Openbh Or Egami IMAGE SOFTCAMS COPYING"
cp -R ${MEDIA}MetrixHDmod/cam /usr/bin/
cp -R ${MEDIA}MetrixHDmod/tuxbox /etc/
if [[ "$(grep "."  /etc/issue | tail -1)" =~ "penbh" ]] ; then
echo " Openbh  IMAGE SOFTCAMS COPYING"
cp -R ${MEDIA}MetrixHDmod/camscript/*.* /usr/camscript
chmod 755 /usr/camscript/Ncam*
else
echo "Egami IMAGE SOFTCAMS COPYING"
cp -R ${MEDIA}MetrixHDmod/camscript/*.* /usr/emu_scripts
rename  Ncam EGcam /usr/emu_scripts/*.sh
chmod 755 /usr/emu_scripts/EGcam*
fi
else
echo " NON VIX Or PKTeam IMAGE SOFTCAMS COPYING"
cp -R ${MEDIA}MetrixHDmod/cam /usr/bin/
cp -R ${MEDIA}MetrixHDmod/tuxbox /etc/
cp  ${MEDIA}MetrixHDmod/atvscript/* /etc/init.d/
chmod 755 /etc/init.d/softcam.*
fi
if [ -d /usr/script ]; then cp -f ${MEDIA}MetrixHDmod/scripts/*.* /usr/script/ ;else echo "create directory" ;mkdir -p /usr/script ;cp -f ${MEDIA}MetrixHDmod/scripts/*.* /usr/script/ ; fi

# softcams vix
#fstab
cp ${MEDIA}MetrixHDmod/fstab /etc/
# ====================== MetrixHD Skin ===============
if [[ ! "$(grep "."  /etc/issue | tail -1)" =~ "atv" ]]; then
echo " COPYING MetrixHD Skin " ; sleep 1

cp -R ${MEDIA}MetrixHDmod/MetrixHD /usr/share/enigma2/
echo " COPYING MetrixHD Skin Converters " ; sleep 1
if [[ "${a,,}" =~ "python3" ]]; then
echo "Python_3 Image   "; sleep 2
cp -R ${MEDIA}MetrixHDmod/pyth3/Converter/*.py* /usr/lib/enigma2/python/Components/Converter/
echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R ${MEDIA}MetrixHDmod/pyth3/Renderer/*.py* /usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R ${MEDIA}MetrixHDmod/pyth3/MyMetrixLite $extlocal
cp -R ${MEDIA}MetrixHDmod/pyth3/AutoBouquetsMaker /usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R ${MEDIA}FileCommander $extfolder; fi
cp -R ${MEDIA}MetrixHDmod/pyth3/My_ScriptRunner $extlocal

#cp -R ${MEDIA}MetrixHDmod/poster/*.png $bb1/ImageBoot/$image/usr/share/
cp -R ${MEDIA}MetrixHDmod/pyth3/Converter/RouteInfo.py /usr/lib/enigma2/python/Components/Converter/

else
echo "Python_2 Image   "; sleep 2

cp -R ${MEDIA}MetrixHDmod/Converter/*.py* /usr/lib/enigma2/python/Components/Converter/

echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R ${MEDIA}MetrixHDmod/Renderer/*.py* /usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R ${MEDIA}MetrixHDmod/MyMetrixLite $extlocal
cp -R ${MEDIA}MetrixHDmod/AutoBouquetsMaker /usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R ${MEDIA}FileCommander $extfolder; fi
cp -R ${MEDIA}MetrixHDmod/My_ScriptRunner $extlocal

#cp -R ${MEDIA}MetrixHDmod/poster/*.png $bb1/ImageBoot/$image/usr/share/
cp -R ${MEDIA}MetrixHDmod/Converter/RouteInfo.py /usr/lib/enigma2/python/Components/Converter/

fi
fi
cp  ${MEDIA}MetrixHDmod/Renderer/fhdlPoster.py /usr/lib/enigma2/python/Components/Renderer/
cp  ${MEDIA}MetrixHDmod/Converter/mypic.py /usr/lib/enigma2/python/Components/Converter/
cp  ${MEDIA}MetrixHDmod/Converter/Kitte888infoMovie.py /usr/lib/enigma2/python/Components/Converter/
cp -r ${MEDIA}MetrixHDmod/psatars /usr/share/enigma2/