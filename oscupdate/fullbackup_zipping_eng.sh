#!/bin/bash

##############################
## Pike_Bishop from OpenATV ##
## https://www.opena.tv/ ##
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


# Close the OSD window.
$Wget -q -O - $Boxip/web/remotecontrol?command=174 && sleep 2


# General logging.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1> $ Logfile 2> & 1
exec 1>$Logfile


# OSD start message with job start including start time.
Startdate="$(date +%a.%d.%b.%Y-%H:%M:%S)" && echo -e "\nJOB START -> $Startdate !"
$Wget -O - -q "$Boxip/web/message?text=Starte%20Full%20Backup%20zippen%20...%20%20->%20%20$Startdate&type=1&timeout=8" > /dev/null


# FUNCTION -> OSD + Log message in the event of an error (abort).
error_message() {
	sleep 9
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)"
	echo -e "\nJOB fehlgeschlagen -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=ABBRUCH%20%20->%20%20%28%20Details%20dazu%20in%20$Logfile%20%29%20%21%0A$Enddate&type=3" > /dev/null
}

# FUNCTION -> OSD + Log End message if successful.
job_end_message() {
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)" 
	echo -e "\n\nJOB Full Backup \"${Box}\" zippen erfolgreich abgeschlossen -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=Full%20Backup%20${Box}%20zippen%20erfolgreich%20abgeschlossen%20%21%0A$Enddate&type=1&timeout=9" > /dev/null
}

# FUNCTION -> OSD + Log message in the event of an error when moving the original full backup (s).
mv_check_message() {
	sleep 10
	Enddate="$(date +%a.%d.%b.%Y-%H:%M:%S)"
	echo -e "\n\nJOB Original Full Backup/s verschieben fehlgeschlagen -> $Enddate !\n"
	$Wget -O - -q "$Boxip/web/message?text=Das%2FDie%20Originale%2Fn%20%28ungezippte%2Fn%29%20Full%20Backup%2Fs\
	%20konnten%0Ajedoch%20nicht%20verschoben%20werden%2E%20Details%20dazu%20in%3B%0A$Logfile%20->%20$Enddate&type=2" > /dev/null
}


# Check whether program p7zip is installed, if
# do not update and install package management.
if [ ! -e $Zip_Program ] ; then
	echo -e "\nAktualisiere Paketmanagement ...\n"
	opkg update

# Error check (without cancellation).
	if [ "$?" != "0" ] ; then
		echo -e "\nPaketmanagement Aktualisierung fehlgeschlagen - vorerst nicht tragisch."
		echo "Doch falls es im naechsten Schritt bei der Install vom Programm $Zip_Package zum"
		echo -e "Abbruch kommt -> ist die Netzwerkverbindung zu pruefen.\n"
	fi

	echo -e "Installiere Programm; $Zip_Package ...\n"
	opkg install $Zip_Package

# Error check.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nABBRUCH !\nInstallation Programm; $Zip_Package fehlgeschlagen."
		echo "Eventuell falls die Paketmanagement Aktualisierung zuvor fehlschlug."
		echo -e "Bitte Programm $Zip_Package manuell installieren,\nund das Script erneut starten.\n"
		error_message && exit 1
	fi
fi

# Create the required target directory (Targetdir) if necessary.
if [ ! -d $Targetdir ] ; then
	echo -e "\nErstelle Verzeichnis; $Targetdir ..."
	mkdir -p $Targetdir

# Error check.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nABBRUCH !\nVerzeichnis; $Targetdir erstellen fehlgeschlagen."
		echo -e "Bitte manuell erstellen,\nund das Script erneut starten.\n"
		error_message && exit 1
	fi
fi


# Fetch the file for box branding (test.py) from the oe-a Git only if necessary, convert it to be readable, and transfer it to the
# Copy "Boxbranding_File_Dir" as "boxbranding.txt" to read out essential information and process it further.
# Main_Image_Folder = octagon # Fixed variable only as a replacement, better read out by box branding as with the following from lines 113 -128.
if [ ! -e $Boxbranding_File ] ; then 
	$Wget -O $Boxbranding_py_File $Boxbranding_py_File_Adress
	python $Boxbranding_py_File | sed 's/<$//' | sed 's/ /_/g' > $Boxbranding_File
