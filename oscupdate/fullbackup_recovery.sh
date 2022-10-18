#!/bin/bash

START_DATE=$(date -d"$(date '+%Y-%m-%d %H:%M:%S')" +%s)
drivee="/media/hdd"

freespace=$(df -k "$drivee"  | awk 'NR==2{print $4}')

if [ $freespace -gt 1000000 ]; then 
echo ok 
else 
echo "=============="
echo "No free Space"
echo "=============="

exit

 fi

backuproot='/tmp/bi/root'
MKFS_TAR='/bin/tar'
BZIP2='/usr/bin/bzip2'
if [[ -f /usr/bin/7za ]]
then
B7ZA='/usr/bin/7za'
else
cp /oscupdate/7za /usr/bin/
chmod 755 /usr/bin/7za
B7ZA='/usr/bin/7za'
fi

DIRECTORY='/media/hdd/images'
WORKDIR='/media/hdd/images/bi'
MODEL='sf8008'
IMAGEFOLDER='octagon/sf8008'
MAINDESTROOT=$DIRECTORY/build_$MODEL
Boxbranding_py_File=/usr/lib/enigma2/python/BoxBrandingTest.py
Boxbranding_py_File_Adress=https://raw.githubusercontent.com/oe-alliance/branding-module/master/BoxBranding/lib/test.py
Boxbranding_File_Dir=/home/root
Boxbranding_File=$Boxbranding_File_Dir/boxbranding.txt
if [ ! -e $Boxbranding_File ] ; then 
	wget -O $Boxbranding_py_File $Boxbranding_py_File_Adress
	python $Boxbranding_py_File | sed 's/<$//' | sed 's/ /_/g' > $Boxbranding_File
	# readout Folder Info to Full Backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
else
	# readout Folder Info to Full Backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
fi

