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
file2edt="fstab"
folder2cop="/etc/"
#to print array variable
#  echo ${az[*]}
#  echo ${az[@]}

#Iterate Through Array Values

for i in "${az[@]}"
do
   : 
   if ! grep -q "409ecc03-05d9-410b-8a00-780e5fae11a9" $direc$i$folder2cop$file2edt
   then 
   echo -n "UUID=409ecc03-05d9-410b-8a00-780e5fae11a9         /media/hdd     auto		defaults				0  0" >> $direc$i$folder2cop$file2edt
   echo "append text to " $direc$i$folder2cop$file2edt "with Success"
   else 
   echo "text already exists in " $direc$i$folder2cop$file2edt
   fi
done   
   
