# ! / bin / bash
str="sdb"
str1="sda"
var1=$(df -h | grep $str)
var2=$(df -h | grep $str1)
IFS=' ' read -r -a array <<< $var1
IFS=' ' read -r -a array1 <<< $var2
bb=${array[-1]}
bb1=${array1[-1]}


rm -rf /tmp/channels_b
rm -rf $bb/.backup/channels_b
rm -rf $bb1/.backup/channels_b
mkdir /tmp/channels_b
cat /etc/enigma2/settings | grep "config.Nims" >> /tmp/channels_b/diseqcayar.txt
cp /etc/enigma2/*.tv /tmp/channels_b/
cp /etc/enigma2/*.radio /tmp/channels_b/
cp /etc/enigma2/lamedb /tmp/channels_b/
cp /etc/enigma2/lamedb5 /tmp/channels_b/
cp /etc/tuxbox/satellites.xml /tmp/channels_b/
echo "backed up to channels /tmpdirectory"
rm -rf /tmp/*.txt
mkdir -p $bb/.backup/channels_b
mkdir -p $bb1/.backup/channels_b
cp -r /tmp/channels_b $bb/.backup/
cp -r /tmp/channels_b $bb1/.backup/
exit 0