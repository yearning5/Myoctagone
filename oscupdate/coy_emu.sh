##!/bin/s

str1="sda"
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array1 <<< $var2
bb1=${array1[-1]}


if [ -d "$bb1/NFR4XBootI" ]
then
direc=$bb1/NFR4XBootI/
fi
if [ $direc ]
then

#command to array variable
aa=$(ls $direc)
#command to array variable
az=($aa)
#echo please enter the Python vesrion 2 or 3
#read pyy
pyy="all"
#if [ -z "$pyy" ]; then pyy="all";  fi
#echo $pyy has been entered
echo please enter the file name
read file2cop
#if [ -z "$file2cop" ]; then file2cop="oscupdate.py";  fi
#file2cop="journalsat.py"
#echo $file2cop has been entered
echo please enter the FOLDER  location
read folder2cop
#echo $folder2cop has been entered
#folder2cop="/oscupdate/"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values
for i in "${az[@]}"; 
do 
	:
		STR=$(grep "."  $direc$i/etc/issue | tail -1)
		SUB=vix
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $direc$i/usr/softcams/$file2cop
			echo $file2cop copied to $direc$i
		fi
		SUB=hyperio
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $direc$i/var/emu/$file2cop
			echo $file2cop copied to $direc$i
		else 
			cp $folder2cop$file2cop $direc$i/usr/bin/cam/$file2cop
			echo $file2cop copied to $direc$i
		fi
			
done

if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))


for ii in "${aaa[@]}"
do
	:
		STR=$(grep "."  $ii/etc/issue | tail -1)
		SUB=vix
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $ii/usr/softcams/$file2cop
			echo $file2cop copied to $ii
		else
		
		SUB=hyperio
		fi
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $ii/var/emu/$file2cop
			echo $file2cop copied to $ii
		else 
			cp $folder2cop$file2cop $ii/usr/bin/cam/$file2cop
			echo $file2cop copied to $ii
		fi
done

umount /media/oscam_fold
else
echo "Not NFR4XBootI"

# ======================= mmcblk0p16 ==========================
if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))
echo please enter the file name
read file2cop
#if [ -z "$file2cop" ]; then file2cop="oscupdate.py";  fi
#file2cop="journalsat.py"
#echo $file2cop has been entered
echo please enter the FOLDER  location
read folder2cop

for ii in "${aaa[@]}"
do
	:
	STR=$(grep "."  $ii/etc/issue | tail -1)
		SUB=vix
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $ii/usr/softcams/$file2cop
			echo $file2cop copied to $ii
		else
		
		SUB=hyperio
		fi
		
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $ii/var/emu/$file2cop
			echo $file2cop copied to $ii
		else 
			cp $folder2cop$file2cop $ii/usr/bin/cam/$file2cop
			echo $file2cop copied to $ii
		fi
done
umount /media/oscam_fold


fi


echo 
echo "Neoboot  Image2   "; sleep 2
echo
if [ -d "$bb1/ImageBoot" ]
then
direc=$bb1/ImageBoot/
fi

if [ $direc ]
then

#command to array variable
aa=$(ls $direc)
#command to array variable
az=($aa)
#echo please enter the Python vesrion 2 or 3
#read pyy


for i in "${az[@]}"; 
do 
	:
		STR=$(grep "."  $direc$i/etc/issue | tail -1)
		SUB=vix
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $direc$i/usr/softcams/$file2cop
			echo $file2cop copied to $direc$i
		else
		
		SUB=hyperio
		fi
		if [[ "${STR,,}" == *"${SUB,,}"* ]];then
			cp $folder2cop$file2cop $direc$i/var/emu/$file2cop
			echo $file2cop copied to $direc$i
		else 
			cp $folder2cop$file2cop $direc$i/usr/bin/cam/$file2cop
			echo $file2cop copied to $direc$i
		fi
done

fi