# Read folder info about the full backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
else
# Read folder info about the full backup from "Boxbranding_File".
	Main_Image_Folder="$(awk '/^getImageFolder/ { print $0}' "$Boxbranding_File" | cut -d "=" -f 2 | cut -d "/" -f 1)"
fi

# Check whether the "Boxbranding_File" file is available and / or the "Main_Image_Folder" tag is also filled.
if [ -z $Main_Image_Folder ] ; then
	echo -e "\n\nABBRUCH !\nVariable "Main_Image_Folder" ist leer, etwas ist"
	echo "schief gelaufen -> $Boxbranding_File nicht vorhanden/leer ?\n"
	error_message && exit 1
fi


# Check whether main full backup is available.
z=0
for d in $Usb_Backup_Image_Path/$Main_Image_Folder $Hdd_Backup_Image_Path/$Main_Image_Folder
do
	z=$((z + 1))
	if [ -d $d ] ; then
		Mediadir_only=${d%/*}
		Main_Full_Backup_Path=$d
		break
	elif [ ! -d $d -a "$z" = "2" ] ; then
		echo -e "\n\nABBRUCH !\nKein Ordner $Main_Image_Folder (Originales Full Backup)"
		echo "in; $Usb_Backup_Image_Path bzw. $Hdd_Backup_Image_Path vorhanden."
		echo -e "Es gibt also nichts zum zippen (packen).\n"
		error_message && exit 1
	fi
done


# Check whether the image is in one directory or in two directories,
# Example for the "Octagon SF8008" only in "octagon" or under "octagon / sf8008".
if [ ! -d $Main_Full_Backup_Path/*/ ] ; then
	Complete_Image_Folder_Path=/$Main_Image_Folder
else
	Complete_Image_Folder_Path="$(ls -l $Main_Full_Backup_Path | awk '{print $NF}')"
	Complete_Image_Folder_Path=/$Main_Image_Folder/$Complete_Image_Folder_Path
fi


# Check whether there is also a full backup in the full backup folder.
# Machine_Root_File = rootfs.tar.bz2 # Fixed variable only as a replacement, better read out as follows using box branding.
Machine_Root_File="$(awk '/^getMachineRootFile/ { print $0}' "$Boxbranding_File" | sed 's/^.*=//')"
#Check_if_File = "$ (ls -Rp $ Main_Full_Backup_Path | awk '/\.(bz2)/ {print $ 0}')"
Check_if_File="$(ls -Rp $Main_Full_Backup_Path | grep "$Machine_Root_File")"
if [ "$Check_if_File" != "$Machine_Root_File" ] ; then
	echo -e "\n\nABBRUCH !\nOrdner zu Full Backup $Main_Image_Folder vorhanden,"
	echo "aber kein Full Backup darin.\n"
	error_message && exit 1
fi

echo -e "\n\nFull Backup fuer \"${Complete_Image_Folder_Path//// } \" gefunden.\n"

# Read information from "Boxbranding_File", from "Full_Backup_Info_File", and elsewhere (for Zip_Name).
#Image = "$ (awk '/ ^ getImageDistro / {print $ 0}'" $ Boxbranding_File "| cut -d" = "-f 2)" # by box branding.
Image="$(grep -v "Wel" /etc/issue | head -n 1 | cut -d " " -f 1)"
#Image = "$ (cat / etc / issue | cut -d" "-f 1)" # not good with OpenATV images.

# Instead of Image and Image_Version separately, the following would also work when putting them together
# of the later "Zip_Name", however, the hyphen in front of $ {Box} must be omitted
# So in total then "Zip_Name = $ {Image_and_Version} $ {Box} - $ Additional- $ Zip_File_Date $ Extension".
#Image_and_Version = "$ (cat / etc / issue | cut -d" \\ "-f 1 | tr '' '-')"

#Image_Version = "$ (awk '/ ^ getImageVersion / {print $ 0}'" $ Boxbranding_File "| cut -d" = "-f 2)" # by box branding.
#Image_Version = "$ (awk '/ ^ Version: / {print $ NF}'" $ Mediadir_only $ {Complete_Image_Folder_Path} \
# / $ Full_Backup_Info_File ")"
# Currently using the following instead of the above command.
Image_Version="$(awk '/^Version/ { print $NF}' "$Mediadir_only${Complete_Image_Folder_Path}\
/$Full_Backup_Info_File" | sed 's/-//g')"
Box = "$ (awk '/ ^ getBoxType / {print $ 0}'" $ Boxbranding_File "| cut -d" = "-f 2)" # by box branding.
#Box = "$ (cat / proc / stb / info / boxtype)"
Additional=backup
Date="$(date +%H%M)"

