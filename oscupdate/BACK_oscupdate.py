import urllib2
import urllib
import base64
import os
import os.path
import requests
from six.moves.urllib.request import urlopen
import urllib2,cookielib
from urllib2 import Request, urlopen
import httplib
#from datetime import datetime
#startTime = datetime.now()
import socket
import datetime
import time
from datetime import date, timedelta
import subprocess
import re,random,string
#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"
import urllib3
urllib3.disable_warnings()
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
now1=datetime.datetime.now()

'''
p=open('/etc/image-version','r')
pp=p.readlines()
p.close()
for i in pp:
    if 'creator' in i.lower():
        image_v=i.split('=')[1]'''

image_v=subprocess.check_output('grep "."  /etc/issue | tail -1',shell=True)[:-6]

if 'pkt' in image_v.lower():
    source='/var/keys/oscam.server'
    source_wic='/var/keys/wicardd.conf'
    pkt_cp='cp /var/keys/oscam.server /var/keys/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /var/keys/oscam.server /var/keys/gcam.server > /dev/null 2>&1'

elif 'vix' in image_v.lower():
    source='/etc/tuxbox/config/oscam.server'
    source_wic='/etc/tuxbox/config/wicardd.conf'
    pkt_cp='cp /etc/tuxbox/config/oscam.server /etc/tuxbox/config/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /etc/tuxbox/config/oscam.server /etc/tuxbox/config/gcam.server > /dev/null 2>&1'
else:
    source='/etc/tuxbox/oscam-emu/oscam.server'
    source_wic='/etc/tuxbox/config/wicardd.conf'
    pkt_cp='cp /etc/tuxbox/oscam-emu/oscam.server /etc/tuxbox/config/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /etc/tuxbox/oscam-emu/oscam.server /etc/tuxbox/config/gcam.server > /dev/null 2>&1'

def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

def f77(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
def f8(seqq):
    seq=sorted(seqq)
    #cc4=sorted(seq,key=lambda x: x[0].lower() or x[1])
    cc4=sorted(seq, key = lambda x: (x[0], x[1]))
    cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0].lower() != cc4[i-1][0].lower() or i==0 or cc4[i][0].lower() == cc4[i-1][0].lower() and cc4[i][1] != cc4[i-1][1]] or []
    return cc4
'''
def allccam(link):
    import requests
    #short url expand
    import httplib
    try:
        conn = httplib.HTTPConnection(link.strip().split('/')[2])
        conn.request('HEAD', '/'+link.strip().split('/')[3])
        response = conn.getresponse()
        response.getheader('location')
        a=response.getheader('location')
        f = requests.get(a,timeout=7)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        q=re.findall('[C:c]: (.*?)</h2>',the_page)[0].split()
        Host=q[0]
        Port=re.findall('>(.*?)<',q[2])[0]
        User=q[3]
        Pass=q[4]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]
'''
def getPage(link):
    link=link.strip('\r\n')
    try:
        cmd=('curl -s -L -m 5 "'+link+'"')
        the_page =subprocess.check_output(cmd,shell=True)
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('c |c: (.*?)[<:\n]',the_page,re.IGNORECASE)
        for i in a:
            if len(i.split())==4:
                break
        a=i.split()
        Host=a[0]
        Port=a[1]
        if 'freeiptv4u.com' in a[0]:
            User=a[2][:-1]+'7'
        else:
            User=a[2]
        Pass=a[3]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]

'''
def getPage(link):
    import requests
    link=link.strip('\r\n')
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=1.0,verify=False)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=5.0,verify=False)
            except:
                pass
        atus='retry errors'
        if atus=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=7.0,verify=False)
        the_page = f.text.encode('ascii', 'ignore')
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('c |c: (.*?)[<:\n]',the_page,re.IGNORECASE)
        for i in a:
            if len(i.split())==4:
                break
        a=i.split()
        Host=a[0]
        Port=a[1]
        if 'freeiptv4u.com' in a[0]:
            User=a[2][:-1]+'7'
        else:
            User=a[2]
        Pass=a[3]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]
'''

def getPage2(link):
    import requests
    link=link.strip('\r\n').strip()
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=5)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=5)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=5)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        a=the_page.split()
        Host=a[1]
        Port=a[2]
        User=a[3]
        Pass=a[4]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]
def getPage3(link):
    import urllib3
    http = urllib3.PoolManager()
    link=link.strip('\r\n')
    try:
        try:
            f = http.request('GET',link,headers=UserAgent,timeout=urllib3.Timeout(connect=1.0))
        except:
            try:
                f = http.request('GET',link,headers=UserAgent,timeout=urllib3.Timeout(connect=1.0))
            except:
                #print 'noway...2 times'
                f.status='retry errors'
                pass
        if f.status=='retry errors':
            f = http.request('GET',link,headers=UserAgent,timeout=urllib3.Timeout(connect=1.0))

        the_page = f.data.decode('utf-8').encode('ascii', 'ignore')
        a=re.findall('[Cc]:(.*?)[<:\n]',the_page)[0].split()
        Host=a[0]

        Port=a[1]
        if 'freeiptv4u.com' in a[0]:
            User=a[2][:-1]+'7'
        else:
            User=a[2]
        Pass=a[3]
    except:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
    return [Host,Port,User,Pass]

