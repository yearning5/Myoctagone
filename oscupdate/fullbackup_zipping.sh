#!/bin/bash

##############################
## Pike_Bishop from OpenATV ##
##  https://www.opena.tv/   ##
##############################

## Variables ##
Boxip=http://localhost

Mediapath=/media
Usb_Backup_Image_Path=$Mediapath/usb
Hdd_Backup_Image_Path=$Mediapath/hdd
Targetdir=$Mediapath/hdd/images
Maindir_for_Org_Fullbackups=Enigma2
Boxbranding_py_File=/usr/lib/enigma2/python/BoxBrandingTest.py
Boxbranding_py_File_Adress=https://raw.githubusercontent.com/oe-alliance/branding-module/master/BoxBranding/lib/test.py
Boxbranding_File_Dir=/home/root
Boxbranding_File=$Boxbranding_File_Dir/boxbranding.txt
Tmp=/tmp
Logfile=$Tmp/fullbackup_image_zipped.log

Full_Backup_Info_File=imageversion

Nice=/bin/nice
Nice_Args="-n 19"
Wget=/usr/bin/wget
Zip_Package=p7zip
Zip_Program=/usr/bin/7za


# close OSD Window automatically.
$Wget -q -O - $Boxip/web/remotecontrol?command=174 && sleep 2


# general Logging.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1>$Logfile 2>&1
exec 1>$Logfile


# OSD job Startmessage with Startdate.
Startdate="$(date +%a.%d.%b.%Y-%H:%M:%S)" && echo -e "\nJOB START -> $Startdate !"
$Wget -O - -q "$Boxip/web/message?text=Start%20Full%20Backup%20zipping%20...%20%20->%20%20$Startdate&type=1&timeout=8" > /dev/null


# FUNCTION -> OSD + Log Message if Error (Abort).
error_message() {
	sleep 9
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)"
	echo -e "\nJOB failed -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=Abort%20%20->%20%20%28%20Details%20thereto%20in%20$Logfile%20%29%20%21%0A$Enddate&type=3" > /dev/null
}

# FUNCTION -> OSD + Log End Message if successful.
job_end_message() {
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)" 
	echo -e "\n\nJOB Full Backup \"${Box}\" zipping successful finished -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=Full%20Backup%20${Box}%20zipping%20successful%20finished%20%21%0A$Enddate&type=1&timeout=9" > /dev/null
}

# FUNCTION -> OSD + Log Message if Error at to move from the Original Full Backup/s.
mv_check_message() {
	sleep 10
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)"
	echo -e "\n\nJOB to move Original Full Backup/s failed -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=To%20move%20the%20Original%20%28unzipped%29%20Full%20Backup%2Fs\
	%20failed%2E%0A%20Details%20thereto%20in%3B%0A$Logfile%20->%20$Enddate&type=2" > /dev/null
}


# Check if Program p7zip is installed, when 
# not Packagemanagement-Update and install it.
if [ ! -e $Zip_Program ] ; then
	echo -e "\nPackagemanagement-Update ...\n"
	opkg update

	# Error Check (without Abort).
	if [ "$?" != "0" ] ; then
		echo -e "\nPackagemanagement-Update failed - for now not tragically."
		echo "But if it comes at the next step by the install from the Program $Zip_Package"
		echo -e "to an Abort -> check your Network-Connection.\n"
	fi

	echo -e "Install Program; $Zip_Package ...\n"
	opkg install $Zip_Package

	# Error Check.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nABORT !\nInstall Programm; $Zip_Package failed."
		echo "Maybe if the Packagemanagement-Update previously also was failed."
		echo -e "Please install the Program $Zip_Package manually,\nand start the Script again.\n"
		error_message && exit 1
	fi
fi

# if required, create the Targetdirectory (Targetdir).
if [ ! -d $Targetdir ] ; then
	echo -e "\nCreate Directory; $Targetdir ..."
	mkdir -p $Targetdir

	# Error Check.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nABORT !\nDirectory; $Targetdir Creation failed."
		echo -e "Please create it manually,\nand start the Script again.\n"
		error_message && exit 1
	fi
fi


# if required, download the file (test.py) for Boxbranding from oe-a git, make it readable, and copy it
# to the "Boxbranding_File_Dir" as "boxbranding.txt" to readout essentially infos from it.
#Main_Image_Folder=octagon # static Variable only as Replacement, better read it out with Boxbranding as following from Line 115 -130.
if [ ! -e $Boxbranding_File ] ; then 
	$Wget -O $Boxbranding_py_File $Boxbranding_py_File_Adress
	python $Boxbranding_py_File | sed 's/<$//' | sed 's/ /_/g' > $Boxbranding_File
	# readout Folder Info to Full Backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
