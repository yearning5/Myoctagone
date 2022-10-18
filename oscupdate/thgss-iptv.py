import requests
import re
import os, sys
from datetime import date, timedelta
import datetime
import time
import urllib3
urllib3.disable_warnings()

UserAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; Linux x86_64; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Safari/537.36',
            'Accept': 'text/html'}

# http://101k.tk/
#username='57901537460525'
#password='57901537460525'
def uri_validator(x):
    try:
        result = requests.get(x,headers=UserAgent,timeout=4.0,verify=False)
        if result.ok:
            return True
        else:
            return False
    except:
        return False

iptt=raw_input('which iptv to generate\n"thgss"=1\n"vtpii"=2\n"Alkaicer"=3\n"journalsat"=4\n"sniperstv"=5\n"freeiptvgen"=6\n "iptvplusx"=7\n      ')
stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')

srr=['4097','5001','5002']
if stream not in srr:
    print 'please enter number from 4097 5001 or 5002\n'
    stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
    if stream not in srr:
        print "you didn't enter number from 4097 5001 or 5002 the program will exit\n"
        sys.exit()

if iptt=='1':
    name='things'
    username=str(raw_input('username='))
    #password=username
    password=str(raw_input('password='))
    lim0='http://24.thgss.com:8000/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
    lim1='http://62.210.178.16:8008/get.php?username='+password+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim2='http://ar.thgss.com:25461/get.php?username='+password+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim3='http://188.166.35.190:25461/get.php?username='+password+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim4='http://pp.thgss.com:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim5='http://free24ip.xyz:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim6='http://tv.free24ip.xyz:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim=[lim0,lim1,lim2,lim3,lim4]
    f=requests.get(lim6,headers=UserAgent,timeout=5.0,verify=False)
    '''for i in lim:
        if uri_validator(i):
            f=requests.get(i,headers=UserAgent,timeout=5.0,verify=False)
            break'''
    ttx=f.text.encode('ascii', 'ignore').split('\r')
#locatf='/tmp/new_'+name+'.m3u'
elif iptt=='2':
    name='vtpii'
    username=str(raw_input('username='))
    password=str(raw_input('password='))
    #password=str(input('password='))
    lim0='http://vtpii.net:8000/get.php?username='+username+'&password='+password+'&type=m3u&output=ts'
    lim1='http://vt.vttpi.com:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim2='http://vttpi.co:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim=[lim0,lim1,lim2]
    for i in lim:
        if uri_validator(i):
            f=requests.get(i,headers=UserAgent,timeout=5.0,verify=False)
            break
    ttx=f.text.encode('ascii', 'ignore').split('\r')
elif iptt=='3':
    name='Alkaicer'
    username=str(raw_input('username='))
    password=str(raw_input('password='))
    lim='http://iptv.allkaicerteam.com:8080/get.php?username='+username+'&password='+password+'&type=m3u'
    if uri_validator(lim):
        f=requests.get(lim,headers=UserAgent,timeout=5.0,verify=False)
    ttx1=f.text.encode('ascii', 'ignore')
    m3uf=[i.strip('\r') for i in ttx1.split('\n')]
    fr=[]
    for i,s in enumerate(m3uf):
        if 'fajer' in s.lower():
            fr.append(s)
            fr.append(m3uf[i+1])
            i=i+2
    ttx=[]
    ttx.append('#EXTM3U\n')
    for i in fr:
        ttx.append(i+'\n')
    i=1
    while i<len(m3uf):
        ttx.append(m3uf[i]+'\n')
        i=i+1
