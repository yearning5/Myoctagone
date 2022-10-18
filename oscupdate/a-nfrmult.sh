#!/bin/sh
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.tv 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.radio 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb5 
rm -Rf $bb1/NFR4XBootI/$image/etc/tuxbox/satellites.xml
cp /etc/enigma2/*.tv $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.radio $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb5 $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/tuxbox/satellites.xml $bb1/NFR4XBootI/$image/etc/tuxbox/
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.tv 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/*.radio 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb 
rm -Rf $bb1/NFR4XBootI/$image/etc/enigma2/lamedb5 
rm -Rf $bb1/NFR4XBootI/$image/etc/tuxbox/satellites.xml
cp /etc/enigma2/*.tv $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.radio $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/lamedb5 $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/tuxbox/satellites.xml $bb1/NFR4XBootI/$image/etc/tuxbox/
cp -R /etc/enigma2/weather_icons $bb1/NFR4XBootI/$image/etc/enigma2/
cp -R /etc/enigma2/weather_icons_special $bb1/NFR4XBootI/$image/etc/enigma2/
cp -R /etc/enigma2/xstreamity $bb1/NFR4XBootI/$image/etc/enigma2/
cp /etc/enigma2/*.json $bb1/NFR4XBootI/$image/etc/enigma2/