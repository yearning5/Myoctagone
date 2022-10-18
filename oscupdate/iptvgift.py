import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
# http://www.iptvgift.com
#username='57901537460525'
#password='57901537460525'
#username=raw_input('username=')
#password=raw_input('password=')
#lim='http://24.thgss.com:8000/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
#lim='http://mhiptv.com:8888/get.php?username='+username+'&password='+password+'&type=m3u&output=ts'
a=requests.get('https://www.iptvgift.com/')
aa=a.text.encode('ascii', 'ignore').strip('\r')
lim=re.findall('href="(https://goo.gl.*?)"',aa,re.DOTALL)[0]
f = requests.get(lim)
ttx=f.text.encode('ascii', 'ignore').split('\r')
locatf='/tmp/iptvgift.m3u'
d=open(locatf,'w')
for i in ttx:
    d.write(i)
d.close()

m3ufl = open(locatf,'r')
m3uf = m3ufl.readlines()
m3ufl.close
m3ufl = open(locatf,'w')
for line in m3uf:
    if line.strip():
        if '#EXTVLCOPT' not in line:
            m3ufl.write(line)
m3ufl.close
m3ufl = open(locatf,'r')
m3uf = m3ufl.readlines()
m3ufl.close()
# the first line containing channel name
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break
if os.path.isfile('/etc/enigma2/userbouquet.iptvgift__tv_.tv.tv'):
    os.remove('/etc/enigma2/userbouquet.iptvgift__tv_.tv')
    file=open('/etc/enigma2/userbouquet.iptvgift__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.iptvgift__tv_.tv','w')
file.write('#NAME iptvgift (TV)\n')
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
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break
kodi=open('/tmp/iptvgift.xml','w')
kodi.write('<streamingInfos>\n')
while i <len(m3uf)-1:
    channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
    channel=channel.strip('\r')
    a1=m3uf[i+1].strip('\n')
    channelurl=a1.strip('\r')
    kodi.write('<streaminginfo>\n')
    #kodi.write('\t<cname>'+channel+'</cname>\n')
    kodi.write('\t<item>\n')
    kodi.write('\t<title>'+channel+'<title>\n')
    kodi.write('\t<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+channelurl+'</link>\n')
    kodi.write('\t</item>\n')
    kodi.write('</streaminginfo>\n')
    i = i+2
kodi.write('</streamingInfos>\n')
kodi.close()
