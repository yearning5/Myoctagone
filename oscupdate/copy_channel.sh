##!/bin/s
if [ -d "/media/hdd/NFR4XBootI" ]
then
direc=/media/hdd/NFR4XBootI/
elif [ -d "/media/nfr4xboot/NFR4XBootI" ]
then
direc=/media/nfr4xboot/NFR4XBootI/
else
echo "Not NFR4XBootI"
exit 0
direc="No Directory"

fi
curr=$(cat $direc.nfr4xboot)

#command to array variable
aa=$(ls $direc)
#command to array variable
az=($aa)

for i in "${az[@]}"
do
   :
   if [ $i != $curr ]; then 
   rm -rf $direc$i/etc/enigma2/*.tv $direc$i/etc/enigma2/*.radio $direc$i/etc/enigma2/lamedb $direc$i/etc/enigma2/lamedb5 $direc$i/etc/tuxbox/satellites.xml
   echo "existing list removed"
   cp -f /etc/enigma2/*.tv $direc$i/etc/enigma2/
   cp -f /etc/enigma2/*.radio $direc$i/etc/enigma2/
   cp -f /etc/enigma2/lamedb $direc$i/etc/enigma2/
   cp -f /etc/enigma2/lamedb5 $direc$i/etc/enigma2/
   cp -f /etc/tuxbox/satellites.xml $direc$i/etc/tuxbox/satellites.xml
   fi
   echo "done for "$i
done


# ======================= mmcblk0p16 ==========================
if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))

for ii in "${aaa[@]}"
do
	:
	rm -rf "/media/oscam_fold/"$ii/etc/enigma2/*.tv "/media/oscam_fold/"$ii/etc/enigma2/*.radio "/media/oscam_fold/"$ii/etc/enigma2/lamedb "/media/oscam_fold/"$ii/etc/enigma2/lamedb5 "/media/oscam_fold/"$ii/etc/tuxbox/satellites.xml
	scp /etc/enigma2/*.tv "/media/oscam_fold/"$ii/etc/enigma2/
	scp /etc/enigma2/*.radio "/media/oscam_fold/"$ii/etc/enigma2/
	scp /etc/enigma2/lamedb "/media/oscam_fold/"$ii/etc/enigma2/
	scp /etc/enigma2/lamedb5 "/media/oscam_fold/"$ii/etc/enigma2/
	scp /etc/tuxbox/satellites.xml "/media/oscam_fold/"$ii/etc/tuxbox/satellites.xml
   
done

umount /dev/mmcblk0p16
