Imagemount="/tmp/multibootcheck"
Imageroot="/tmp/imageroot"





SystemInfo["HasMultibootMTD"]
SystemInfo["HasRootSubdir"]

#===================================================

SystemInfo["canRecovery"] :

if [[ "hd51 vs1500 h7 8100s" =~ $getMachineBuild ]]; then
canRecovery=(disk.img mmcblk0p1)
elif [[ "xc7439 osmio4k osmio4kplus osmini4k" =~ $getMachineBuild ]]; then
canRecovery=(emmc.img mmcblk1p1)
elif [[ "gbmv200 cc1 sf8008 sf8008m sf8008opt sx988 ustym4kpro ustym4kottpremium beyonwizv2 viper4k og2ott4k" =~ $getMachineBuild ]]; then
canRecovery=(usb_update.bin none)
fi

#===================================================

SystemInfo["canMultiBoot"]:

SystemInfo["canMultiBoot"] = getMultibootslots()


bootslots = {}

#SystemInfo["MBbootdevice"] = getMBbootdevice()

# MBbootdevice
if [ ! -d "$Imagemount" ]; then
mkdir -p $Imagemount
fi

for device in  /dev/block/by-name/bootoptions /dev/mmcblk0p1 /dev/mmcblk1p1 /dev/mmcblk0p3 /dev/mmcblk0p4;
do 
	if ls $device > /dev/null; then 
		mount $device $Imagemount 
	if [ -f $Imagemount/STARTUP ]; then 
	echo [Multiboot] Startupdevice found: $device
	MBbootdevice=$device
	fi
	umount $Imagemount
	fi
done

	
if ! mount | grep $Imagemount > /dev/null; then
	rm -r $Imagemount
fi		
		
	
# 


if SystemInfo["MBbootdevice"]:

if [ ! -z  $MBbootdevice ]; then
if [ ! -d "$Imagemount" ]; then
mkdir -p $Imagemount
fi

mount $MBbootdevice $Imagemount
	Console().ePopen("/bin/mount %s %s" % (SystemInfo["MBbootdevice"], Imagemount))
for file in $Imagemount/STARTUP_*;
do
if [[ *$file* =~ "STARTUP_RECOVERY" ]] ; then
RecoveryMode=True
echo "[multiboot] [getMultibootslots] RecoveryMode is set to: "$RecoveryMode

arrIN=(${file//_/ })
if [[ *$file* =~ "BOXMODE" ]] ; then
slotnumber=${arrIN[-3]}
else
slotnumber=${arrIN[-1]}
fi
re='^[0-9]+$'
if [[ $slotnumber =~ $re ]]; then

 
			if slotnumber.isdigit() and slotnumber not in bootslots:
				slot = {}
				for line in open(file).readlines():
					# print "Multiboot getMultibootslots readlines = %s " %line
					if "root=" in line:
						line = line.rstrip("\n")
						device = getparam(line, "root")
						if path.exists(device) or device == "ubi0:ubifs":
							slot["device"] = device
							slot["startupfile"] = path.basename(file)
							if "sda" in line:
								slot["kernel"] = "/dev/sda%s" % line.split("sda", 1)[1].split(" ", 1)[0]
								slot["rootsubdir"] = None
							elif "ubi.mtd=" in line:
								slot["kernel"] = "/dev/mtd%s" % line.split("mtd", 1)[1].split(" ", 1)[0]
							else:
								slot["kernel"] = "%sp%s" % (device.split("p")[0], int(device.split("p")[1]) - 1)
							if "rootsubdir" in line:
								SystemInfo["HasRootSubdir"] = True
								if "ubi.mtd=" in line:
									SystemInfo["HasMultibootMTD"] = True
								print "[multiboot] [getMultibootslots] HasRootSubdir is set to:%s" % SystemInfo["HasRootSubdir"]
								slot["rootsubdir"] = getparam(line, "rootsubdir")
								slot["kernel"] = getparam(line, "kernel")

						break
				if slot:
					bootslots[int(slotnumber)] = slot
		print "[multiboot1] getMultibootslots bootslots = %s" % bootslots
		Console().ePopen("umount %s" % Imagemount)
		if not path.ismount(Imagemount):
			rmdir(Imagemount)
	return bootslots