# Read out image date from full backups with OpeneightTool or the backup suite.
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
echo -e "\nName der .zip Datei festgelegt auf;\n${Zip_Name}.zip\n"


# Zip (zip) into the target directory.
echo -e "\nStarte Full Backup \" ${Box} \" zippen (packen) ..."
$Nice $Nice_Args $Zip_Program a $Targetdir/${Zip_Name}.zip -tzip -mx=7 $Main_Full_Backup_Path
# $ Nice $ Nice_Args $ Zip_Program a $ Targetdir / $ {Zip_Name} .zip -tzip a -bt -bd $ Main_Full_Backup_Path

case $? in
	0)
# Check for the hit "Everything is Ok" in the log file.
	Integrity_check="$(awk '/^Everything is Ok/ { print $1,$2,$3}' "$Logfile")"

	if [ "$Integrity_check" = "Everything is Ok" ] ; then
		echo -e "\nFull Backup \" ${Box} \" erfolgreich gezippt\nund in; $Targetdir\nals; ${Zip_Name}.zip\nabgelegt.\n"
	else
# Check the correctness (integrity) of the * .zip file (is quick).
		echo -e "\nStarte Integritaets Check auf;\n$Targetdir/${Zip_Name}.zip ...\n"
		$Zip_Program t $Targetdir/${Zip_Name}.zip

			if [ "$?" = "0" ] ; then
# Check "only" after the second hit "Everything is Ok" in the log file.
				Integrity_check="$(awk '/^Everything is Ok/ { if ( ++c == 2 ) { sub("°C",""); print $1,$2,$3 } }' "$Logfile")"

					if [ "$Integrity_check" = "Everything is Ok" ] ; then
						echo -e "\nFull Backup \" ${Box} \" erfolgreich gezippt\nund in; $Targetdir\nals; ${Zip_Name}.zip\nabgelegt.\n"
					elif [ "$Integrity_check" != "Everything is Ok" ] ; then
						echo -e "\n\nABBRUCH !\nIntegritaets Check auf;\n$Targetdir/${Zip_Name}.zip\ngescheitert."
						echo -e "Moeglicherweise ist das Archiv in;\n$Targetdir mit Namen;\n${Zip_Name}.zip kaputt.\n"
						error_message && exit 1
					fi
			else
				echo -e "\n\nABBRUCH !\nIntegritaets Check auf;\n$Targetdir/${Zip_Name}.zip\ngescheitert."
				echo -e "Moeglicherweise ist das Archiv in;\n$Targetdir mit Namen;\n${Zip_Name}.zip kaputt.\n"
				error_message && exit 1
			fi
	fi
	;;
	*)
	echo -e "\n\nABBRUCH !\nFull Backup \" ${Box} \" zippen\nleider fehlgeschlagen - Beendet.\n"
	error_message && exit 1
	;;
esac


# Check whether the main full backup has already been moved.
Main_Full_Backup_Info="$(grep -m 1 "^Bereits verschoben" "$Mediadir_only\
${Complete_Image_Folder_Path}/$Full_Backup_Info_File")"
if [ "$Main_Full_Backup_Info" = "Bereits verschoben" ] ; then
	echo -e "\nOriginales Full Backup;\n$Mediadir_only${Complete_Image_Folder_Path}\nwurde schon einmal verschoben.\n"
	Main_Full_Backup=cancelled
else
	Main_Full_Backup=$Mediadir_only/$Main_Image_Folder
fi

# Check whether there is a second full backup + whether it is by date to
# Main full backup fits, as well as whether it has already been moved.
Second_Full_Backup_Path="$Mediadir_only/fullbackup_"*""
# First read out the image date, of second full backups with OpeneightTool or the backup suite.
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

