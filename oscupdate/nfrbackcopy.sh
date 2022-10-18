#!/bin/sh
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}

image=Openbh-4.4_turk

echo "Make directory  " $image " into $bb1/NFR4XBootI "
if [ -d $bb1/NFR4XBootI/$image ]
then
echo $image "already exists it will be deleted"
rm -rf $bb1/NFR4XBootI/$image
fi 
mkdir $bb1/NFR4XBootI/$image
echo "Directory  " $image " Created into $bb1/NFR4XBootI "

echo "tar files needed   " $image 

tar -jxf /tmp/rootfs.tar.bz2 -C $bb1/NFR4XBootI/$image &&
echo "Copying nucessary file needed   " $image 
cp /etc/network/interfaces $bb1/NFR4XBootI/$image/etc/network/interfaces

cp /etc/passwd $bb1/NFR4XBootI/$image/etc/passwd
cp /etc/shadow $bb1/NFR4XBootI/$image/etc/shadow
cp /etc/resolv.conf $bb1/NFR4XBootI/$image/etcresolv.conf

cp /etc/wpa_supplicant.conf $bb1/NFR4XBootI/$image/etc/wpa_supplicant.conf
echo "Copying directory  NFR4XBoot_client"
cp -r /usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
cp -r /usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client/.nfr4xboot_location $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot_client/.nfr4xboot_location
cp -r /usr/lib/enigma2/python/Plugins/Extensions/Hijri $bb1/NFR4XBootI/$image/usr/lib/enigma2/python/Plugins/Extensions/
mkdir -p $bb1/NFR4XBootI/$image/media/usb
# softcams vix
#fstab
cp /etc/fstab $bb1/NFR4XBootI/$image/etc/

rm $bb1/NFR4XBootI/$image/etc/init.d/tpmd

rm $bb1/NFR4XBootI/$image/etc/bhversion

