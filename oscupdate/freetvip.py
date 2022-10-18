import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
tday=datetime.datetime.today().strftime('%d')
tmonth=datetime.datetime.today().strftime('%m')
tyear=datetime.datetime.today().strftime('%Y')
tdate=(datetime.datetime.today()+timedelta(1)).strftime('%d-%m-%Y')
#tdate=(datetime.datetime.today()- timedelta(1)).strftime('%d-%m-%Y')
#link='https://www.iptv4sat.com/'+tyear+'/'+tmonth+'/'
link='http://www.freetvip.com/'
f = requests.get(link)
the_page = f.text
the_page =the_page.encode('ascii', 'ignore')
c=re.findall('href="(.*?).m3u"',the_page,re.DOTALL)
for i in c:
    if len(i)<100:
        if 'sport' in i.lower():
            sportlin=i+'.m3u'
        elif 'arab' in i.lower():
            normallin=i+'.m3u'
        elif 'europ' in i.lower():
            movielin=i+'.m3u'
#SPORT
f = requests.get(sportlin)
ttx=f.text.encode('ascii', 'ignore').split('\r')
locatf='/tmp/freetvip_sport..m3u'
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
m3ufl.close
file=open('/etc/enigma2/userbouquet.autoiptv_sport__tv_.tv','w')
file.write('#NAME autoiptv_sport (TV)\n')

for i in range(len(m3uf)):
    if 'http:' in m3uf[i]:
        channel=m3uf[i-1].split(',')[1]
        chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel)
file.close()
      
#NORMAL
f = requests.get(normallin)
ttx=f.text.encode('ascii', 'ignore').split('\r')
locatf='/tmp/freetvip_normal..m3u'
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
m3ufl.close
file=open('/etc/enigma2/userbouquet.autoiptv_normal__tv_.tv','w')
file.write('#NAME autoiptv_normal (TV)\n')

for i in range(len(m3uf)):
    if 'http:' in m3uf[i]:
        channel=m3uf[i-1].split(',')[1]
        chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel)
file.close()

#MOVIE
f = requests.get(movielin)
ttx=f.text.encode('ascii', 'ignore').split('\r')
locatf='/tmp/freetvip_movie..m3u'
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
m3ufl.close
file=open('/etc/enigma2/userbouquet.autoiptv_movie__tv_.tv','w')
file.write('#NAME autoiptv_movie (TV)\n')

for i in range(len(m3uf)):
    if 'http:' in m3uf[i]:
        channel=m3uf[i-1].split(',')[1]
        chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel)
file.close()
