# -*- coding: utf-8 -*-
import sys

PY3=sys.version_info[0]
import requests, random, string,os, os,socks
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#  trough socks 5 proxy
ccc=['all']#'US','IN','DE','CN','IN','RU']
params = (
    ('request', 'getproxies'),
    ('protocol', 'socks5'),
    ('timeout', '1000'),
    ('country', random.choice(random.sample(ccc,len(ccc)))),
)

if os.path.exists('/tmp/d1.txt') and os.path.getsize('/tmp/d1.txt') > 0:
    with open('/tmp/d1.txt') as f1:
        d1=f1.read().split('\n')

else:
    response = requests.get('https://api.proxyscrape.com/v2/', params=params,verify=False)
    #'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'
    with open('/tmp/d1.txt','w') as f:
        f.write(response.text.replace('\r',''))
    d1=response.text.split()
def socksss5():
    random.shuffle(d1)
    try:

        for i in d1:
            try:
                proxies = {'http': "socks5h://"+i}
                a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=5,verify=False).text
                if a:
                    c=eval(a)['country']
                    ip=eval(a)['query']
                    portt=i.split(':')[1]
                    cit_reg=eval(a)['city']+'_'+eval(a)['regionName']
                    #lisst.append(i)
                    out=[i,ip,portt,cit_reg,c]
                    break
            except:
                pass
    except:
        out=''

    return out

def trtr():
    nn=0
    while nn<1000:
        userr=''.join(random.choice(string.digits) for _ in range(7))
        if userr[0]!='0':
            break
        nn=nn+1

    freer=nrand()
    s = requests.session()
    s.cookies.clear()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    response = s.get('https://freeiptvgen.com/', headers=headers, proxies=proxies,verify=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://freeiptvgen.com',
        'Connection': 'keep-alive',
        'Referer': 'https://freeiptvgen.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    data = {
      'id': '948440',
      'username': userr,
      'userbq': 'All',
      'reffreer': freer,
      'thesite': 'https://freeiptvgen.com/'
    }


    response = s.post('https://www.freeiptvgen.com:5744/inserttotable', headers=headers, data=data, proxies=proxies,verify=False)

    df1=response.text
    s.cookies.clear()
    #print df1+' '+userr+' '+freer

    return [df1,userr,freer]



def nrand():
    vowels = 'aeiou'
    consonants = 'bcdfghijklmnpqrstvwxz'
    f0=random.choice(list(consonants))+random.choice(list(vowels))
    f1=random.choice(list(consonants))+random.choice(list(vowels))
    f2=random.choice(list(consonants))+random.choice(list(vowels))
    f=f0+f1+f2
    return f

#print trtr()

for i in range(10):
    for j in range(5):
        #print i
        ss=socksss5()
        ip=ss[1] # change your proxy's ip
        port = int(ss[2]) # change your proxy's port
        prx=ip+':'+str(port)

        proxies = {'http': "socks5h://"+prx}

        tsts1=requests.get('http://ip-api.com/json', proxies=proxies,verify=False).text
        if tsts1:
            print (prx)
            print (tsts1)
            break
    dsf=trtr()
    print (dsf)
    if 'success' in dsf[0]:
        userr12=dsf[-2]
        with open(r'/etc/enigma2/userbouquet.freeiptvgen__tv_.tv','r') as f:
            fil=f.readlines()

        with open(r'/etc/enigma2/userbouquet.freeiptvgen__tv_.tv','w') as f:
            for ij in fil:
                if 'http' in ij :
                    ij=ij.replace(ij.split('/')[3],userr12)
                f.write(ij)
        break
print (i)
print ('After ' + str(i+1)+' iterations')
print (str(dsf[0])+'\n')
print (str(dsf[1])+'\n')








a=os.popen('wget -qO - http://127.0.0.1/web/servicelistreload?mode=2')
print (a.read())

with open('/tmp/freeiptvgen.txt','w') as f:
    f.write(dsf[0]+'\n')
    f.write(dsf[1]+'\n')
