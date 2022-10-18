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
#command to array variable
aa=$(ls $direc)
#command to array variable
az=($aa)
#echo please enter the file name
echo please enter the FOLDER  name
read file2cop
#file2cop="freearhey"
echo please enter the FOLDER  location
read folder2cop
#folder2cop="/usr/lib/enigma2/python/Plugins/Extensions/"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values

for i in "${az[@]}"
do
   : 
   if [ -d $direc$i$folder2cop ] 
   then
   cp -fR $folder2cop$file2cop $direc$i$folder2cop
   echo $file2cop "copied to " $i
   else
   echo $i "does not contain destination"
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
	cp $folder2cop$file2cop "/media/oscam_fold/"$ii$folder2cop
	echo $file2cop "copied to " $ii
	else
	echo $ii "does not contain destination"
	fi
done

umount /dev/mmcblk0p16


