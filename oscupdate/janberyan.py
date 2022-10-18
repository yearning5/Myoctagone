import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
# janberyan.com
import urllib2
user=raw_input('user= ')
passs=raw_input('pass= ')
link='http://iptv-janberyan.com:25461/get.php?username='+user+'&password='+passs+'&type=m3u&output=mpegts'
m3uf=[]
for line in urllib2.urlopen(link):
    if line.strip():
        if '#EXTVLCOPT' not in line:
            m3uf.append(line)

# the first line containing channel name
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break
if os.path.isfile('/etc/enigma2/userbouquet.janberyan__tv_.tv'):
    os.remove('/etc/enigma2/userbouquet.janberyan__tv_.tv')
    file=open('/etc/enigma2/userbouquet.janberyan__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.janberyan__tv_.tv','w')
file.write('#NAME janberyan (TV)\n')
while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+':'+channel+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
file.close()