else
	# readout Folder Info to Full Backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
fi

# Check if the file "Boxbranding_File" is available and/or if the Variable "Main_Image_Folder" is filled.
if [ -z $Main_Image_Folder ] ; then
	echo -e "\n\nABORT !\nVariable "Main_Image_Folder" is empty, something is"
	echo "gone wrong -> $Boxbranding_File not available/empty ?\n"
	error_message && exit 1
fi


# Check if Main Full Backup available.
z=0
for d in $Usb_Backup_Image_Path/$Main_Image_Folder $Hdd_Backup_Image_Path/$Main_Image_Folder
do
	z=$((z + 1))
	if [ -d $d ] ; then
		Mediadir_only=${d%/*}
		Main_Full_Backup_Path=$d
		break
	elif [ ! -d $d -a "$z" = "2" ] ; then
		echo -e "\n\nABORT !\nNo Folder $Main_Image_Folder (Original Full Backup)"
		echo "in; $Usb_Backup_Image_Path respectively $Hdd_Backup_Image_Path available."
		echo -e "So there is nothing to zip (packing).\n"
		error_message && exit 1
	fi
done


# Check if the Image is only in one or in two Directory/s,
# as Example for the "Octagon SF8008" only in "octagon" or under "octagon/sf8008".
if [ ! -d $Main_Full_Backup_Path/*/ ] ; then
	Complete_Image_Folder_Path=/$Main_Image_Folder
else
	Complete_Image_Folder_Path="$(ls -l $Main_Full_Backup_Path | awk '{print $NF}')"
	Complete_Image_Folder_Path=/$Main_Image_Folder/$Complete_Image_Folder_Path
fi


# Check if in the Full Backup Folder is also a Full Backup in it.
#Machine_Root_File=rootfs.tar.bz2 # static Variable only as Replacement, better as following read it out with Boxbranding.
Machine_Root_File="$(awk '/^getMachineRootFile/ { print $0}' "$Boxbranding_File" | sed 's/^.*=//')"
#Check_if_File="$(ls -Rp $Main_Full_Backup_Path | awk '/\.(bz2)/ { print $0}')" # not good enough.
Check_if_File="$(ls -Rp $Main_Full_Backup_Path | grep "$Machine_Root_File")"
if [ "$Check_if_File" != "$Machine_Root_File" ] ; then
	echo -e "\n\nABORT !\nFolder for Full Backup $Main_Image_Folder available,"
	echo "but no Full Backup in it.\n"
	error_message && exit 1
fi

echo -e "\n\nFull Backup for \"${Complete_Image_Folder_Path//// } \" found.\n"

# readout Infos from "Boxbranding_File", from "Full_Backup_Info_File", and other files (for Zip_Name).
#Image="$(awk '/^getImageDistro/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2)" # with Boxbranding.
Image="$(grep -v "Wel" /etc/issue | cut -d " " -f 1)" # from file "/etc/issue".
#Image="$(cat /etc/issue | cut -d " " -f 1)" # not good for OpenATV Images.

# Instead readout Image and Image_Version separate it works the following too, but then by combine
# the "Zip_Name" later in line 208 it needs to remove the Hyphen "-" before the Variable ${Box} so
# that it looks as "Zip_Name=${Image_and_Version}${Box}-$Additional-$Zip_File_Date$Extension".
#Image_and_Version="$(cat /etc/issue | cut -d "\\" -f 1 | tr ' ' '-')"

#Image_Version="$(awk '/^getImageVersion/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2)" # with Boxbranding.
#Image_Version="$(awk '/^Version:/ { print $NF}' "$Mediadir_only${Complete_Image_Folder_Path}\
#/$Full_Backup_Info_File")" # in this case better as with Boxbranding to zip also older Full Backup/s.
# but i use the following at the moment instead.
Image_Version="$(awk '/^Version/ { print $NF}' "$Mediadir_only${Complete_Image_Folder_Path}\
/$Full_Backup_Info_File" | sed 's/-//g')"
Box="$(awk '/^getBoxType/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2)" # with Boxbranding.
#Box="$(cat /proc/stb/info/boxtype)"
Additional=backup
Date="$(date +%H%M)"

# readout the Image Date, from Fullbackup/s with OpeneightTool or Backupsuite.
Openeight_backuptool_infodate=Sicherungskopie
Backupsuite_backuptool_infodate=Back-up
if grep "$Openeight_backuptool_infodate" $Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File ; then
	Main_Full_Backup_Date="$(awk -v var=$Openeight_backuptool_infodate 'match($1,var){print $NF}'\
	"$Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File" | sed 's/-//g')"