def getPage4(link):
    import urllib3
    http = urllib3.PoolManager()
    link=link.strip('\r\n')
    try:
        try:
            f = http.request('GET',link,headers=UserAgent)
        except:
            try:
                f = http.request('GET',link,headers=UserAgent)
            except:
                f.status='retry errors'
                pass
        if f.status=='retry errors':
            f = http.request('GET',link,headers=UserAgent)
        the_page =f.data.decode('utf-8').encode('ascii', 'ignore')
        a=the_page.split()
        Host=a[1]
        Port=a[2]
        User=a[3]
        Pass=a[4]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]
def ifosat(link):
    try:
        data = urllib2.urlopen(link,timeout=5)
        the_page=data.read()
        Host=re.findall('[host:C]: (.*?)[<: ]', the_page,re.DOTALL)[0]
        Port=re.findall('port: (.*?)[<: ]', the_page,re.DOTALL)[0]
        User=re.findall('user: (.*?)[<: ]', the_page,re.DOTALL)[0]
        Pass=re.findall('pass: (.*?)[<: ]', the_page,re.DOTALL)[0]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return  [Host, Port, User, Pass]
def ccamfree(link):
    link=link.strip('\r\n')
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=5)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=5)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=5)
        the_page = f.text.encode('ascii', 'ignore')
        list1=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :\n:\t]', the_page)
        list2=[]
        if len(list1)>0:
            for i in list1:
                if len(i)==4 and i[1].isdigit():
                    list2.append(i)
        else:
            list2=[['error','error','error','error']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['error','error','error','error']]
    return list2
def nlinefree(link):
    link=link.strip('\r\n')
    import requests
    import re
    UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
     'Accept': 'text/html'}
    def f8(seqq):
        seq=sorted(seqq)
        cc4=sorted(seq,key=lambda x: x[0]and x[1])
        cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
        return cc4
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=5)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=5)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=5)
        the_page = f.text.encode('ascii', 'ignore')
        list1=re.findall('N: (.*?) (.*?) (.*?) (.*?)[<: :\n:\t]', the_page)
        list2=[]
        if len(list1)>0:
            for i in list1:
                if len(i)==4:
                    list2.append(i)
        else:
            list2=[['error','error','error','error']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['error','error','error','error']]
    return list2
def blueccam1(link):
    import requests
    link=link.strip('\r\n')
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=5)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=5)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=5)
        the_page = f.text.encode('ascii', 'ignore')
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('<h2>(.*?)</h2>',the_page)
        Host=a[0].split()[1]
        Port=re.findall(r'\b\d+\b', a[0].split()[3])[0]
        User=a[0].split()[4]
        Pass=a[0].split()[5]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
    return [Host,Port,User,Pass]

# ======    Message on screen =========================================================================

message_script=os.system('wget -O /dev/null -q "http://localhost/web/message?text= \nOscupdate script by GUIRA is Running ......&type=2&timeout=6"')

#======================================================================================================

#activation servsat
try:
    acct=subprocess.check_output('curl -s --max-time 5 "http://www.serversat.net/cccam.php" --data "author=anaana"', shell=True)
except:
    pass
#print "servsat updated"
#activation servsat MGCAMD
try:
    acct=subprocess.check_output('curl -s --max-time 5 "http://www.serversat.net/mgcamd.php" --data "author=anaana"', shell=True)
except:
    pass
#print "servsat MG updated"

#activation tounfite
a11=subprocess.check_output('curl -s --cookie-jar - "http://tounfite.ddns.net/iptvsmarttv.php" --data-raw "username=year&password=anaa"',shell=True)
#activation
link='http://tounfite.ddns.net/'+a11[a11[:a11.find('Afficher')].rfind('href="'):a11.find('Afficher')].split('"')[1]
coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
cmd='curl -s '+link+' -H "Cookie: PHPSESSID='+coki
a12=subprocess.check_output(cmd,shell=True)
#activation algsat mgcamd

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    a=subprocess.check_output('curl -s --max-time 5 "http://algsat.ddns.net/" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Origin: http://algsat.ddns.net" -H "Upgrade-Insecure-Requests: 1" -H "Content-Type: application/x-www-form-urlencoded" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Referer: http://algsat.ddns.net/" -H "Accept-Language: en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5" -H "Cookie: _ga=GA1.3.502606778.1586306352; PHPSESSID=smle44lavg1i16uldk74l9e173; _gid=GA1.3.185868082.1586609023; _gat_gtag_UA_132808415_2=1" --data "Username='+user+'&Username='+user+'&addf2=" --insecure &', shell=True)
    a1=subprocess.check_output('curl -s --max-time 5 "http://algsat.ddns.net/mgcamd.php" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Referer: http://algsat.ddns.net/" -H "Accept-Language: en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5" -H "Cookie: _ga=GA1.3.502606778.1586306352; PHPSESSID=smle44lavg1i16uldk74l9e173; _gid=GA1.3.185868082.1586609023; _gat_gtag_UA_132808415_2=1"  --insecure &', shell=True)
    b=a1
    ho=re.findall('N: (.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','algsat']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

#print "algsat MG updated"

# kcccam

