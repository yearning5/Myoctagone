##!/bin/s
if [ -d "/media/hdd/NFR4XBootI" ]
then

direc=/media/hdd/NFR4XBootI/
elif [ -d "/media/nfr4xboot/NFR4XBootI" ]
then

direc=/media/nfr4xboot/NFR4XBootI/
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
if [ -z "$file2cop" ]; then file2cop="oscupdate.py";  fi
#file2cop="journalsat.py"
#echo $file2cop has been entered
echo please enter the FOLDER  location
read folder2cop
if [ -z "$folder2cop" ]; then folder2cop="/oscupdate/";  fi
#echo $folder2cop has been entered
#folder2cop="/oscupdate/"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values
for i in "${az[@]}"; 
do 
	:
		if [[ $pyy == 2 ]]  && [[ ! "$i"  =~ "py" ]] 
		then
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		 
		elif [[ $pyy == 3 ]]  && [[  "$i"  =~ "py" ]] 
			then  
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		elif [[ $pyy == "all" ]]
			then   
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		fi
done

#for i in "${az[@]}"
#do
#   :
#	if [[ ! "$i"  =~ "py"$pyy ]]
#	then
#		if [ -d $direc$i$folder2cop ] 
#		then
#		cp $folder2cop$file2cop $direc$i$folder2cop
#		echo $file2cop "copied to " $i
#		else
#		echo $i "does not contain destination"
#		echo "we will create foler " $folder2cop
#		mkdir $direc$i$folder2cop
#		cp $folder2cop$file2cop $direc$i$folder2cop
#		echo $file2cop "copied to " $i
#		fi
#	fi
#done
# ======================= mmcblk0p16 ==========================
if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))


for ii in "${aaa[@]}"
do
	:
	if [[ $pyy == 2 ]]  
	then
	if [ -d "/media/oscam_fold/"$ii$folder2cop ] 
	then
	cp $folder2cop$file2cop "/media/oscam_fold/"$ii$folder2cop
	echo $file2cop "copied to " $ii
	else
	echo $ii "does not contain destination"
	fi
	elif [[ $pyy == "all" ]]
	then
	if [ -d "/media/oscam_fold/"$ii$folder2cop ] 
	then
	cp $folder2cop$file2cop "/media/oscam_fold/"$ii$folder2cop
	echo $file2cop "copied to " $ii
	else
	echo $ii "does not contain destination"
	fi
	fi
done

umount /media/oscam_fold
else
echo "Not NFR4XBootI"

# ======================= mmcblk0p16 ==========================
if [ -d "/media/oscam_fold" ]; then  echo "ok oscam_fold exists"; else echo "will create oscam_fold ";mkdir /media/oscam_fold; fi

mount /dev/mmcblk0p16 /media/oscam_fold
aaa=($(ls /media/oscam_fold | grep linuxrootfs))
echo please enter the Python vesrion 2 or 3
read pyy
if [ -z "$pyy" ]; then pyy="all";  fi
#echo $pyy has been entered
echo please enter the file name
read file2cop
if [ -z "$file2cop" ]; then file2cop="oscupdate.py";  fi
#file2cop="journalsat.py"
#echo $file2cop has been entered
echo please enter the FOLDER  location
read folder2cop
if [ -z "$folder2cop" ]; then folder2cop="/oscupdate/";  fi

for ii in "${aaa[@]}"
do
	:
	if [[ $pyy == 2 ]]  
	then
	if [ -d "/media/oscam_fold/"$ii$folder2cop ] 
	then
	cp $folder2cop$file2cop "/media/oscam_fold/"$ii$folder2cop
	echo $file2cop "copied to " $ii
	else
	echo $ii "does not contain destination"
	fi
	elif [[ $pyy == "all" ]]
	then
	if [ -d "/media/oscam_fold/"$ii$folder2cop ] 
	then
	cp $folder2cop$file2cop "/media/oscam_fold/"$ii$folder2cop
	echo $file2cop "copied to " $ii
	else
	echo $ii "does not contain destination"
	fi
	fi
done

umount /media/oscam_fold


fi

echo 
echo "Neoboot  Image2   "; sleep 2
echo
if [ -d "/media/hdd/ImageBoot" ]
then

direc=/media/hdd/ImageBoot/
elif [ -d "/media/neoboot/ImageBoot" ]
then

direc=/media/neoboot/ImageBoot/
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

for i in "${az[@]}"; 
do 
	:
		a=$(ls $direc$i/usr/lib/)
		if [[ $pyy == 2 ]]  && [[ ! "${a,,}" =~ "python3" ]]
		then
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		 
		elif [[ $pyy == 3 ]]  && [[ "${a,,}" =~ "python3" ]]
			then  
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		elif [[ $pyy == "all" ]]
			then   
			if [ -d $direc$i$folder2cop ] 
			then
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			else
			echo $i "does not contain destination"
			echo "we will create foler " $folder2cop
			mkdir $direc$i$folder2cop
			cp $folder2cop$file2cop $direc$i$folder2cop
			echo $file2cop "copied to " $i
			fi
		fi
done

fi