getImageDistro="$(awk '/^getImageDistro/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getImageVersion="$(awk '/^getImageVersion/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getMachineBrand="$(awk '/^getMachineBrand/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
GetBoxName="$(awk '/^getMachineName/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getMachineRootFile="$(awk '/^getMachineRootFile/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getImageBuild="$(awk '/^getImageBuild/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getDriverDate="$(awk '/^getDriverDate/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getImageFolder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getMachineMtdKernel="$(awk '/^getMachineMtdKernel/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getMachineKernelFile="$(awk '/^getMachineKernelFile/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
getMachineBuild="$(awk '/^getMachineBuild/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"

MTDKERNEL=$getMachineMtdKernel
MTDROOTFS=$getMachineMtdRoot
KERNELBIN=$getMachineKernelFile


IMAG=$(grep "."  /etc/issue | tail -1)
if [[ $IMAG =~ "openpli" ]] ; then
IMAGEDISTRO='Openpli'
imagename=${IMAG::-6}
DISTROVERSION=$(echo  $imagename | grep -Eo '[+-]?[0-9]+([.][0-9]+)?')
else
IMAGEDISTRO=$getImageDistro
DISTROVERSION=$getImageVersion
fi

MACHINEBUILD=$getMachineBuild

if [[ $getMachineBrand == A* ]] || [[ $getMachineBrand == E* ]] || [[ $getMachineBrand == I* ]] || [[ $getMachineBrand == O* ]] || [[ $getMachineBrand == U* ]] || [[ $getMachineBrand == Xt* ]] ; then
 echo BACK-UP TOOL FOR AN $getMachineBrand $GetBoxName
else
 echo BACK-UP TOOL FOR A $getMachineBrand $GetBoxName
fi

VERSION="Version $IMAGEDISTRO $DISTROVERSION"

echo -e "\n$VERSION\n_________________________________________________\n\nPlease be patient, a backup will now be made,\n
because of the used filesystem the back-up\nwill take about 1-15 minutes for this system\n
_________________________________________________\n\nBackup Mode: Flash Online\n
_________________________________________________\n\nCreate: rootfs.tar\n"


rm -rf $WORKDIR
mkdir -p $WORKDIR

#MAINDEST=$DIRECTORY/build_$MODEL/$Main_Image_Folder

MAINDEST=$DIRECTORY/build_$MODEL/$IMAGEFOLDER
if ( df | grep -q $backuproot ); then umount $backuproot  ; fi 
if ( df | grep -q $backuproot ); then umount $backuproot  ; fi
if ( df | grep -q $backuproot ); then umount $backuproot  ; fi
sync

if [ -d  $backuproot ]; then rm -rf backuproot; mkdir -p "$backuproot" ;else mkdir -p "$backuproot" ; fi
mount --bind / $backuproot


$MKFS_TAR -cf $WORKDIR/rootfs.tar -C $backuproot --exclude ./var/nmbd --exclude ./.resizerootfs --exclude ./.resize-rootfs --exclude ./.resize-linuxrootfs --exclude ./.resize-userdata --exclude ./var/lib/samba/private/msg.sock --exclude ./var/lib/samba/msg.sock/* --exclude ./run/avahi-daemon/socket .

echo "Now Creating $getMachineRootFile"
$BZIP2 $WORKDIR/rootfs.tar


echo "Create: kerneldump"

dd if=/dev/$MTDKERNEL of=$WORKDIR/$KERNELBIN &&

echo -e "\nAlmost there... \n"
echo -e "Now building the Backup Image\n"
if [ -d  $MAINDEST ]; then rm -rf $DIRECTORY/build_$MODEL; mkdir -p "$MAINDEST" ;else mkdir -p "$MAINDEST" ; fi

# 
IFS=', ' read -r -a array1 <<< "$(cat /proc/version)"
#
enigma2sttings=$(cat /etc/enigma2/settings)
AboutText="Full Image Backup [Image Info]\nModel: $getMachineBrand $GetBoxName\nBackup Date: $(date '+%Y%m%d') \
\nChipset: 3798mv200\nCPU: Hisilicon\nCores: 4\nVersion: $DISTROVERSION\nBuild: $getImageBuild\nKernel: ${array1[2]} \
\nDrivers:\t${getDriverDate:0:4}-${getDriverDate:4:2}-${getDriverDate:6:2}\n[Enigma2 Settings]\n"
echo -e $AboutText >> $MAINDEST/imageversion
echo "$enigma2sttings" >> $MAINDEST/imageversion

mv $WORKDIR/rootfs.tar.bz2 $MAINDEST/rootfs.tar.bz2

mv $WORKDIR/$KERNELBIN $MAINDEST/$KERNELBIN


echo "Rename the unforce_$MACHINEBUILD.txt to force_$MACHINEBUILD.txt and move it to the root of your usb-stick" > $MAINDEST/force_"$MACHINEBUILD"_READ.ME
echo "When you enter the recovery menu then it will force to install the image in the linux1 selection" >> $MAINDEST/force_"$MACHINEBUILD"_READ.ME


DATE=$(date '+%Y%m%d_%H%M')

$B7ZA a -r -bt -bd $DIRECTORY/$IMAGEDISTRO-$DISTROVERSION-$MODEL-backup-"$DATE"_mmc.zip $MAINDESTROOT/*

sync

echo -e "_________________________________________________\n"
echo $DIRECTORY/$IMAGEDISTRO-$DISTROVERSION-$MODEL-backup-"$DATE"_mmc.zip
echo -e "_________________________________________________\n \nPlease wait...almost ready! \nTo restore the \
image:\nUse OnlineFlash in SoftwareManager\n_________________________________________________\n"
echo "Image created on: "$DIRECTORY/$IMAGEDISTRO-$DISTROVERSION-$MODEL-backup-"$DATE"_mmc.zip

rm -rf $DIRECTORY/build_$MODEL

umount /tmp/bi/root
rmdir /tmp/bi/root
rmdir /tmp/bi
rm -rf $WORKDIR
sleep 5

END_DATE=$(date -d"$(date '+%Y-%m-%d %H:%M:%S')" +%s)

echo "$START_DATE $END_DATE" | awk ' { printf("It took %.2f Minutes to complete this job.\n", ($2-$1)/60); } '

exit