try:
    ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
    a=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" --data "protocol=mgcam&server=f3.kcccam.com&vehicle1=agree"', shell=True)
    a1=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" -H "cookie: already='+ip+'"&', shell=True)
    b=a1
    ho=re.findall('CWS(.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[1]
    port= ho[2]
    user= ho[3]
    Pass= ho[4]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','kcccam']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+5]='user                          = '+user+'\n'
                read[i+6]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass
#print "algsat MG2 updated"


# infosat MgCAMD2

try:
    a=subprocess.check_output('curl -s --max-time 5 "http://infosat.satunivers.tv/mgfr/" --data "user=anaana&pass=anaana"', shell=True)
    aa=a
    mghost=re.findall('host: (.*?)<',aa)[0].strip()
    mgport=re.findall('port: (.*?)<',aa)[0].strip()
    mguser=re.findall('user: (.*?)<',aa)[0].strip()
    mgpass=re.findall('pass: (.*?)<',aa)[0].strip()
    a=[mghost,mgport,mguser,mgpass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if 'infosat.satunivers.tv,30000' in read[i]:
                read[i]='device                        = '+mghost+','+mgport+'\n'
                read[i+2]='user                          = '+mguser+'\n'
                read[i+3]='password                      = '+mgpass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass
#print "infosat MG2 updated"
# infosat MgCAMD1
try:

    a1=subprocess.check_output('curl -s --max-time 5 "http://infosat.satunivers.tv/mg/" --data "user=anaana&pass=anaana"', shell=True)
    aa1=a1
    mghost1=re.findall('host.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mgport1=re.findall('port.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mguser1=re.findall('user.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mgpass1=re.findall('pass.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    a=[mghost1,mgport1,mguser1,mgpass1]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read1=ffii.readlines()
        ffii.close()
        for j in range(len(read1)):
            if 'infosat.satunivers.tv,24000' in read1[j]:
                read1[j]='device                        = '+mghost1+','+mgport1+'\n'
                read1[j+2]='user                          = '+mguser1+'\n'
                read1[j+3]='password                      = '+mgpass1+'\n'
                break
        ffii=open(source,'w')
        for i in read1:
            ffii.write(i)
        ffii.close()
except:
    pass
#print "infosat MG1 updated"
try:
    a5=subprocess.check_output('curl -s --max-time 5 "http://server.satunivers.tv/gc/index.html"  --data "user=anaana&pass=dzpros-forum"', shell=True)
    a=subprocess.check_output('curl -s --max-time 5 "http://server.satunivers.tv/gc/cg.php" --data "user=anaana&pass=dzpros-forum"', shell=True)
    aa=a
    aaa=re.findall('c: (.*?)<',aa,re.IGNORECASE)[0].split()
    for i in aaa:
        if len(i.split())==4 and i.split()[1].isdigit():
            break
        else:
            1/0
    a=i.split()
    mhost=a[0]
    mport=a[1]
    muser=a[2]
    mpass=a[3]
    a=[mhost,mport,muser,mpass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if 'infosat_cccam' in read[i]:
                read[i+2]='device                        = '+mhost+','+mport+'\n'
                read[i+3]='user                          = '+muser+'\n'
                read[i+4]='password                      = '+mpass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

#print "infosat cccam updated"

#   OSN

try:
    user='96200507'
    #user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username=96200507&&cline="'
    b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #ho=re.findall('n: (.*?)<',b,re.IGNORECASE)[0].split()
    #host= re.findall('host.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    #port= re.findall('port.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    #Pass= re.findall('pass.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
except:
    pass
# urliptv

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    a1=subprocess.check_output('curl -s --max-time 5 "https://urliptv.com/CCcam/" --data "Username='+user+'&cline="', shell=True)
    b=a1
    ho=re.findall('c: (.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','urliptv']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

# firecccam

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    cmd='curl -s --max-time 5 "http://firecccam.com/mgcamdg.php"  --data "Username='+user+'&Password='+user+'&Email='+user+'@yahoo.com^&addf="'
    a1=subprocess.check_output(cmd, shell=True)
    b=a1
    ho=re.findall('n: (.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','firecccam']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

servers1=[]
servers2=[]
my_servers=[]

# oscampk
try:
    cmd='curl -s --max-time 5 "https://oscampk.com/index.php"  --data "addf=addf"'
    a1=subprocess.check_output(cmd, shell=True)
    b=a1
    ho=re.findall('C: (.*?)<',b,re.DOTALL)[0].strip('\n').split(' ')
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        oscalm=[host,port,user,Pass]
        my_servers.append(oscalm)
except:
    pass

if os.path.isfile('/oscupdate/my-servers.txt'):
    the_file=open('/oscupdate/my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()
# ccamtiger

for i in range(len(the_links)):
    serv=getPage(the_links[i])
    #print i
    my_servers.append(serv)

#print "my-servers.txt updated"

if os.path.isfile('/oscupdate/dreamosat.txt'):
    the_file=open('/oscupdate/dreamosat.txt','r')
    the_links =the_file.readlines()
    the_file.close()

for i in range(len(the_links)):
    serv=getPage4(the_links[i])
    servers1.append(serv)

#print "dreamosat updated"
#clines Najmsatcamd

if os.path.isfile('/oscupdate/clines.txt'):
    the_fil=open('/oscupdate/clines.txt','r')
    the_clins =the_fil.readlines()
    the_fil.close()
anaj0=ccamfree(the_clins[0])
anaj1=ccamfree(the_clins[1])
anaj2=ccamfree(the_clins[2])
anaj3=ccamfree(the_clins[3])
anaj4=ccamfree(the_clins[4])
anaj5=ccamfree(the_clins[5])
anaj=anaj0+anaj1+anaj2+anaj3+anaj4+anaj5
cliness=f8(anaj)
cliness=f8(cliness)
clina=[]
for i in cliness:
    if 'fcnoip' not in i[0]:
        clina.append(i)

for i in range(len(clina)):
    servers2.append(clina[i])

#print "najmsat updated"

#========================================================
#====                NLINES                            ======
#========================================================

nl0=nlinefree(the_clins[0])
nl1=nlinefree(the_clins[1])
nl2=nlinefree(the_clins[2])
nl=nl0+nl1+nl2
ness=f8(nl)

ncamd=[]

for line in ness:
    ncamd.append(line)
#print "nlines updated"

'''
# --------------------------------------------------------
# cccam-live.com
# --------------------------------------------------------

try:
    link='http://www.cccam-live.com/'
    f = requests.get(link,headers=UserAgent,timeout=5)
    the_page = f.text.encode('ascii', 'ignore')
    st=(datetime.datetime.today()).strftime('%Y-%m-%d')
    sr='href="(http://www.cccam.*?'+st+'/)'
    a=re.findall(sr,the_page)
    link0=a[0]
    cccamlive=ccamfree(link0)
    cccamliv=[]
    for i in cccamlive:
        if 'fcnoip' not in i[0]:
            cccamliv.append(i)
    for i in range(len(cccamliv)):
        if len(i)==4:
            servers2.append(cccamliv[i])
except:
    pass

#print "cccam-live updated"
'''
if os.path.isfile('/oscupdate/allcccam.txt'):
        the_fil=open('/oscupdate/allcccam.txt','r')
        the_lins =the_fil.readlines()
        the_fil.close()

#servs=[]
#for i in range(4):
    #serv=allccam(the_lins[i])
    #servers1.append(serv)
#print "allcam updated"
'''
#======buy-iptv===============================
lubuy=the_lins[9]
lubuy=lubuy.strip('\r\n')
try:
    f = requests.get(lubuy,timeout=5)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    c1=the_page.find('C:')
    c2=the_page[c1:].find('<')
    b1=c1+c2
    Host=the_page[c1:b1].split()[1]
    User=the_page[c1:b1].split()[2]
    Pass=the_page[c1:b1].split()[3]
    c3=the_page.find('Port ')
    c4=the_page[c3:].find('<')
    b2=c3+c4
    Port=the_page[c3:b2].split()[2]
    buyiptv=[Host,Port,User,Pass]
except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    buyiptv=[[Host, Port, User, Pass]]

servers1.append(buyiptv)
'''
#print "buyiptv updated"
#======cccamlux===============================
'''lux=the_lins[5]
lux=lux.strip('\r\n')

try:
    lx2=requests.get(lux,headers=UserAgent,timeout=5)
    lx2 = lx2.text.encode('ascii', 'ignore')
    lux=lux+re.findall('href="(.*?)">Free CCcam<',lx2)[0]
    lx1=requests.get(lux,headers=UserAgent,timeout=5)
    lx1 = lx1.text.encode('ascii', 'ignore')
    luxhost=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[0]
    luxport=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[2]
    luxuser=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[4]
    luxpass=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[6]
    luxccam= [luxhost,luxport,luxuser,luxpass]
except:
    luxccam= [['error','error','error','error']]


servers1.append(luxccam)

#print "lux updated"
'''
#======cccamstore===============================
'''wee=the_lins[7]
wee=wee.strip('\r\n')
store=getPage(wee)
servers1.append(store)
#print "wee updated"
'''
#=============================================
#servers.append(servs)
req3 ='http://infosat.satunivers.tv/cgn/index1.php'
khaledsat=ifosat(req3)
req1 ='http://server.satunivers.tv/server2/'
khaled1=ifosat(req1)
req ='http://infosat.satunivers.tv/download1.php?file=srtx5.txt'
khaled2=ifosat(req)
my_servers.append(khaled2)
my_servers.append(khaled1)
my_servers.append(khaledsat)
req4 ='http://s1.satunivers.tv/download1.php?file=srtx4.txt'
try:
	urllib.urlretrieve(req4, ('/tmp/Server_infosat.txt'))
	the_file=open('/tmp/Server_infosat.txt','rt')
	the_files =the_file.read()
	ssr=[the_files.split()[1],the_files.split()[2],the_files.split()[3],the_files.split()[4]]
except:
	Host="error"
	Port="error"
	User="error"
	Pass="error"
	ssr=[[Host, Port, User, Pass]]

my_servers.append(ssr)
#print "infosat servers updated"
# ================================= freeclines + testious =================================
linktest1='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()).strftime('%Y-%m-%d')
linktest2='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()-datetime.timedelta(1)).strftime('%Y-%m-%d')

if requests.get(linktest1,headers=UserAgent,timeout=5).status_code==200:
    link3=linktest1
elif requests.get(linktest2,headers=UserAgent,timeout=5).status_code==200:
    link3=linktest2
else:
    link3='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()-datetime.timedelta(2)).strftime('%Y-%m-%d')

testious=ccamfree(link3)
ntestious=nlinefree(link3)
for lne in ntestious:
    ncamd.append(lne)

# free
try:
    link1='http://www.freecline.com/index'
    link=link1.strip('\r\n')
    '''yr=(datetime.datetime.now()- timedelta(0)).strftime('%Y')
    mt=(datetime.datetime.now()- timedelta(0)).strftime('%m')
    dy=(datetime.datetime.now()- timedelta(0)).strftime('%d')'''
    td1=(datetime.date.today()-datetime.timedelta(0)).strftime('%Y/%m/%d')
    ys1=(datetime.date.today()-datetime.timedelta(1)).strftime('%Y/%m/%d')
    ys2=(datetime.date.today()-datetime.timedelta(2)).strftime('%Y/%m/%d')
    f = requests.get("http://www.freecline.com/history/CCcam/"+td1,headers=UserAgent,timeout=5)
    f1 = requests.get("http://www.freecline.com/history/CCcam/"+ys1,headers=UserAgent,timeout=5)
    f2 = requests.get("http://www.freecline.com/history/CCcam/"+ys2,headers=UserAgent,timeout=5)
    ff=requests.get("http://www.freecline.com/history/Newcamd/"+td1,headers=UserAgent,timeout=5)
    ff1=requests.get("http://www.freecline.com/history/Newcamd/"+ys1,headers=UserAgent,timeout=5)
    ff2=requests.get("http://www.freecline.com/history/Newcamd/"+ys2,headers=UserAgent,timeout=5)
    if f.status_code==200:
        f=f
    elif f1.status_code==200:
        f=f1
    elif f2.status_code==200:
        f=f2
    if ff.status_code==200:
        ff=ff
    elif ff1.status_code==200:
        ff=ff1
    elif ff2.status_code==200:
        ff=ff2
    the_page=f.text.encode('ascii', 'ignore')
    a1=re.findall('(c: .*?)status_icon_online',the_page,re.DOTALL|re.IGNORECASE)
    a2=[re.findall('c: (.*?)<',i,re.DOTALL|re.IGNORECASE)[-1] for i in a1]
    a2=[i.split(' ') for i in a2]
    freecline=f8(a2)
    if freecline==[]:
        freecline=[['error','error','error','error']]
    # free N-lines
    the_pagea=ff.text.encode('ascii', 'ignore')
    aa1=re.findall('(n: .*?)status_icon_online',the_pagea,re.DOTALL|re.IGNORECASE)
    aa2=[re.findall('n: (.*?)<',i,re.DOTALL|re.IGNORECASE)[-1] for i in aa1]
    aaa2=[[i.split()[0],i.split()[1],i.split()[2],i.split()[3]] for i in aa2]
    #bcd=[bb[0].split('_') for bb in bd if bb !=[]] or [['err'],['err'],['err'],['err']]
    #bbc=[]
    #for i in bcd:
        #bbc.append([i[0],i[1],i[2],i[3]])

    freeN=f8(aaa2)
    if freeN==[]:
        freeN=[['error','error','error','error']]

    for lnee in freeN:
        ncamd.append(lnee)
except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    freecline=[[Host, Port, User, Pass]]

try:
    f = requests.get('https://www.cccam3.com/free-mgcamd-server/',headers=UserAgent,timeout=5)
    the_page=f.text.encode('ascii', 'ignore')
    ccam3=re.findall(r'CWS =.*?>(.*?)<.*?>(.*?)<.*?>(.*?)<.*?>(.*?)<',the_page,re.IGNORECASE)
    try:
        at1 = int(ccam3[-1][2].strip(' ')[-2:])-13
        at1=ccam3[-1][2].strip(' ')[:-2] + str(at1)
    except:
        at1=ccam3[-1][2].strip(' ')
    cccam3=[ccam3[-1][0].strip(' '),ccam3[-1][1].strip(' '),at1,ccam3[-1][3].strip(' ')]
    ncamd.append(cccam3)
except:
    pass


## 4cardsharing
try:
    card='http://www.4cardsharing.net'
    linkk4=card.strip('\r\n')
    fff4 = requests.get(linkk4,headers=UserAgent,timeout=5)#,proxies=proxiess)
    pag4 = fff4.text.encode('ascii', 'ignore')
    tod=(datetime.datetime.now()- timedelta(0)).strftime('%d-%m-%Y')
    teod=(datetime.datetime.now()- timedelta(1)).strftime('%d-%m-%Y')
    yest=(datetime.datetime.now()- timedelta(2)).strftime('%d-%m-%Y')
    if tod in pag4:
        ttod=tod
    elif teod in pag4:
        ttod=teod
    else:
        ttod=yest
    c1=pag4.find(ttod+'/"')
    c2=pag4[:c1].rfind('https:')
    linkk4=pag4[c2:c1+len(tod)]
    fff4 = ccamfree(linkk4)
    card4sh=f8(fff4)
    if card4sh==[]:
        card4sh=[['error','error','error','error']]

except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    card4sh=[[Host, Port, User, Pass]]

# cccam.date
amdat='http://cccam.date'
dat=ccamfree(amdat)
serversm=card4sh+freecline+testious+dat
fcnoip11=[]
for i in testious or freecline or card4sh:
    if 'egypt' in i[0] or 'bemhd' in i[0] or 'egygold' in i [0]:
        fcnoip11.append(i)
for i in freecline:
    if 'egypt' in i[0] or 'bemhd' in i[0] or 'egygold' in i [0]:
        fcnoip11.append(i)
fcnoip12=f8(fcnoip11)
if fcnoip12==[]:
    fcnoip12=[['error','error','error','error']]

for n in fcnoip12:
    servers2.append(n)
ghg=freecline+testious
ghg=f8(ghg)
for nj in ghg:
    servers2.append(nj)
servers2=f8(servers2)

#print "testious freecline and dat updated"

serverss=[]
for lline in (servers1+servers2):
    if len(lline)==4:
        serverss.append(lline)
servers=f8(serverss)
allservers=[]
for i in servers:
    if not 'cardserver' in i[0].lower():
        allservers.append(i)
servers=f8(allservers)

#print "all servers sorted and filtred"
#==============  duckdns  ===============

rnd='yearning_5'
sgn=requests.Session()
url='http://80.211.55.20/cccam/redirect.php'
try:
    Cccam = ''
    hdr={'Host': '80.211.55.20',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
         'Accept-Encoding': 'gzip, deflate',
         'Content-Type': 'application/x-www-form-urlencoded',
         'Content-Length': '22',
         'Connection': 'keep-alive',
         'Referer': 'http://80.211.55.20/cccam/index.php',
         'Cookie': 'RAZOR_SERVER_VERIFY_X=0',
         'Upgrade-Insecure-Requests': '1'}
    prm={'Username':rnd,'addf':'' }
    r = sgn.post(url,headers=hdr,data=prm)
    r2 = sgn.get('http://80.211.55.20/cccam/index.php').text
    rgx = '''<center>(.+?)<br><img src='assets/img/ok.png' />'''
    cccam = re.findall(rgx,r2)
    if cccam:
        qsc=cccam[0].encode('ascii', 'ignore').split()
        duckdns=[qsc[1],qsc[2],qsc[3],qsc[4]]
    else:
        duckdns=[['error','error','error','error']]
except:
    duckdns=[['error','error','error','error']]
if len(duckdns)==4:
    my_servers.append(duckdns)

#print "duckdns updated"
#====================================================
# ================== cccam4all hack
sgn=requests.Session()
try:
    def get_cccam(urlo):
        r = sgn.get(urlo).content
        vmx = '''<h3.+?><span.+?><strong>(.+?)</strong></span></h3>'''
        cccam = re.findall(vmx,r)
        if cccam:
            return cccam[0]
        else:
            return 'nada_cccam'
    def get_flyurl(url):
        r = sgn.get(url).content
        tmx = '''html\( "<a.+?href='(.+?)'>Click here to proceed</a>"'''
        href = re.findall(tmx,r)
        if href:

            return get_cccam(href[0])
        else:
            return 'nada_href'
    r = sgn.get('http://cccam4all.hack-sat.org/').content
    rgx = '''<a class="button" href="(.+?)" id.+?><h2>Click Active User!</h2></a>'''
    button = re.findall(rgx,r)
    if button:
        CCcam = get_flyurl(button[0])
    else:
        'nada'

    def cfDecodeEmail(encodedString):
        r = int(encodedString[:2],16)
        email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
        return email

    aa=re.findall('[C:c]:(.*?)[<:\n]',CCcam)[0].split()
    cod=re.findall('data-cfemail="(.*?)">',CCcam)[0]
    host=aa[0]
    port=aa[1]
    user=aa[2]+cfDecodeEmail(cod)
    passs=CCcam.split()[len(CCcam.split())-1]
    hack=[host,port,user,passs]
    my_servers.append(hack)

except:
    pass

#print "cc4all updated"
#===================  hack-sat  =================
try:
    import requests,re
    sgn=requests.Session()
    def get_iptvsat4k():
        def get_cccam(urlo):
            r = sgn.get(urlo).content
            vmx = '''<h3.+?><span.+?><strong>(.+?)</strong></span></h3>'''
            cccam = re.findall(vmx,r)
            if cccam:
                return cccam[0]
            else:
                return [['error','error','error','error']]
        def get_flyurl(url):
            r = sgn.get(url).content
            tmx = '''html\( "<a.+?href='(.+?)'>Click here to proceed</a>"'''
            href = re.findall(tmx,r)
            if href:
                #print href[0]
                return get_cccam(href[0])
            else:
                return [['error','error','error','error']]
        r = sgn.get('http://generator.hack-sat.com/').content
        rgx = '''<a class="button" href="(.+?)" id.+?><h2>Click Active User!</h2></a>'''
        button = re.findall(rgx,r)
        if button:
            #print button[0]
            CCcam = get_flyurl(button[0])
            return CCcam
        else:
            return [['error','error','error','error']]
    qsc= get_iptvsat4k().split()
    hacksat=[qsc[1],qsc[2],qsc[3],qsc[4]]
except:
    hacksat=[['error','error','error','error']]
if len(hacksat)==4:
    my_servers.append(hacksat)
#print "hack updated"

my_servers1=[]
for i in my_servers:
    if not 'err' in i[0]:
        my_servers1.append(i)
#import socket
test101=[]
for i in my_servers1:
    try:
        a=socket.gethostbyname(i[0])
        i[0]=a
        test101.append(i)
    except:
        pass
my_servers1=f8(test101)
my_servers=my_servers1

"""newservers=[]
for new in servers:
    if not 'err' in new[0] and not '51.38.48.10' in new[0] :
        newservers.append(new)"""
import socket
test1=[]
for i in servers:
    try:
        a=socket.gethostbyname(i[0])
        i[0]=a
        test1.append(i)
    except:
        pass
servers=f8(test1)

servers=[i for i in servers if not any(i[0]  in j for j in my_servers)]

drop1=['topservercccam','alkaicer','serversat','generator3','freeiptv4u','dzpros-forum']
servers=[i for i in servers if not any(j in i[3]  for j in drop1)]
servers=servers
drop=['err','speeds','51.38.48.10','178.128.200.245']
#drop=[]
servers=[i for i in servers if not any(j in i[0]  for j in drop)]
#pass drop

my_servers=[i for i in my_servers if not any(j in i[0]  for j in drop)]
#drop1=[]

#print "remover err from servers"


#====================================================
with open('/tmp/a_servers.txt','w') as ff:
    for nn in servers:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')

#from CCcamTester import TestCline
#serversm=[]
#for i in serversmww:
#    s='C: '+i[0]+' '+i[1]+' '+i[2]+' '+i[3]
#    if TestCline(s)==True:
#        serversm.append(i)

#serversm=sorted(serversm)
#serversm=[serversm[i] for i in range(len(serversm)) if serversm[i][0] != serversm[i-1][0] or i==0 or serversm[i][0] == serversm[i-1][0] and serversm[i][1] != serversm[i-1][1]] or [['err'],['err'],['err'],['err']]

#print "servers to tmp a_servers"
if serversm==[]:
    serversm=[['error','error','error','error']]
serverssm=[]
for lline in serversm:
    if len(lline)==4:
        serverssm.append(lline)
serversm=f8(serverssm)

#print "finish filter serversm"

with open('/tmp/a_serversm.txt','w') as ff:
    for nn in serversm:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')
#print "finish append serversm to a_servers"

ncamd=f8(ncamd)

labelsm=[]
for i in range(len(serversm)):
    labelsm.append(serversm[i][0])
# =========================================================================================
#======= oscam ====================
if os.path.isfile(source):
    the_pag=open(source,'r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>422:
    the_pag=open(source,'w')
    i=0
    while i <422:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()

#print "wirite first oscam"

#=================================
#           scccam
#=================================
'''try:
    act=getPage3('http://scccam.com/getc.php?user=yearnig_5&pass=yearnig_5')
    fil=open('/etc/tuxbox/oscam-emu/oscam.server','r')
    a=fil.readlines()
    fil.close()
    for i in range(len(a)):
        if 'scccam.com,' in a[i]:
            break
    a[i+1]='user                          = yearnig_5\n'
    a[i+2]='password                      = yearnig_5\n'
    fil=open('/etc/tuxbox/oscam-emu/oscam.server','w')
    for i in a:
        fil.write(i)
    fil.close()
except:
    pass
'''
#print "sccam  updated and writen"

#===========================================================
#                    freeiptv4u
#===========================================================
ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
fil=open(source,'r')
a=fil.readlines()
fil.close()
for i in range(len(a)):
    if 'freeiptv4u.com,' in a[i]:
        break
a[i+1]='user                          = '+ip+'\n'
fil=open(source,'w')
for i in a:
    fil.write(i)
fil.close()
#   Activation
s = requests.Session()
parames = {'user':ip,'pass':'freeiptv4u.com','submit':'click Active User'}
url="http://cccam.freeiptv4u.com/9dqsfg95b/"
try:
    r = s.post(url,data=parames)
except:
    pass
#print "freeiptv4u updated"

#===========================================================
#===========================================================
#                    flylinks
#===========================================================
ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
fil=open(source,'r')
a=fil.readlines()
fil.close()
for i in range(len(a)):
    if 'flylinks.net,' in a[i]:
        break
a[i+1]='user                          = '+ip+'\n'
fil=open(source,'w')
for i in a:
    fil.write(i)
fil.close()
#   Activation
s = requests.Session()
parames = {'user':ip,'pass':'www.flylinks.net','submit':'click Active User'}
url="http://cccam.flylinks.net/index.php"
try:
    r = s.post(url,data=parames)
except:
    pass

#print "flylinks updated"
#===========================================================
#===========================================================
#                    flylinks
#===========================================================

#   Activation
"""
from requests.auth import HTTPBasicAuth
import urllib
rnd='yearning_5'
url= 'http://cccam48.webtechdz.com/CC48H/index01.php'
headers={'Host': 'cccam48.webtechdz.com',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
         'Accept-Encoding': 'gzip, deflate',
         'Referer': 'http://cccam48.webtechdz.com/CC48H/index01.php',
         'Content-Type': 'application/x-www-form-urlencoded',
         'Cookie': 'visited=yes'}
s = requests.Session()
parames = {'Username':rnd,'Password':rnd,'addf':''}
try:
    r = s.post(url,headers=headers,data=parames)
    htmldata2 = r.text
    Rgx = '''> C: (.+?)<'''
    cline = re.findall(Rgx,htmldata2)
except:
    pass"""

#print "cccam48 updated"
#===========================================================

the_pag=open(source,'r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open(source,'a')
        #mecccam

ij=1
for i in my_servers:
    i.append('My_'+str(ij)+'_'+i[0])
    ij=ij+1

jj=1
for i in servers:
    i.append(str(jj)+'_'+i[0])
    jj=jj+1

servers=my_servers+servers

for j in servers:
    try:
        host=j[0]
        port=j[1]
        user=j[2]
        pasw=j[3]
        exxcept=['178.238.236.25','176.31.156.44','213.136.94.35','167.86.119.185','185.22.173.58','5.135.75.42','5.189.156.56','178.238.232.233','116.202.196.126','178.128.200.245','51.77.220.127','37.59.80.83','94.130.220.50','94.130.199.50','144.91.117.213','178.63.69.157']

        if any(host in i for i in exxcept):
            the_pag.write('\n\n[reader]\nlabel= '+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1708:000000;0500:030B00;0500:032830;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')
        else:
            the_pag.write('\n\n[reader]\nlabel= '+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1708:000000;0500:030B00;0500:032830;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
ncamd1=[]
for i in ncamd:
    if len(i)==4:
        ncamd1.append(i)
drop=['err','speeds','algsat','saqr','kcccam','firecccam','satunivers','serversat']
#drop=[]
ncamd1=[i for i in ncamd1 if not any(j in i[0]  for j in drop)]
ncamd=f8(ncamd1)
try:
    #lin='https://www.google.com/search?rlz=1C1AVFC_enTD866TD866&sxsrf=ALeKk00Uv4oOkMLit4cUJTGnqaRvTS5rlg%3A1586723680804&ei=YHuTXpPLMMWLlwTpgIOgBA&q=satkeys.biz+mgcamd&oq=satkeys.bizhttps://www.google.com/search?rlz=1C1AVFC_enTD866TD866&sxsrf=ALeKk00Uv4oOkMLit4cUJTGnqaRvTS5rlg%3A1586723680804&ei=YHuTXpPLMMWLlwTpgIOgBA&q=satkeys.biz+mgcamd&oq=satkeys.biz'
    #f=requests.get(lin,headers=UserAgent,timeout=3.0,verify=False)
    #the_page = f.text.encode('ascii', 'ignore')
    #a=re.findall('href="(https://satkeys.biz/index.*?)"',the_page)[0]
    a='https://satkeys.biz/index.php?topic=93755.0'
    f=requests.get(a,headers=UserAgent,timeout=5.0,verify=False)
    b = f.text.encode('ascii', 'ignore')
    ho=re.findall('CWS(.*?)<',b,re.IGNORECASE)
    ser=[]
    for i in ho:
        ii=i.split()
        ser.append([ii[1].replace(' ',''),ii[2].replace(' ',''),ii[3].replace(' ',''),ii[4].replace(' ','')])
    ser=f8(ser)
    for i in ser:
        ncamd.append(i)
except:
    pass
ncamd=f8(ncamd)


with open('/tmp/a_ncamd.txt','w') as ff:
    for nn in ncamd:
        s='N: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]+' 01 02 03 04 05 06 07 08 09 10 11 12 13 14'
        ff.write(s+'\n')
#print "finish write a_ncam"
t_pag=open(source,'a')
for i in range(len(ncamd)):
    #print i
    try:
        host=ncamd[i][0]
        label='Ncam_'+str(i+1)+'_'+host
        port=ncamd[i][1]
        user=ncamd[i][2]
        pasw=ncamd[i][3]
        t_pag.write('\n\n[reader]\nlabel= '+label + '\nprotocol= newcamd\ndevice= ' + host + ',' + port + '\nkey = 0102030405060708091011121314\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\n#cccversion= 2.0.11\ndisablecrccws_only_for= 1708:000000;0500:030B00;0500:032830;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')
    except IndexError:
        pass


t_pag.close()
#print "oscam  updated and writen"
#======= Ncam ====================

os.system(pkt_cp)
#print "ncam  updated and writen"
#======= G-CAMD ====================
os.system(pkt_cp1)
#print "gcam  updated and writen"
#======= wicardd ====================
if os.path.isfile(source_wic):
    the_pag=open(source_wic,'r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>253:
    the_pag=open(source_wic,'w')
    i=0
    while i <253:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open(source_wic,'r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open(source_wic,'a')
        #mecccam
for j in servers:
    try:
        host=j[0]
        port=j[1]
        user=j[2]
        pasw=j[3]
        the_pag.write('\n[reader]\nname= ' + j[4] + '\nactive= 1\ntype= cccam\naccount=' + user + ':' + pasw + '@' + host + ':' + port + '\ndebug = 1\nreconnect_delay = 1\nemm_cache = 1\necm_ttl = 15000\nreconnect_to_account_ip =1\ndropbadcws= 1')
    except IndexError:
        pass
the_pag.close()

#print "wicard  updated and writen"
"""# ============================== oscam Modern ========================================
os.system('cp /var/keys/oscam.server /etc/tuxbox/oscammodern/oscam.server > /dev/null 2>&1')"""
#print "oscam modern  updated and writen"
"""# ============================== oscam @ config folder  ========================================
os.system('cp /var/keys/oscam.server /var/keys/oscam.server > /dev/null 2>&1')"""
#print "oscam @ config updated and writen"
#======= NLINES ====================
"""if os.path.isfile('/etc/tuxbox/Nlines/oscam.server'):
    the_pag=open('/etc/tuxbox/Nlines/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>70:
    the_pag=open('/etc/tuxbox/Nlines/oscam.server','w')
    i=0
    while i <70:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/Nlines/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/Nlines/oscam.server','a')
        #mecccam
Nlabels=[]
for i in range(len(ncamd)):
    Nlabels.append(ncamd[i][0])

for j in range(len(Nlabels)):
    try:
        host=ncamd[len(Nlabels)-1-j][0]
        port=ncamd[len(Nlabels)-1-j][1]
        user=ncamd[len(Nlabels)-1-j][2]
        pasw=ncamd[len(Nlabels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + Nlabels[len(Nlabels)-1-j] + '\nenable= 1\nprotocol= newcamd\ndevice=' + host + ',' + port + '\nkey = 0102030405060708091011121314\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()"""
##print "nlines  updated and writen"
#from datetime import datetime
##print datetime.now() - startTime

d=open('/tmp/excution.txt','w')
now=datetime.datetime.now()
difference =now - now1
d.write('Started at:\n')
d.write(str(now1)+'\n')
d.write('completed at:\n')
d.write(str(now)+'\n')
d.write('elapsed time is:\n')
d.write(str(difference)+'\n')
d.close()
print difference

# print message of termination
difference=str(difference).rsplit('.',1)[0].split(':')
difference=difference[0]+' hr '+difference[1]+' min and '+difference[2]+' sec'
message_script2=os.system('wget -O /dev/null -q "http://localhost/web/message?text= \nOscupdate script by GUIRA is updated in ......\n'+'\n'+difference+'&type=2&timeout=15"')
