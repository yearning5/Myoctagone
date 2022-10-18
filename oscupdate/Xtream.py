import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
# janberyan.com
import urllib2
# xtream to m3u
import random
url=raw_input('enter url without hhtp://   =')
#port=raw_input('enter port   =')
user=raw_input('enter user   =')
passs=raw_input('enter password   =')

#link='http://'+url+':'+port+'/get.php?username='+user+'&password='+passs+'&type=m3u&output=ts'
link='http://'+url+'/get.php?username='+user+'&password='+passs+'&type=m3u&output=ts'
a=urllib2.urlopen(link)
#a=urllib2.urlopen('http://beryantv.com:25461/get.php?username=000422001200140&password=000422001200140&type=m3u&output=ts')
aa=a.readlines()
m3uf=[]
for line in aa:
    if line.strip():
        if '#EXTVLCOPT' not in line:
            m3uf.append(line)
tmmp='/tmp/'+'xtream'+str(random.randrange(1000,9999))+'.m3u'
fid=open(tmmp,'w')
for l in m3uf:
    fid.write(l)
fid.close()
# the first line containing channel name
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break


if os.path.isfile('/etc/enigma2/userbouquet.xtream__tv_.tv'):
    ax='xtream'+str(random.randrange(1000,9999))
    with open('/etc/enigma2/bouquets.tv','r') as f: our=f.readlines()
    if not any(ax in s for s in our):
        with open('/etc/enigma2/bouquets.tv','a') as f: f.write('#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+ax+'__tv_.tv" ORDER BY bouquet\n')
else:
    ax='xtream'
    with open('/etc/enigma2/bouquets.tv','r') as f: our=f.readlines()
    if not any(ax in s for s in our):
        with open('/etc/enigma2/bouquets.tv','a') as f: f.write('#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+ax+'__tv_.tv" ORDER BY bouquet\n')

file=open('/etc/enigma2/userbouquet.'+ax+'__tv_.tv','w')
file.write('#NAME '+ax+' (TV)\n')
while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        channel=re.sub(r'\s\W+', '', channel)
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+':'+channel+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
file.close()
