##!/bin/sh
cd /tmp
FreeServer=/tmp/anwar.txt
FreeServertmpa=/tmp/freeservra*
FreeServertmpb=/tmp/freeservrb*
FreeServertmpe=/tmp/freeservre*
HTTPSERV70="http://anwarcccam.xyz/index1.php"
HTTPSERV71="http://skypkcccam.com/testline.php"
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
wget -O $FreeServertmpa70 $HTTPSERV70 > /dev/null 2>&1
wget -O $FreeServertmpa71 $HTTPSERV71 > /dev/null 2>&1
sed -ne 's#.*Username" value="\([^"<]*\).*#\1#p' $FreeServertmpa71 > $FreeServertmpb71
sed -ne 's#.*Password" value="\([^"<]*\).*#\1#p' $FreeServertmpa71 > $FreeServertmpb72
sed -ne 's#.*name="expiry"value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb73
sed -ne 's#.*name="enddate"value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb7
PATCH_J_XM="yearing_5"
PATCH_J_XM2="yearing_5"
PATCH_J_XM3=$(cat /tmp/freeservrb73)
PATCH_J_XM4=$(cat /tmp/freeservrb74)
curl -d "url=anwarcccam.xyz&portcccam=55000&user11=${PATCH_J_XM}&pass11=${PATCH_J_XM2}&expiry=${PATCH_J_XM3}&enddate=${PATCH_J_XM4}&submit=GenerateCline" -X POST http://anwarcccam.xyz/index1.php > $FreeServertmpa71 
sed -ne 's#.*>Your Cline\([^<]*\).*#\1#p' $FreeServertmpa71 > $FreeServertmpa72
sed 's#^#C#' $FreeServertmpa72 > $FreeServertmpa73
cat $FreeServertmpa73 >> $FreeServer:
rm -f $FreeServertmpa > /dev/null 2>&1
rm -f $FreeServertmpb > /dev/null 2>&1
rm -f $FreeServertmpa* $FreeServertmpb*