elif grep "$Backupsuite_backuptool_infodate" $Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File ; then
	Main_Full_Backup_Date="$(awk -v var=$Backupsuite_backuptool_infodate 'match($1,var){print $NF}'\
	"$Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File" | cut -d "_" -f 1 | tr -d '.' )"
fi

Zip_File_Date=${Main_Full_Backup_Date}-$Date
Extension=_mmc
Zip_Name=${Image}-${Image_Version}-${Box}-$Additional-$Zip_File_Date$Extension
echo -e "\nName of the .zip File defined to;\n${Zip_Name}.zip\n"


# zipping (packing) in the Targetdirectory.
echo -e "\nStart Full Backup \" ${Box} \" zipping (packing) ..."
$Nice $Nice_Args $Zip_Program a $Targetdir/${Zip_Name}.zip -tzip -mx=7 $Main_Full_Backup_Path
#$Nice $Nice_Args $Zip_Program a $Targetdir/${Zip_Name}.zip -tzip a -bt -bd $Main_Full_Backup_Path

case $? in
	0)
	# Check for Hits "Everything is Ok" in Logfile.
	Integrity_check="$(awk '/^Everything is Ok/ { print $1,$2,$3}' "$Logfile")"

	if [ "$Integrity_check" = "Everything is Ok" ] ; then
		echo -e "\nFull Backup \" ${Box} \" zipping successful\nand in; $Targetdir\nas; ${Zip_Name}.zip\ndiscarded.\n"
	else
		# Check the Correctness (Integrity) from *.zip File (goes fast).
		echo -e "\nStart Integrity Check on;\n$Targetdir/${Zip_Name}.zip ...\n"
		$Zip_Program t $Targetdir/${Zip_Name}.zip

			if [ "$?" = "0" ] ; then
				# Check only for the second Hits "Everything is Ok" in Logfile.
				Integrity_check="$(awk '/^Everything is Ok/ { if ( ++c == 2 ) { sub("°C",""); print $1,$2,$3 } }' "$Logfile")"

					if [ "$Integrity_check" = "Everything is Ok" ] ; then
						echo -e "\nFull Backup \" ${Box} \" zipping successful\nand in; $Targetdir\nas; ${Zip_Name}.zip\ndiscarded.\n"
					elif [ "$Integrity_check" != "Everything is Ok" ] ; then
						echo -e "\n\nABORT !\nIntegrity Check on;\n$Targetdir/${Zip_Name}.zip\nfailed."
						echo -e "Possibly the Archive in;\n$Targetdir with Namen;\n${Zip_Name}.zip is broken.\n"
						error_message && exit 1
					fi
			else
				echo -e "\n\nABORT !\nIntegrity Check on;\n$Targetdir/${Zip_Name}.zip\nfailed."
				echo -e "Possibly the Archive in;\n$Targetdir with Namen;\n${Zip_Name}.zip is broken.\n"
				error_message && exit 1
			fi
	fi
	;;
	*)
	echo -e "\n\nABORT !\nFull Backup \" ${Box} \" zipping\nunfortunately failed - Finished.\n"
	error_message && exit 1
	;;
esac


# Check if the Main Full Backup was moved one times.
Main_Full_Backup_Info="$(grep -m 1 "^Bereits verschoben" "$Mediadir_only\
${Complete_Image_Folder_Path}/$Full_Backup_Info_File")"
if [ "$Main_Full_Backup_Info" = "Bereits verschoben" ] ; then
	echo -e "\nOriginal Full Backup;\n$Mediadir_only${Complete_Image_Folder_Path}\nwas already moved one times.\n"
	Main_Full_Backup=cancelled
else
	Main_Full_Backup=$Mediadir_only/$Main_Image_Folder
fi

# Check if a Second Full Backup is available + if it is from the same date
# as the Main Full Backup, and if it was already moved one times.
Second_Full_Backup_Path="$Mediadir_only/fullbackup_"*""
# Firstly readout the Image Date, from Second-Fullbackup with OpeneightTool or Backupsuite.
if grep "$Openeight_backuptool_infodate" ""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File" ; then
	Second_Full_Backup_Date="$(awk -v var=$Openeight_backuptool_infodate 'match($1,var){print $NF}'\
	""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File" | sed 's/-//g')"
elif grep "$Backupsuite_backuptool_infodate" ""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File" ; then
	Second_Full_Backup_Date="$(awk -v var=$Backupsuite_backuptool_infodate 'match($1,var){print $NF}'\
	""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File" | cut -d "_" -f 1 | tr -d '.')"
