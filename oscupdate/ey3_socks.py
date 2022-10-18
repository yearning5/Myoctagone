import requests,re,os,random,string,socks
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#  trough socks 5 proxy
ccc=['UA','SG','US','ZA','DE','CN','IN','FR','RU','GP','ID','GB']
params = (
    ('request', 'getproxies'),
    ('protocol', 'socks5'),
    ('timeout', '1000'),
    ('country', random.shuffle(ccc)),
)

if os.path.exists('/tmp/d1.txt') and os.path.getsize('/tmp/d1.txt') > 0:
    with open('/tmp/d1.txt') as f1:
        d1=f1.read().split('\n')
else:
    response = requests.get('https://api.proxyscrape.com/v2/', params=params,verify=False)
    with open('/tmp/d1.txt','w') as f:
        f.write(response.text.encode('ascii','ignore').replace('\r',''))
    d1=response.text.encode('ascii','ignore').split()
def socksss5(): 
    random.shuffle(d1)
    for i in d1:
        try:
            proxies = {'http': "socks5h://"+i}
            a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=5).text
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

    return out
ss=socksss5()
ip=ss[1] # change your proxy's ip
port = int(ss[2]) # change your proxy's port
prx=ip+':'+str(port)
print prx
'''
def socks55(ip,port):
    import socket
    import socks
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket
    return
# ===============================================
#             go throught sockets proxy    
# ===============================================
socks55(ip,port)
execfile('/oscupdate/getiip.py')'''
proxies = {'http': "socks5h://"+prx}

tsts1=requests.get('http://ip-api.com/json', proxies=proxies).text
print tsts1
usser=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
print usser

def getcookies(ln):
    import requests
    a_session = requests.Session()
    a_session.get(ln,verify=False,proxies=proxies)
    session_cookies = a_session.cookies
    cookies_dictionary = session_cookies.get_dict()
    return cookies_dictionary

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://eyetv.club',
    'Connection': 'keep-alive',
    'Referer': 'https://eyetv.club/index.php',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
}

try:
    coo1=getcookies('https://eyetv.club/index.php')
    
    r1 = requests.get('https://eyetv.club/index.php', headers=headers1, cookies=coo1,proxies=proxies,verify=False)
    data = {
      'username': usser,
      'bouquet': '0'
    }
    
    r2 = requests.post('https://eyetv.club/index.php', headers=headers2, cookies=coo1, data=data,proxies=proxies,verify=False)
    
    ll1='https://eyetv.club//godownload.php?uri='+usser+'&bouquet=0'
    
    r3=requests.get(ll1, headers=headers1, cookies=coo1,proxies=proxies,verify=False)
    ll2=re.findall('value="(http://eyetv.site:8080/get.php.*?)"',r3.text,re.DOTALL)[0].replace('amp;','')
    userr=re.findall('username=(.*?)&',ll2)[0]
    passs=re.findall('password=(.*?)&',ll2)[0]
    
    if os.stat('/etc/enigma2/userbouquet.eye_3days__tv_.tv').st_size != 0:
        with open(r'/etc/enigma2/userbouquet.eye_3days__tv_.tv','r') as f:
            ff=f.readlines()
        f1= open(r'/etc/enigma2/userbouquet.eye_3days__tv_.tv','w')
        #print "old user : "+i.split('/')[3]
        #print "old pass : "+i.split('/')[4]
        for i in ff:
            if '#SERVICE' in i:
                i=i.replace(i.split('/')[3],userr).replace(i.split('/')[4],passs)
            f1.write(i)
        f1.close()
        with open(r'/etc/enigma2/xstreamity/playlists.txt') as f:
            ff=f.read()
        
        u1=re.findall('http://eyetv.site.*username=(.*?)&',ff)[0]
        p1=re.findall('http://eyetv.site.*password=(.*?)&',ff)[0]
        with open(r'/etc/enigma2/xstreamity/playlists.txt','w') as f:
            f.write(ff.replace(u1,userr).replace(p1,passs))
except:
    pass

# ===============================================
#             going back to original sockets proxy    
# ===============================================
        
socks.setdefaultproxy()