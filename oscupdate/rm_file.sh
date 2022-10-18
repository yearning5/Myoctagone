##!/bin/sh
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
#command to array variable
aa=$(ls $direc)
#command to array variable
az=($aa)
#echo please enter the file name
#read file2cop
file2cop="Myclock.ttf"
folder2cop="/usr/share/fonts/"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values

for i in "${az[@]}"
do
   : 
   if [ -d $direc$i$folder2cop ] 
   then
   rm  $direc$i$folder2cop$file2cop
   echo $file2cop "removed  from " $i
   else
   echo $i "does not contain destination"
   #echo "we will create foler " $folder2cop
   #mkdir $direc$i$folder2cop
   #cp $folder2cop$file2cop $direc$i$folder2cop$file2cop
   echo $file2cop "removed  from " $i
   fi
done


# ======================= mmcblk0p16 ==========================
if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))

for ii in "${aaa[@]}"
do
	:
	if [ -d "/media/oscam_fold/"$ii$folder2cop ] 
	then
	rm  "/media/oscam_fold/"$ii$folder2cop$file2cop
	echo $file2cop "removed  from " $ii
	else
	echo $ii "does not contain destination"
	fi
done

umount /dev/mmcblk0p16


