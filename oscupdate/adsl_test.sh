#!/bin/sh
echo
wget -qO- http://ipecho.net/plain | xargs echo -e "Your IP Address is:\n"
echo
echo ' Now we begin with :'
echo
echo '================================='
echo '          FAST.COM               '
echo '================================='
python <<HEREDOC
import sys
sys.path.insert(1, '/oscupdate')
import fast_com
print 'your Bandwidth speed is:\n\n'+  str(fast_com.fast_com(maxtime=6))+' Mb/s\n\n'
HEREDOC
echo 
echo ' And Now with :'
echo '================================='
echo '          MIRE ADSL              '
echo '================================='
python /oscupdate/mire.py &&
echo
echo
echo ' And Now with :'
echo '================================='
echo '             OOKLA               '
echo '================================='
echo
aa=$(/oscupdate/speedtest --accept-license)
echo "$aa" | awk 'NR == 7 || /PATTERN/'
echo