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
#read file2cop
#file2cop="TMBD"
folder="SquarDevise"
folder2remove="/usr/lib/enigma2/python/Plugins/Extensions/SquarDevise/SquarDevise"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values

for i in "${az[@]}"
do
	:
	rm -fR $direc$i$folder2remove
	echo $folder "removed from " $i
done