fi

if grep -m 1 "^Bereits verschoben" ""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File" ; then
	Second_Full_Backup_Info="$(grep -m 1 "^Bereits verschoben"\
	""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File")"
elif grep -m 1 "^Bereits verschoben" ""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File" ; then
	Second_Full_Backup_Info="$(grep -m 1 "^Bereits verschoben"\
	""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File")"
fi

if [ -d "$Second_Full_Backup_Path" ] ; then

	if [ "$Second_Full_Backup_Date" != "$Main_Full_Backup_Date" ] ; then
		echo -e "\nThe Full Backup in;"
		echo ""$Second_Full_Backup_Path""
		echo "fits not to the Full Backup in;"
		echo -e "$Mediadir_only/$Main_Image_Folder.\ntherefore it will be not moved.\n"
		Second_Full_Backup=cancelled
	elif [ "$Second_Full_Backup_Date" = "$Main_Full_Backup_Date" ] ; then

			if [ "$Second_Full_Backup_Info" = "Bereits verschoben" ] ; then
				echo -e "\nOriginal Full Backup in;"
				echo ""$Second_Full_Backup_Path""
				echo -e "was already moved one times.\n"
				Second_Full_Backup=cancelled
			else
				Second_Full_Backup=$Second_Full_Backup_Path
			fi
	fi
else
	echo -e "\nNo Original Second Full Backup;\n$Mediadir_only/fullbackup_*\nto move available.\n"
	Second_Full_Backup=cancelled
fi

# Check if a move is necessary, if not it will be finished.
if [ "$Main_Full_Backup" = "cancelled" -a "$Second_Full_Backup" = "cancelled" ] ; then
	job_end_message && exit 0
fi


# First fill in Tagging "Bereits verschoben" in the Original Full Backup/s to move.
sed -i '1s/^/Bereits verschoben\n\n/' "$Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File"
sed -i '1s/^/Bereits verschoben\n\n/' ""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File"
sed -i '1s/^/Bereits verschoben\n\n/' ""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File"


# Create Targetdirectory for Original Full Backup/s to move.
New_Dir_for_Org_Backups="$Mediadir_only/$Maindir_for_Org_Fullbackups/$Box/\
${Image}-${Image_Version}/full_backup/${Image}-${Image_Version}-${Box}-${Zip_File_Date}_fullbackup"
echo -e "\nCreate Directory;\n$New_Dir_for_Org_Backups\nto move the Folder/s (to/the Original Full Backup/s);"
echo -e "$Mediadir_only/$Main_Image_Folder and/or;\n$Mediadir_only/fullbackup_* there\n ...\n"
mkdir -p $New_Dir_for_Org_Backups

# Error Check.
if [ "$?" != "0" ] ; then
	echo -e "\n\nCreation Directory;\n$New_Dir_for_Org_Backups\nfailed.\ntherefore the Original Full Backup/s;"
	echo -e "$Mediadir_only/$Main_Image_Folder and/or; $Mediadir_only/fullbackup_*\ncan't be move - not tragically."
	echo -e "Create the Directory;\n$New_Dir_for_Org_Backups\nmanually, and move the Original Full Backup/s there.\n"
	job_end_message && mv_check_message && exit 1
fi


# Move the Original Full Backup/s.
for d in $Main_Full_Backup $Second_Full_Backup
do
	if [ "$d" != "cancelled" ] ; then
		echo -e "\nmove Original Full Backup $d ..."
		$Nice $Nice_Args mv $d $New_Dir_for_Org_Backups
	fi

	# Check if move was ok.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nOriginal Full Backup; $d\nto move failed - not tragically."
		echo -e "Move the Original Full Backup; $d\nmanually to Directory;\n$New_Dir_for_Org_Backups.\n"
		failed=yes
	fi
done

# Error Check to move.
if [ "$failed" = "yes" ] ; then
	job_end_message && mv_check_message && exit 1
fi


# The following is obsolete, so no translations needed for it.
# Die/das verschobene/n Full Backup/s im "Full_Backup_Info_File" mit "Bereits verschoben" kennzeichnen.
# Obsolete ! Die Kennzeichnung "Bereits verschoben" erfolgt nun schon vor dem Verschieben.
#sed -i '1s/^/Bereits verschoben\n\n/' "$New_Dir_for_Org_Backups${Complete_Image_Folder_Path}/\
#$Full_Backup_Info_File"
#sed -i '1s/^/Bereits verschoben\n\n/' "$New_Dir_for_Org_Backups/fullbackup_"*"/\
#"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File" 2> /dev/null


job_end_message


exit
