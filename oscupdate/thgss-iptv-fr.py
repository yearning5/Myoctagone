import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
# http://101k.tk/
#username='57901537460525'
#password='57901537460525'
username=str(input('username FR='))
password=username
#password=str(input('password='))
lim='http://pp.thgss.com:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
f = requests.get(lim,timeout=10)
ttx=f.text.encode('ascii', 'ignore').split('\r')
locatf='/tmp/new-fr..m3u'
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
if os.path.isfile('/etc/enigma2/userbouquet.things-FR__tv_.tv'):
    os.remove('/etc/enigma2/userbouquet.things-FR__tv_.tv')
    file=open('/etc/enigma2/userbouquet.things-FR__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.things-FR__tv_.tv','w')
file.write('#NAME things-FR (TV)\n')
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
# filter some to nailesat sport
file=open('/etc/enigma2/userbouquet.things-FR__tv_.tv','r')
things=file.readlines()
file.close()
fltlines=[]
fltch=['piwi','bara','jeem','tiji','kids','teletoo','zouzou']
for lin in things:
    if any(nn in lin.lower() for nn in fltch):
    	if not any (nn in lin.lower() for nn in ['cn','maj','kara','sem','toyo','spac','==']):
	    	fltlines.append(lin)
file=open('/etc/enigma2/userbouquet.nilesat_sports__tv_.tv','r')
ilesat_sports=file.readlines()
file.close()
nilesat_sports=[]
for i in ilesat_sports:
    if not any(x in i for x in ('4097:0:1:0:0','#DESCRIPTION')):
        nilesat_sports.append(i)
for i in fltlines:
    nilesat_sports.append(i)
file=open('/etc/enigma2/userbouquet.nilesat_sports__tv_.tv','w')
for i in nilesat_sports:
    file.write(i)
file.close()

