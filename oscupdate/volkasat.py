# -*- coding: utf-8 -*-
import sys

PY3=sys.version_info[0]

import requests,re , random , string, os
import urllib3
urllib3.disable_warnings()


for i in range(10):
    USERR=''.join((random.choice(string.digits) for x in range(9)))
    if USERR[0]!=0:
        break
UserAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; Linux x86_64; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Safari/537.36',
            'Accept': 'text/html'}


try:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    r = requests.get('http://iptv.volkasat.com/', headers=headers)

    cookies = {
        '_ga_8Z5QQ2FBN1': 'GS1.1.1647536866.1.0.1647536866.0',
        '_ga': 'GA1.1.1159320973.1647536866',
        '__gads': 'ID=43a1fb92569607e4-227a2fa5b3d100ce:T=1647536868:RT=1647536868:S=ALNI_MbgSDA-XYwJKwfbS3gOkWEpS_HDUA',
        'FCNEC': '[[AKsRol8yVQlTReDD_hQS7byN4m-sbMzFI0zwaPMDSXLqDpTW8jiwSJAE_ETW0PWannwbxg91wcD7w7I9Mg9PzZiE_hqruxTmn58IZMT3VReFlji7Lg4QPvDkDyjdXztSRuWBVZCYhLeTmw6SLD0qGeMpkUANq18P6w==],null,[]]',
        'cookieconsent_status': 'dismiss',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Origin': 'http://iptv.volkasat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://iptv.volkasat.com/',
        'Upgrade-Insecure-Requests': '1',
    }

    r2 = requests.post('http://iptv.volkasat.com/index.php', headers=headers, cookies=cookies).text

    cookies = {
        '_ga_8Z5QQ2FBN1': 'GS1.1.1647536866.1.1.1647537003.0',
        '_ga': 'GA1.1.1159320973.1647536866',
        '__gads': 'ID=43a1fb92569607e4-227a2fa5b3d100ce:T=1647536868:RT=1647536868:S=ALNI_MbgSDA-XYwJKwfbS3gOkWEpS_HDUA',
        'cookieconsent_status': 'dismiss',
        'uername': USERR,
        'FCNEC': '[[AKsRol-T1z6lHVK_6CihpiMybdvixzc6Qe1MSyMfPbxxdoYHY4KeiQE4NVYn9smbD60AUTQJPpqa-SNpK51thLoAXbSk2LFX1aljfAIiJzN6qIXxy9e4gCUnZpnjItTnaSd03bYdCSNDNS_ks0n48g5oFffL--NqXg==],null,[]]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://iptv.volkasat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://iptv.volkasat.com/get.php',
        'Upgrade-Insecure-Requests': '1',
    }

    params = (
        ('do', 'cccam'),
    )

    data = {
      'do': 'cccam',
      'doccam': 'generate'
    }

    r3 = requests.post('http://iptv.volkasat.com/get.php', headers=headers, params=params, cookies=cookies, data=data).text

    l1=re.findall("href='(.*?)'",r3)
    liin=[i for i in l1 if 'm3u' in i][0]

    print (liin)
    with open('/tmp/volkasat_link.txt','w') as f12:
        f12.write(liin)
    print ('volkasat_link file written')
    try:
        with  open('/etc/enigma2/xstreamity/playlists.txt','r') as f:
            ff=f.read()
        u1=re.findall('http://iptv.volkasat.com:25461/get.php?username=(.*?)&pa',ff)[0]
        newff=ff.replace('http://iptv.volkasat.com:25461/get.php?username='+u1,'http://iptv.volkasat.com:25461/get.php?username='+USERR)
        with  open('/etc/enigma2/xstreamity/playlists.txt','w') as f:
            f.write(newff)
    except:
        pass
    for i in range(10):
        f=requests.get(liin,headers=UserAgent)
        ttx=f.text.encode('ascii', 'ignore').split('\r')
        if ttx != ['']:
            print ("  Donne After "+str(i+1)+"  iterations")
            break

    #print ttx
    name='volkasat'
    stream='5001'
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
except:
    print('\n not workeing ..................\n')