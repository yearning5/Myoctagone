##!/bin/sh

python /oscupdate/picons.py &&
if [[ -f /usr/bin/7za ]]
then
echo "7za is installed " sleep 2
else
echo "7za is Not installed "; sleep 2
echo "It will be installed "; sleep 2
cp /oscupdate/7za /usr/bin/
chmod 755 /usr/bin/7za
fi

for i in $(ls /tmp/ere/*.7z); do 7za e $i -o"/media/hdd/piconATV/" "*.png" -aoa; echo files from $i cpied to folder; sleep 2 ; done

cp /media/hdd/piconATV/1_0_1_49C_3_1_E082F62_0_0_0.png /media/hdd/piconATV/1_0_1_FB4_D_1_E082E2F_0_0_0.png
cp /media/hdd/piconATV/1_0_1_49C_3_1_E082F62_0_0_0.png /media/hdd/piconATV/1_0_1_FE6_D_1_E082E2F_0_0_0.png
cp /media/hdd/piconATV/1_0_1_3F2_1_1_E08318F_0_0_0.png /media/hdd/piconATV/1_0_1_FDC_D_1_E082E2F_0_0_0.png
cp /media/hdd/piconATV/1_0_1_3F2_1_1_E08318F_0_0_0.png /media/hdd/piconATV/1_0_1_FF0_D_1_E082E2F_0_0_0.png
cp /media/hdd/piconATV/1_0_19_791E_2C6_600_E080000_0_0_0.png /media/hdd/piconATV/1_0_1_DA2_C_1_E082E7C_0_0_0.png
cp /media/hdd/piconATV/1_0_1_2BC7_19C8_FBFF_820000_0_0_0.png /media/hdd/piconATV/1_0_1_77FE_2C3_600_E080000_0_0_0.png
cp /media/hdd/piconATV/1_0_1_7598_2BD_600_E080000_0_0_0.png /media/hdd/piconATV/1_0_1_A32_5_1_E082E09_0_0_0.png
cp /media/hdd/piconATV/1_0_19_7729_2C1_600_E080000_0_0_0.png /media/hdd/piconATV/1_0_1_A3C_5_1_E082E09_0_0_0.png
cp /media/hdd/piconATV/1_0_1_C1D_1E78_71_820000_0_0_0.png /media/hdd/piconATV/1_0_1_3330_3390_71_820000_0_0_0.png

