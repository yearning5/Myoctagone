##!/bin/sh
cd /tmp
FreeServer=/tmp/tounfite.txt
FreeServertmpa=/tmp/freeservra*
FreeServertmpb=/tmp/freeservrb*
FreeServertmpe=/tmp/freeservre*
FreeServertmpb70=/tmp/freeservrb70
FreeServertmpb71=/tmp/freeservrb71
FreeServertmpb72=/tmp/freeservrb72
FreeServertmpb73=/tmp/freeservrb73
FreeServertmpb74=/tmp/freeservrb74
FreeServertmpa70=/tmp/freeservra70
FreeServertmpa71=/tmp/freeservra71
FreeServertmpa72=/tmp/freeservra72
FreeServertmpa73=/tmp/freeservra73
FreeServertmpa74=/tmp/freeservra74
PATCH_J_XM="year"
PATCH_J_XM2="year"
curl -d "username=${PATCH_J_XM}&password=${PATCH_J_XM2}" -X POST http://tounfite.ddns.net/affiche.php > $FreeServertmpa71 
#sed -ne 's#.*style="color:red">\([^<]*\).*#\1#p' $FreeServertmpa71 > $FreeServertmpb72
#wget -q -O- --trust-server-names "http://tounfite.ddns.net/resultat.php" > $FreeServertmpa72
curl -d "username=${PATCH_J_XM}&password=${PATCH_J_XM2}" -X POST http://tounfite.ddns.net/resultat.php > $FreeServertmpa72 
sed -ne 's#.*style="color:red">\([^<]*\).*#\1#p' $FreeServertmpa72 > $FreeServertmpb72
sed -ne 's#.*user :\([^<]*\)</br>.*#\1#p' $FreeServertmpa71 > $FreeServertmpb73
sed -ne 's#.*pass :\([^<]*\)</br>.*#\1#p' $FreeServertmpa71 > $FreeServertmpb74
PATCH_J_XM6=$(cat /tmp/freeservrb72)
PATCH_J_XM3=$(cat /tmp/freeservrb73)
PATCH_J_XM4=$(cat /tmp/freeservrb74)
TEXT="${PATCH_J_XM6} ${PATCH_J_XM} ${PATCH_J_XM2}"
sed -i "1i\\
$TEXT" /tmp/freeservrb72
sed 2d /tmp/freeservrb72 -i
cat $FreeServertmpb72 >> $FreeServer
rm -f $FreeServertmpa > /dev/null 2>&1
rm -f $FreeServertmpb > /dev/null 2>&1
rm -f $FreeServertmpa* $FreeServertmpb*
