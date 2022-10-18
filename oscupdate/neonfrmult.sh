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
image=Openspa-8
extfolder=$bb1/ImageBoot/$image/usr/lib/enigma2/python/Plugins/Extensions/
extlocal=/usr/lib/enigma2/python/Plugins/Extensions/
local=/
file=openspa-8.0.001-sf8008-20220612_mmc.zip
cd $bb1/ImagesUpload
echo "Unzip  " $file " tmp directory"
unzip -o $file &&
echo "File " $file " Unzipped  with success"
echo "Make directory  " $image " into $bb1/ImageBoot "
if [ -d $bb1/ImageBoot/$image ];then echo $image "already exists it will be deleted"; sleep 2; rm -Rf $bb1/ImageBoot/$image  ;fi

echo $image "Has been deleted" ; sleep 2
echo "Directory  " $image " Will be Created into $bb1/ImageBoot " ; sleep 2
mkdir $bb1/ImageBoot/$image
echo "Directory  " $image " Created into $bb1/ImageBoot " ; sleep 2

echo "tar files needed   " $image 

tar -jxf $bb1/ImagesUpload/octagon/sf8008/rootfs.tar.bz2 -C $bb1/ImageBoot/$image &&

rm -r $bb1/ImagesUpload/octagon
echo "Creating Neoboot file for Multiboot info "; sleep 2
rm $bb1/ImageBoot/$image/.multinfo
echo $image > $bb1/ImageBoot/$image/.multinfo
rm $bb1/ImageBoot/$image/.data
tr=$(date +'%m.%d.%Y - %T')
echo  "image installation time "$tr >> $bb1/ImageBoot/$image/.data
rm $bb1/ImageBoot/$image/.control_ok
echo -e  "image start OK\ndo not delete this file!" >> $bb1/ImageBoot/$image/.control_ok

echo "Copying nucessary file needed   " $image 
cp -fr /etc/network $bb1/ImageBoot/$image/etc/
cp -f /etc/passwd $bb1/ImageBoot/$image/etc/
cp -f /etc/shadow $bb1/ImageBoot/$image/etc/
cp -f /etc/resolv.conf $bb1/ImageBoot/$image/
cp -f /etc/wpa_supplicant.conf $bb1/ImageBoot/$image/etc/
cp -f /etc/wpa_supplicant.wlan0.conf  $bb1/ImageBoot/$image/etc/
cp -f /etc/inadyn.conf $bb1/ImageBoot/$image/etc/

echo "Repair ftp service "

sed -i 's/listen=NO/listen=YES/' $bb1/ImageBoot/$image/etc/vsftpd.conf
sed -i 's/listen_ipv6=YES/listen_ipv6=NO/' $bb1/ImageBoot/$image/etc/vsftpd.conf

#echo "Copying directory  Neoboot"

cp -rf /media/hdd1/NeoBoot  $extfolder $dev_null
a=$(ls $bb1/ImageBoot/$image/usr/lib/)


if [[ "${a,,}" =~ "python3" ]]; then
echo "Python 3 Image   "; sleep 2
#cp -R /media/hdd1/.MetrixHDmod/pyth3/NFR4XBoot_client $extfolder

cp -R /media/hdd1/.MetrixHDmod/pyth3/xtra/xtraEvent $extfolder
cp -R /media/hdd1/.MetrixHDmod/pyth3/xtra/Converter/xtra* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/
cp -R /media/hdd1/.MetrixHDmod/pyth3/xtra/Renderer/xtra* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer/
cp -R /media/hdd1/.MetrixHDmod/xtra/xtra $bb1/ImageBoot/$image/usr/share/enigma2/

else
echo "Python 2 Image   "; sleep 2
#cp -R /media/hdd1/.MetrixHDmod/NFR4XBoot_client $extfolder

cp -R /media/hdd1/.MetrixHDmod/xtra/xtraEvent $extfolder
cp -R /media/hdd1/.MetrixHDmod/xtra/Converter/xtra* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/
cp -R /media/hdd1/.MetrixHDmod/xtra/Renderer/xtra* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer/
cp -R /media/hdd1/.MetrixHDmod/xtra/xtra $bb1/ImageBoot/$image/usr/share/enigma2/

