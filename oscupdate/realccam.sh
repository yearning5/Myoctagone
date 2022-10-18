##!/bin/sh
#*******************************************#
#   E2-MyOpenVPN-SERVICE  By YASSINOV       #
#          Build 28032019 Reloaded          # 
#      Forum/Support:www.yassinov.com       #       
#*******************************************#

cd /tmp
FreeServer=/tmp/realcam.txt
FreeServertmpa=/tmp/freeservra*
FreeServertmpb=/tmp/freeservrb*
FreeServertmpe=/tmp/freeservre*
HTTPSERV70="https://www.realcccam.com/freecccam.php"
FreeServertmpb70=/tmp/freeservrb70
FreeServertmpb71=/tmp/freeservrb71
FreeServertmpb72=/tmp/freeservrb72
FreeServertmpa70=/tmp/freeservra70
FreeServertmpa71=/tmp/freeservra71
FreeServertmpa72=/tmp/freeservra72

wget -O $FreeServertmpa70 $HTTPSERV70 > /dev/null 2>&1
sed -ne 's#.*name="Username"  value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb70
sed -ne 's#.*name="Password"  value="\([^"<]*\).*#\1#p' $FreeServertmpa70 > $FreeServertmpb71
curl -d "Username=$(<freeservrb70)&Password=$(<freeservrb71)&submit=addf&addf=5 Days Free Cline" -X POST https://www.realcccam.com/freecccam.php > $FreeServertmpa71 
sed -ne 's#.*class="btn-primary btn-lg">\([^<]*\).*#\1#p' $FreeServertmpa71 > $FreeServertmpb72
cat $FreeServertmpb72 >> $FreeServer

rm -f $FreeServertmpa > /dev/null 2>&1
rm -f $FreeServertmpb > /dev/null 2>&1
rm -f $FreeServertmpa* $FreeServertmpb*