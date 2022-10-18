#!/bin/sh
cp /usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot/bin/nfr4xinitnoboot /sbin/nfr4xinit
chmod 777 /sbin/nfr4xinit;chmod 777 /sbin/init;ln -sfn /sbin/nfr4xinit /sbin/init
mv /etc/init.d/volatile-media.sh /etc/init.d/volatile-media.sh.back
if [ ! -d "/etc/nfr4x/" ] 
then
mkdir /etc/nfr4x/
ddd=/etc/nfr4x/
else
ddd=/etc/nfr4x/
fi
cp /usr/lib/enigma2/python/Plugins/Extensions/NFR4XBoot/.nfr4xboot_location $ddd
echo $ddd