fi
#cp -R /media/hdd1/.MetrixHDmod/pyth3/NFR4XBoot_client/.nfr4xboot_location $extfolder"NFR4XBoot_client"/.nfr4xboot_location



lis="AJPan Hijri Quran2 MultiStalker IPTVPlayer HistoryZapSelector SubsSupport PermanentCaid OscamStatus TMBD  PermanentClock  DreamExplorer IPtoSAT PermanentEvent WeatherPlugin EPGImport LiveFootBall   XStreamity FileCommander Prayertimes  FootOnSat MyMetrixLite Quran  My_ScriptRunner Quran1"

if [[ "${a,,}" =~ "python3" ]]; then
echo "Python_3 Image   "; sleep 2
echo "Copying Python 3 plugins ....." ; sleep 1
for line in $lis
do 
cp -R /media/hdd1/.MetrixHDmod/pyth3/$line  $extfolder
echo $line" plugin has been copied ....." ; sleep 1
done
else
echo "Python_2 Image   "; sleep 2
echo "Copying Python 2 plugins ....." ; sleep 1
for line in $lis
do 
cp -R $extlocal$line  $extfolder
echo $line" plugin has been copied ....." ; sleep 1
done
fi
cp /media/hdd1/.stalker.conf $bb1/ImageBoot/$image/home/
echo "Copying channel list "

rm -fr $bb1/ImageBoot/$image/etc/enigma2/

