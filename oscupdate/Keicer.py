#import requests
#import re
#from datetime import date, timedelta
#import datetime
#import time
# http://www.iptvgift.com
#username='57901537460525'
#password='57901537460525'
#username=raw_input('username=')
#password=raw_input('password=')
#lim='http://24.thgss.com:8000/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
#lim='http://mhiptv.com:8888/get.php?username='+username+'&password='+password+'&type=m3u&output=ts'
import os
from glob import glob
glob_pattern = os.path.join('/tmp', '*.m3u') # * means all if need specific format then *.m3u
aa= sorted(glob(glob_pattern), key=os.path.getctime)

'''aa=[]
for i in a:
    if 'alkaicer' in i and '.m3u' in i:
        aa.append(i)
'''
if len(aa)>0:
    locatf=aa[-1]
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
    if os.path.isfile('/etc/enigma2/userbouquet.Keicer__tv.tv'):
        os.remove('/etc/enigma2/userbouquet.Keicer__tv_.tv')
        file=open('/etc/enigma2/userbouquet.Keicer__tv_.tv','w')
        file.close()
    file=open('/etc/enigma2/userbouquet.Keicer__tv_.tv','w')
    file.write('#NAME Keicer (TV)\n')
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

else:
    print '============================'
    print '       '
    print 'Please check " /tmp "  folder for'
    print 'alkeicer m3u file or duplication'
    print 'Exit without update'
    print '       '
    print '============================'


