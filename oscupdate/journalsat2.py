import requests
import re
import os, sys
from datetime import date, timedelta
import datetime
import time
import urllib3
import random
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

#iptt=raw_input('which iptv to generate\n"thgss"=1\n"vtpii"=2\n"Alkaicer"=3\n"journalsat"=4\n   ')
#stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')

#iptt='4'
stream='5001'

srr=['4097','5001','5002','']
if stream not in srr:
    print 'please enter number from 4097 5001 or 5002\n'
    stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
    if stream not in srr:
        print "you didn't enter number from 4097 5001 or 5002 the program will exit\n"
        sys.exit()
now=datetime.datetime.now()

def iptt():
    name='journalsat'
    cookies = {
        '__gads': 'ID=22c68f5a1cab1630-22d5855153c900e4:T=1625343653:RT=1625343653:S=ALNI_MbhliPUh3fJsRAQ3bCOy8UTH0tnhA',
        '_ga': 'GA1.2.1850125005.1625343678',
        '_gid': 'GA1.2.1991746237.1625343683',
        'uername': ID,
        'ip': ip,
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625343763449],null,null]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    r1 = requests.get('http://iptv.journalsat.com/random/index.php', headers=headers, cookies=cookies)


    cookies = {
        '__gads': 'ID=22c68f5a1cab1630-22d5855153c900e4:T=1625343653:RT=1625343653:S=ALNI_MbhliPUh3fJsRAQ3bCOy8UTH0tnhA',
        '_ga': 'GA1.2.1850125005.1625343678',
        '_gid': 'GA1.2.1991746237.1625343683',
        'uername': ID,
        'ip': ip,
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625343854428],null,null]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://iptv.journalsat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://iptv.journalsat.com/random/index.php',
        'Upgrade-Insecure-Requests': '1',
    }

    r2 = requests.post('http://iptv.journalsat.com/random/index.php', headers=headers, cookies=cookies)


    cookies = {
        '__gads': 'ID=22c68f5a1cab1630-22d5855153c900e4:T=1625343653:RT=1625343653:S=ALNI_MbhliPUh3fJsRAQ3bCOy8UTH0tnhA',
        '_ga': 'GA1.2.1850125005.1625343678',
        '_gid': 'GA1.2.1991746237.1625343683',
        'uername': ID,
        'ip': ip,
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625343854428],null,null]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://iptv.journalsat.com/random/index.php',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    r3 = requests.get('http://iptv.journalsat.com/random/get.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')



    cookies = {
        '__gads': 'ID=22c68f5a1cab1630-22d5855153c900e4:T=1625343653:RT=1625343653:S=ALNI_MbhliPUh3fJsRAQ3bCOy8UTH0tnhA',
        '_ga': 'GA1.2.1850125005.1625343678',
        '_gid': 'GA1.2.1991746237.1625343683',
        'uername': ID,
        'ip': ip,
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625344332893],null,null]',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://iptv.journalsat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://iptv.journalsat.com/random/get.php',
        'Upgrade-Insecure-Requests': '1',
    }

    params = (
        ('do', 'cccam'),
    )

    data = {
      'do': 'cccam',
      'doccam': 'generate'
    }

    r4 = requests.post('http://iptv.journalsat.com/random/get.php', headers=headers, params=params, cookies=cookies, data=data).text.encode('ascii','ignore')

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.post('http://iptv.journalsat.com/random/get.php?do=cccam', headers=headers, cookies=cookies, data=data)
    host=re.findall('"text-white">(.*?)<',r4,re.DOTALL)[0]
    username=re.findall('"text-white">(.*?)<',r4,re.DOTALL)[1]
    password=re.findall('"text-white">(.*?)<',r4,re.DOTALL)[2]
    liin=re.findall(' href=\'(http://iptv.*?)\'',r4,re.DOTALL)[0]
    print liin
    for i in range(10):
        f=requests.get(liin,headers=UserAgent)
        ttx=f.text.encode('ascii', 'ignore').split('\r')
        if ttx != ['']:
            print "  Donne After "+str(i+1)+"  iterations"
            break
        else:
            print 'list is empty'

    #print ttx

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
    with open(r'/oscupdate/journalsat_check.txt','w') as f:
        f.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+'\n'+ID)
    return

# get ip address

a12=requests.get('http://ip-api.com/json').text.encode('ascii','ignore')
ip=eval(a12)['query']
print ip
if not os.path.exists(r'/oscupdate/journalsat_check.txt'):
    ID=str(random.randint(100000000, 999999999))
    print ' a new  ID will be Used '+ID
    a1 =iptt()
else:
    with open(r'/oscupdate/journalsat_check.txt','r') as f:
        aaa=f.readlines()
        aa=aaa[0].split(':')
    dif=((now.year-float(aa[0]))* (365*24*60*60)+(now.month-float(aa[1]))* (730*60*60)+(now.day-float(aa[2]))* (24*60*60)+(now.hour-float(aa[3]))* (60*60)+(now.minute-float(aa[4]))* (60)+now.second-float(aa[5]))/3600
    print 'Actual ID is '+aaa[1]+' === "_" === '
    if dif > 6:
        ID=str(random.randint(100000000, 999999999))
        print ' MORE than 6 Hours a new  ID will be Used '+ID
        a1 =iptt()
    else:
        print ' THE same ID will be Used '+aaa[1]
        ID=aaa[1]
        a1 =iptt()