cp -fR /etc/enigma2/ $bb1/ImageBoot/$image/etc/
#cp -fR /media/hdd1/.MetrixHDmod/epgimport $bb1/ImageBoot/$image/etc/
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
cp -R /media/hdd1/.MetrixHDmod/oscupdate $bb1/ImageBoot/$image/
cp -R /media/hdd1/.MetrixHDmod/cron $bb1/ImageBoot/$image/etc/
# ======       Openvix  =============
if [[ "${image,,}" =~ "vix" ]]; then
echo " VIX IMAGE SOFTCAMS COPYING"
#cp -R $bb1/ImageBoot/openvix-5.3/usr/softcams $bb1/ImageBoot/$image/usr/
cp -a /media/hdd1/.MetrixHDmod/cam/. $bb1/ImageBoot/$image/usr/softcams/
#chmod 755 $bb1/ImageBoot/$image/usr/softcams/*.*
cp -R /etc/tuxbox/config $bb1/ImageBoot/$image/etc/tuxbox/
cp -f /etc/tuxbox/oscam-emu/*.* $bb1/ImageBoot/$image/etc/tuxbox/config
cp -f /media/hdd1/.MetrixHDmod/vixoscupdate.sh $bb1/ImageBoot/$image/oscupdate/oscupdate.sh
chmod 755 $bb1/ImageBoot/$image/oscupdate/oscupdate.sh
elif [[ "${image,,}" =~ "hyperio" ]]; then
echo " Pkteam IMAGE SOFTCAMS COPYING"
cp -f /media/hdd1/.MetrixHDmod/pktoscupdate.sh $bb1/ImageBoot/$image/oscupdate/oscupdate.sh
chmod 755 $bb1/ImageBoot/$image/oscupdate/oscupdate.sh
cp -f /etc/tuxbox/config/*.* $bb1/ImageBoot/$image/var/keys/
cp -f /etc/tuxbox/oscam-emu/*.* $bb1/ImageBoot/$image/var/keys/
cp -a /media/hdd1/.MetrixHDmod/cam/. $bb1/ImageBoot/$image/var/emu
elif [[ "${image,,}" =~ "penbh" ]] || [[ "${image,,}" =~ "gami" ]]; then
echo " Openbh Or Egami IMAGE SOFTCAMS COPYING"
cp -R /media/hdd1/.MetrixHDmod/cam $bb1/ImageBoot/$image/usr/bin/
cp -R /etc/tuxbox $bb1/ImageBoot/$image/etc/
if [[ "${image,,}" =~ "penbh" ]] ; then
echo " Openbh  IMAGE SOFTCAMS COPYING"
cp -R /media/hdd1/.MetrixHDmod/camscript/*.* $bb1/ImageBoot/$image/usr/camscript
chmod 755 $bb1/ImageBoot/$image/usr/camscript/Ncam*
else
echo "Egami IMAGE SOFTCAMS COPYING"
cp -R /media/hdd1/.MetrixHDmod/camscript/*.* $bb1/ImageBoot/$image/usr/emu_scripts
rename  Ncam EGcam $bb1/ImageBoot/$image/usr/emu_scripts/*.sh
chmod 755 $bb1/ImageBoot/$image/usr/emu_scripts/EGcam*
fi
else
echo " NON VIX Or PKTeam IMAGE SOFTCAMS COPYING"
cp -R /media/hdd1/.MetrixHDmod/cam $bb1/ImageBoot/$image/usr/bin/
cp -R /etc/tuxbox $bb1/ImageBoot/$image/etc/
cp /etc/init.d/softcam.* $bb1/ImageBoot/$image/etc/init.d/
chmod 755 $bb1/ImageBoot/$image/etc/init.d/softcam.*
fi
if [ -d $bb1/ImageBoot/$image/usr/script ]; then cp -f /usr/script/*.* $bb1/ImageBoot/$image/usr/script/ ;else echo "create directory" ;mkdir -p $bb1/ImageBoot/$image/usr/script ;cp -f /usr/script/*.* $bb1/ImageBoot/$image/usr/script/ ; fi
mkdir -p $bb1/ImageBoot/$image/media/usb
# softcams vix
#fstab
cp /etc/fstab $bb1/ImageBoot/$image/etc/
rm $bb1/ImageBoot/$image/etc/init.d/tpmd
rm $bb1/ImageBoot/$image/etc/bhversion
cp -r /etc/samba/ $bb1/ImageBoot/$image/etc/
# ====================== MetrixHD Skin ===============
if [[ ! "${image,,}" =~ "atv" ]]; then
echo " COPYING MetrixHD Skin " ; sleep 1

cp -R /media/hdd1/.MetrixHDmod/MetrixHD $bb1/ImageBoot/$image/usr/share/enigma2/
echo " COPYING MetrixHD Skin Converters " ; sleep 1
if [[ "${a,,}" =~ "python3" ]]; then
echo "Python_3 Image   "; sleep 2
cp -R /media/hdd1/.MetrixHDmod/pyth3/Converter/*.py* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/
echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R /media/hdd1/.MetrixHDmod/pyth3/Renderer/*.py* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R /media/hdd1/.MetrixHDmod/pyth3/MyMetrixLite $extfolder
cp -R /media/hdd1/.MetrixHDmod/pyth3/AutoBouquetsMaker $bb1/ImageBoot/$image/usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R /media/hdd1/.FileCommander $extfolder; fi
cp -R /media/hdd1/.MetrixHDmod/pyth3/My_ScriptRunner $extfolder

#cp -R /media/hdd1/.MetrixHDmod/poster/*.png $bb1/ImageBoot/$image/usr/share/
cp -R /media/hdd1/.MetrixHDmod/pyth3/Converter/RouteInfo.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/

else
echo "Python_2 Image   "; sleep 2

cp -R /media/hdd1/.MetrixHDmod/Converter/*.py* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/

echo " COPYING MetrixHD Skin Rnders " ; sleep 1
cp -R /media/hdd1/.MetrixHDmod/Renderer/*.py* $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer/
echo " COPYING MyMetrixLite Extension " ; sleep 1
cp -R /media/hdd1/.MetrixHDmod/MyMetrixLite $extfolder
cp -R /media/hdd1/.MetrixHDmod/AutoBouquetsMaker $bb1/ImageBoot/$image/usr/lib/enigma2/python/Plugins/SystemPlugins/
#if [ ! -d $extfolder"FileCommander" ]; then echo " COPYING FileCommander " ; sleep 1 ;cp -R /media/hdd1/.FileCommander $extfolder; fi
cp -R /media/hdd1/.MetrixHDmod/My_ScriptRunner $extfolder

#cp -R /media/hdd1/.MetrixHDmod/poster/*.png $bb1/ImageBoot/$image/usr/share/
cp -R /media/hdd1/.MetrixHDmod/Converter/RouteInfo.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/

fi
fi
cp  /media/hdd1/.MetrixHDmod/Renderer/fhdlPoster.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Renderer/
cp  /media/hdd1/.MetrixHDmod/Converter/mypic.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/
cp  /media/hdd1/.MetrixHDmod/Converter/Kitte888infoMovie.py $bb1/ImageBoot/$image/usr/lib/enigma2/python/Components/Converter/