if [ -d ""$Second_Full_Backup_Path"" ] ; then

	if [ "$Second_Full_Backup_Date" != "$Main_Full_Backup_Date" ] ; then
		echo -e "\nDas Full Backup in;"
		echo ""$Second_Full_Backup_Path""
		echo "passt nicht zum Full Backup in;"
		echo -e "$Mediadir_only/$Main_Image_Folder.\nEs wird daher nicht verschoben.\n"
		Second_Full_Backup=cancelled
	elif [ "$Second_Full_Backup_Date" = "$Main_Full_Backup_Date" ] ; then

			if [ "$Second_Full_Backup_Info" = "Bereits verschoben" ] ; then
				echo -e "\nOriginales Full Backup in;"
				echo ""$Second_Full_Backup_Path""
				echo -e "wurde schon einmal verschoben.\n"
				Second_Full_Backup=cancelled
			else
				Second_Full_Backup=$Second_Full_Backup_Path
			fi
	fi
else
	echo -e "\nKein Originales Zweit Full Backup;\n$Mediadir_only/fullbackup_*\nzum Verschieben vorhanden.\n"
	Second_Full_Backup=cancelled
fi

# Check whether a move is even an option, if not it ends.
if [ "$Main_Full_Backup" = "cancelled" -a "$Second_Full_Backup" = "cancelled" ] ; then
	job_end_message && exit 0
fi


# Enter the label "already moved" in advance in the original (s) to be moved full backup (s).
sed -i '1s/^/Bereits verschoben\n\n/' "$Mediadir_only${Complete_Image_Folder_Path}/$Full_Backup_Info_File"
sed -i '1s/^/Bereits verschoben\n\n/' ""$Second_Full_Backup_Path"/"*"${Complete_Image_Folder_Path}/$Full_Backup_Info_File"
sed -i '1s/^/Bereits verschoben\n\n/' ""$Second_Full_Backup_Path"/"*"/$Full_Backup_Info_File"


# Create target directory for the original (s) to be moved full backup / s.
New_Dir_for_Org_Backups="$Mediadir_only/$Maindir_for_Org_Fullbackups/$Box/\
${Image}-${Image_Version}/full_backup/${Image}-${Image_Version}-${Box}-${Zip_File_Date}_fullbackup"
echo -e "\nErstelle Verzeichnis;\n$New_Dir_for_Org_Backups\num den/die Ordner (das/die Originale/n Full Backup/s);"
echo -e "$Mediadir_only/$Main_Image_Folder und/oder;\n$Mediadir_only/fullbackup_*\ndorthin zu verschieben ...\n"
mkdir -p $New_Dir_for_Org_Backups

# Error check.
if [ "$?" != "0" ] ; then
	echo -e "\n\nVerzeichnis;\n$New_Dir_for_Org_Backups\nerstellen fehlgeschlagen.\nSomit koennen die Originalen Full Backups;"
	echo -e "$Mediadir_only/$Main_Image_Folder und/oder; $Mediadir_only/fullbackup_*\nnicht verschoben werden - nicht tragisch."
	echo -e "Einfach das Verzeichnis;\n$New_Dir_for_Org_Backups\nmanuell erstellen, und die Originalen Full Backups da hin verschieben.\n"
	job_end_message && mv_check_message && exit 1
fi


# Move original full backup / s.
for d in $Main_Full_Backup $Second_Full_Backup
do
	if [ "$d" != "cancelled" ] ; then
		echo -e "\nVerschiebe Originales Full Backup $d ..."
		$Nice $Nice_Args mv $d $New_Dir_for_Org_Backups
	fi

# Check whether the move worked.
	if [ "$?" != "0" ] ; then
		echo -e "\n\nOriginales Full Backup; $d\nverschieben fehlgeschlagen - nicht tragisch."
		echo -e "Einfach das Originale Full Backup; $d\nmanuell in das Verzeichnis;\n$New_Dir_for_Org_Backups\nverschieben.\n"
		failed=yes
	fi
done

# Error check for moving.
if [ "$failed" = "yes" ] ; then
	job_end_message && mv_check_message && exit 1
fi


# Mark the moved full backup (s) in the "Full_Backup_Info_File" with "Already moved".
# Obsolete! "Already moved" is now indicated before the move.
#sed -i '1s / ^ / Already moved \ n \ n /' "$ New_Dir_for_Org_Backups $ {Complete_Image_Folder_Path} / \
# $ Full_Backup_Info_File "
#sed -i '1s / ^ / Already moved \ n \ n /' "$ New_Dir_for_Org_Backups / fullbackup _" * "/ \
# "*" $ {Complete_Image_Folder_Path} / $ Full_Backup_Info_File "2> / dev / null

job_end_message


exit