elif iptt=='4':
    name='journalsat'
    cookies = {
        '_ga': 'GA1.2.1444096135.1619435351',
        '_gid': 'GA1.2.1100187472.1619435351',
        '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
        '_gat_gtag_UA_131846294_1': '1',
        'FCCDCF': '[null,null,["[[],[],[],[],null,null,true]",1619435418969],null,null]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://iptv.journalsat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://iptv.journalsat.com/',
        'Upgrade-Insecure-Requests': '1',
    }

    r1 = requests.post('http://iptv.journalsat.com/index.php', headers=headers, cookies=cookies)



    cookies = {
        '_ga': 'GA1.2.884653929.1619435494',
        '_gid': 'GA1.2.1063229768.1619435494',
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Content-Length': '0',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://iptv.journalsat.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://iptv.journalsat.com/index.php',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    r2 = requests.post('http://iptv.journalsat.com/index.php', headers=headers, cookies=cookies, verify=False)

    import random
    a=str(random.randint(100000000, 999999999))
    cookies = {
        '_ga': 'GA1.2.884653929.1619435494',
        '_gid': 'GA1.2.1063229768.1619435494',
        'uername': a,
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://iptv.journalsat.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://iptv.journalsat.com/get.php',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('do', 'cccam'),
    )

    data = {
      'do': 'cccam',
      'doccam': 'generate'
    }

    r3 = requests.post('http://iptv.journalsat.com/get.php', headers=headers, params=params, cookies=cookies, data=data, verify=False).text.encode('ascii','ignore')
    host=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[0]
    username=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[1]
    password=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[2]
    liin=re.findall(' href=\'(http://iptv.*?)\'',r3,re.DOTALL)[0]
    f=requests.get(liin,headers=UserAgent,timeout=1.0,verify=False)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
elif iptt=='5':
    name='sniperstv'
    username=str(raw_input('username='))
    password=str(raw_input('password='))
    #password=str(input('password='))
    lim0='http://jokertv.link:25461/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
    lim1='http://jokertv.link:8080/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'

    lim=[lim0,lim1]
    for i in lim:
        if uri_validator(i):
            f=requests.get(i,headers=UserAgent,timeout=5.0,verify=False)
            break
    ttx=f.text.encode('ascii', 'ignore').split('\r')
elif iptt=='6':
    name='freeiptvgen'
    username=str(raw_input('username='))
    password=str(raw_input('password='))
    #password=str(input('password='))
    lim0='http://freeiptvgen.com:25461/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
    #lim1='http://freeiptvgen.com:25461/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
    #lim1='http://jokertv.link:8080/get.php?username='+username+'&password='+password+'&type=m3u&output=mpegts'
    lim=[lim0]
    for i in lim:
        if uri_validator(i):
            f=requests.get(i,headers=UserAgent,timeout=10.0,verify=False)
            break
    ttx=f.text.encode('ascii', 'ignore').split('\r')
elif iptt=='7':
    name='iptvplusx'
    username=str(raw_input('username='))
    password=str(raw_input('password='))
    #password=str(input('password='))
    lim0='http://iptv.iptvplusx.com:8000/get.php?username='+username+'&password='+password+'&type=m3u_plus&output=mpegts'
    lim=[lim0]
    for i in lim:
        if uri_validator(i):
            f=requests.get(i,headers=UserAgent,timeout=5.0,verify=False)
            break
    ttx=f.text.encode('ascii', 'ignore').split('\r')
#bouquets
bouq=open('/etc/enigma2/bouquets.tv','r')
bo=bouq.read()
bouq.close()
if name not in bo:
    new='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+name+'__tv_.tv" ORDER BY bouquet\n'
    file=open('/etc/enigma2/bouquets.tv','a')
    file.write(new)
    file.close()

locatf='/tmp/new_'+name+'.m3u'

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
bein=[]
for i in range(0,len(m3uf[1:])-1,2):
    if 'bein' in m3uf[1:][i].lower():
        bein.append(m3uf[1:][i])
        bein.append(m3uf[1:][i+1])

fr=[]

for i in range(0,len(m3uf[1:])-1,2):
    if 'rmc' in m3uf[1:][i].lower():
        fr.append(m3uf[1:][i])
        fr.append(m3uf[1:][i+1])

OSN=[]
for i in range(0,len(m3uf[1:])-1,2):
    if 'osn' in m3uf[1:][i].lower():
        OSN.append(m3uf[1:][i])
        OSN.append(m3uf[1:][i+1])


m3uf=['#EXTM3U\n']+bein+fr+OSN+[i for i in m3uf[1:] if i not in (bein + OSN +fr) ]
# the first line containing channel name
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break
if os.path.isfile('/etc/enigma2/userbouquet.'+name+'__tv_.tv'):
    os.remove('/etc/enigma2/userbouquet.'+name+'__tv_.tv')
    file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
file.write('#NAME '+name+' (TV)\n')
while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+':'+channel+'\n'
        channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
file.close()
