##!/bin/sh
cd /tmp
saeed7
FreeServer=/tmp/saeed7.txt
FreeServertmpa=/tmp/freeservra*
FreeServertmpb=/tmp/freeservrb*
FreeServertmpe=/tmp/freeservre*
HTTPSERV70="http://www.saeed7.com/free.php"
FreeServertmpb70=/tmp/freeservrb70
FreeServertmpb71=/tmp/freeservrb71
FreeServertmpb72=/tmp/freeservrb72
FreeServertmpb73=/tmp/freeservrb73
FreeServertmpb74=/tmp/freeservrb74
FreeServertmpb75=/tmp/freeservrb75
FreeServertmpb76=/tmp/freeservrb76
FreeServertmpa70=/tmp/freeservra70
FreeServertmpa71=/tmp/freeservra71
FreeServertmpa72=/tmp/freeservra72
FreeServertmpa73=/tmp/freeservra73
FreeServertmpa74=/tmp/freeservra74
wget -O $FreeServertmpa70 $HTTPSERV70 > /dev/null 2>&1
sed -ne 's#.*name="Username"  value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb73
sed -ne 's#.*name="Password"  value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb74
PATCH_J_XM=$(cat /tmp/freeservrb73)
PATCH_J_XM2=$(cat /tmp/freeservrb74)
curl -d "Username=${PATCH_J_XM}&Password=${PATCH_J_XM2}&addf= FREE LINE GENRATE here " -X POST "http://www.saeed7.com/free.php" > $FreeServertmpa71 
sed -ne 's#.*><center><br><h1>\([^"<]*\) <.*#\1#p' $FreeServertmpa71 > $FreeServertmpa74
cat $FreeServertmpa74 >> $FreeServer
rm -f $FreeServertmpa > /dev/null 2>&1
rm -f $FreeServertmpb > /dev/null 2>&1
rm -f $FreeServertmpa* $FreeServertmpb*