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
import datetime
from datetime import date, timedelta
import re
#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"
import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
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
def f77(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
def f8(seqq):
    seq=sorted(seqq)
    cc4=sorted(seq,key=lambda x: x[0]and x[1])
    cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
    return cc4

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

def getPage(link):
    import requests
    link=link.strip('\r\n')
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=10)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=10)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=10)
        the_page = f.text.encode('ascii', 'ignore')
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('[C\s|c]:(.*?)[<:\n]',the_page)
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
def getPage2(link):
    import requests
    link=link.strip('\r\n').strip()
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=10)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=10)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=10)
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


def ifosat(link):
    try:
        data = urllib2.urlopen(link,timeout=7)
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
    UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
     'Accept': 'text/html'}
    def f8(seqq):
        seq=sorted(seqq)
        cc4=sorted(seq,key=lambda x: x[0]and x[1])
        cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
        return cc4
    try:
        try:
            f = requests.get(link,headers=UserAgent,timeout=10)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=10)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=10)
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
            f = requests.get(link,headers=UserAgent,timeout=10)
        except:
            try:
                f = requests.get(link,headers=UserAgent,timeout=10)
            except:
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=10)
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
servers1=[]
servers2=[]
#ativate tounfite
os.system('tounfite.sh > /dev/null 2>&1')
os.system('rm tmp/tounfite.txt > /dev/null 2>&1')

#cccam =4g

try:
    os.system('cccam4g.sh > /dev/null 2>&1')
    filll=open('tmp/ccam4g.txt')
    a4g=filll.read()
    filll.close()
    os.system('rm tmp/ccam4g.txt > /dev/null 2>&1')
    c4g=re.findall('[C:c]:(.*?)[<:\n]',a4g)[0].split()
    servers1.append(c4g)
except:
    pass

#anwarcccam

try:
    os.system('anwarcccam.sh > /dev/null 2>&1')
    filll=open('tmp/anwar.txt')
    a4g=filll.read()
    filll.close()
    os.system('rm tmp/anwar.txt > /dev/null 2>&1')
    c4g=re.findall('[C:c]:(.*?)[<:\n]',a4g)[0].split()
    servers1.append(c4g)
except:
    pass
if os.path.isfile('my-servers.txt'):
    the_file=open('my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()

for i in range(len(the_links)):
    serv=getPage(the_links[i])
    servers1.append(serv)

if os.path.isfile('dreamosat.txt'):
    the_file=open('dreamosat.txt','r')
    the_links =the_file.readlines()
    the_file.close()

for i in range(len(the_links)):
    serv=getPage2(the_links[i])
    servers1.append(serv)

#clines Najmsatcamd
if os.path.isfile('clines.txt'):
    the_fil=open('clines.txt','r')
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

# --------------------------------------------------------
# cccam-live.com
# --------------------------------------------------------

try:
    link='http://www.cccam-live.com/'
    f = requests.get(link,headers=UserAgent,timeout=10)
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


if os.path.isfile('allcccam.txt'):
        the_fil=open('allcccam.txt','r')
        the_lins =the_fil.readlines()
        the_fil.close()

#servs=[]
for i in range(4):
    serv=allccam(the_lins[i])
    servers1.append(serv)
#======buy-iptv===============================
lubuy=the_lins[9]
lubuy=lubuy.strip('\r\n')
try:
    f = requests.get(lubuy,timeout=7)
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
#======cccamlux===============================
lux=the_lins[5]
lux=lux.strip('\r\n')

try:
    lx2=requests.get(lux,headers=UserAgent,timeout=10)
    lx2 = lx2.text.encode('ascii', 'ignore')
    lux=lux+re.findall('href="(.*?)">Free CCcam<',lx2)[0]
    lx1=requests.get(lux,headers=UserAgent,timeout=10)
    lx1 = lx1.text.encode('ascii', 'ignore')
    luxhost=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[0]
    luxport=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[2]
    luxuser=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[4]
    luxpass=re.findall('[C:c]: (.*?)<', lx1,re.DOTALL)[0].split()[6]
    luxccam= [luxhost,luxport,luxuser,luxpass]
except:
    luxccam= [['error','error','error','error']]


servers1.append(luxccam)
#======cccamstore===============================
wee=the_lins[7]
wee=wee.strip('\r\n')
store=getPage(wee)
servers1.append(store)
#=============================================
#servers.append(servs)
req3 ='http://infosat.satunivers.tv/cgn/index1.php'
khaledsat=ifosat(req3)
req1 ='http://server.satunivers.tv/server2/'
khaled1=ifosat(req1)
req ='http://infosat.satunivers.tv/download1.php?file=srtx5.txt'
khaled2=ifosat(req)
servers1.append(khaled2)
servers1.append(khaled1)
servers1.append(khaledsat)
req4 ='http://s1.satunivers.tv/download1.php?file=srtx4.txt'
try:
	urllib.urlretrieve(req4, ('tmp/Server_infosat.txt'))
	the_file=open('tmp/Server_infosat.txt','rt')
	the_files =the_file.read()
	ssr=[the_files.split()[1],the_files.split()[2],the_files.split()[3],the_files.split()[4]]
except:
	Host="error"
	Port="error"
	User="error"
	Pass="error"
	ssr=[[Host, Port, User, Pass]]

servers1.append(ssr)
# ================================= freeclines + testious =================================
link2='http://www.testious.com/free-cccam-servers'
link=link2.strip('\r\n')
link3='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()).strftime('%Y-%m-%d')
testious=ccamfree(link3)
ntestious=nlinefree(link3)
for lne in ntestious:
    ncamd.append(lne)
# free
try:
    link1='http://www.freecline.com/index'
    link=link1.strip('\r\n')
    yr=(datetime.datetime.now()- timedelta(0)).strftime('%Y')
    mt=(datetime.datetime.now()- timedelta(0)).strftime('%m')
    dy=(datetime.datetime.now()- timedelta(0)).strftime('%d')
    td1=yr+"/"+mt+"/"+dy
    ys1=yr+"/"+mt+"/"+str(int(dy)-1)
    ys2=yr+"/"+mt+"/"+str(int(dy)-2)
    f = requests.get("http://www.freecline.com/history/CCcam/"+td1,headers=UserAgent,timeout=10)
    f1 = requests.get("http://www.freecline.com/history/CCcam/"+ys1,headers=UserAgent,timeout=10)
    f2 = requests.get("http://www.freecline.com/history/CCcam/"+ys2,headers=UserAgent,timeout=10)
    ff=requests.get("http://www.freecline.com/history/Newcamd/"+td1,headers=UserAgent,timeout=10)
    ff1=requests.get("http://www.freecline.com/history/Newcamd/"+ys1,headers=UserAgent,timeout=10)
    ff2=requests.get("http://www.freecline.com/history/Newcamd/"+ys2,headers=UserAgent,timeout=10)
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
    a=re.findall(r'status_icon_online(.*?)">C|">c',the_page,re.DOTALL)
    bc=[re.findall(r'href="/info/CCcam/(.*?)/',bb,re.DOTALL) for bb in a]
    bcc=[bb[0].split('_') for bb in bc if bb !=[]] or [['err'],['err'],['err'],['err']]
    freecline=f8(bcc)
    if freecline==[]:
        freecline=[['error','error','error','error']]
    # free N-lines
    the_pagea=ff.text.encode('ascii', 'ignore')
    aa=re.findall(r'status_icon_online(.*?)">N|">n',the_pagea,re.DOTALL)
    bd=[re.findall(r'href="/info/Newcamd/(.*?)/',bb,re.DOTALL) for bb in aa]
    bcd=[bb[0].split('_') for bb in bd if bb !=[]] or [['err'],['err'],['err'],['err']]
    bbc=[]
    for i in bcd:
        bbc.append([i[0],i[1],i[2],i[3]])

    freeN=f8(bcd)
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


## 4cardsharing
try:
    card='http://www.4cardsharing.net'
    linkk4=card.strip('\r\n')
    fff4 = requests.get(linkk4,headers=UserAgent,timeout=10)#,proxies=proxiess)
    pag4 = fff4.text.encode('ascii', 'ignore')
    tod=(datetime.datetime.now()- timedelta(1)).strftime('%d-%m-%Y')
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
servers22=[]
for ss in servers2:
    if not any(e[0] == ss[0] and e[1]==ss[1] for e in servers1):
        print ss
        servers22.append(list(ss))




serverss=[]
for lline in servers:
    if len(lline)==4:
        serverss.append(lline)
servers=f8(serverss)
allservers=[]
for i in servers:
    if not 'cardserver' in i[0].lower():
        allservers.append(i)
servers=f8(allservers)
with open('tmp/a_servers.txt','w') as ff:
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


if serversm==[]:
    serversm=[['serversm-err','serversm-err','serversm-err','serversm-err']]
serverssm=[]
for lline in serversm:
    if len(lline)==4:
        serverssm.append(lline)
serversm=f8(serverssm)

with open('tmp/a_serversm.txt','w') as ff:
    for nn in serversm:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')
ncamd=f8(ncamd)
with open('tmp/a_ncamd.txt','w') as ff:
    for nn in ncamd:
        s='N: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]+' 01 02 03 04 05 06 07 08 09 10 11 12 13 14'
        ff.write(s+'\n')
labelsm=[]
for i in range(len(serversm)):
    labelsm.append(serversm[i][0])
# =========================================================================================
#======= oscam ====================
if os.path.isfile('tmp//oscam-emu/oscam.server'):
    the_pag=open('tmp//oscam-emu/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>438:
    the_pag=open('tmp//oscam-emu/oscam.server','w')
    i=0
    while i <438:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()

#=================================
#           scccam
#=================================
try:
    act=getPage('http://scccam.com/getc.php?user=yearnig_5&pass=yearnig_5')
    fil=open('tmp//oscam-emu/oscam.server','r')
    a=fil.readlines()
    fil.close()
    for i in range(len(a)):
        if 'scccam.com,' in a[i]:
            break
    a[i+1]='user                          = yearnig_5\n'
    a[i+2]='password                      = yearnig_5\n'
    fil=open('tmp//oscam-emu/oscam.server','w')
    for i in a:
        fil.write(i)
    fil.close()
except:
    pass
#===========================================================
#                    freeiptv4u
#===========================================================
ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
fil=open('tmp//oscam-emu/oscam.server','r')
a=fil.readlines()
fil.close()
for i in range(len(a)):
    if 'freeiptv4u.com,' in a[i]:
        break
a[i+1]='user                          = '+ip+'\n'
fil=open('tmp//oscam-emu/oscam.server','w')
for i in a:
    fil.write(i)
fil.close()
#   Activation
s = requests.Session()
parames = {'user':ip,'pass':'freeiptv4u.com','submit':'click Active User'}
url="http://server.freeiptv4u.com/"
try:
    r = s.post(url,data=parames)
except:
    pass

#===========================================================
#===========================================================
#                    flylinks
#===========================================================
ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
fil=open('tmp//oscam-emu/oscam.server','r')
a=fil.readlines()
fil.close()
for i in range(len(a)):
    if 'flylinks.net,' in a[i]:
        break
a[i+1]='user                          = '+ip+'\n'
fil=open('tmp//oscam-emu/oscam.server','w')
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

#===========================================================
#===========================================================
#                    flylinks
#===========================================================

#   Activation
import re
import requests
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
    pass

#===========================================================

the_pag=open('tmp//oscam-emu/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//oscam-emu/oscam.server','a')
        #mecccam
labels=[]
for i in range(len(servers)):
    labels.append(servers[i][0])

for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
#======= Ncam ====================
if os.path.isfile('tmp//config/ncam.server'):
    the_pag=open('tmp//config/ncam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>16:
    the_pag=open('tmp//config/ncam.server','w')
    i=0
    while i <16:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//config/ncam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//config/ncam.server','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
#======= G-CAMD ====================
if os.path.isfile('tmp//config/gcam.server'):
    the_pag=open('tmp//config/gcam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>438:
    the_pag=open('tmp//config/gcam.server','w')
    i=0
    while i <438:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//config/gcam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//config/gcam.server','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
#======= wicardd ====================
if os.path.isfile('tmp//config/wicardd.conf'):
    the_pag=open('tmp//config/wicardd.conf','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>253:
    the_pag=open('tmp//config/wicardd.conf','w')
    i=0
    while i <253:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//config/wicardd.conf','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//config/wicardd.conf','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n[reader]\nname= ' + labels[len(labels)-1-j] + '\nactive= 1\ntype= cccam\naccount=' + user + ':' + pasw + '@' + host + ':' + port + '\ndebug = 1\nreconnect_delay = 1\nemm_cache = 1\necm_ttl = 15000\nreconnect_to_account_ip =1\ndropbadcws= 1')
    except IndexError:
        pass
the_pag.close()
# ============================== oscam Modern ========================================
if os.path.isfile('tmp//oscammodern/oscam.server'):
    the_pag=open('tmp//oscammodern/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>438:
    the_pag=open('tmp//oscammodern/oscam.server','w')
    i=0
    while i <438:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//oscammodern/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//oscammodern/oscam.server','a')
        #mecccam
for j in range(len(labelsm)):
    try:
        host=serversm[len(labelsm)-1-j][0]
        port=serversm[len(labelsm)-1-j][1]
        user=serversm[len(labelsm)-1-j][2]
        pasw=serversm[len(labelsm)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= ' +str(j)+'_'+ labelsm[len(labelsm)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
# ============================== oscam @ config folder  ========================================
if os.path.isfile('tmp//config/oscam.server'):
    the_pag=open('tmp//config/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>438:
    the_pag=open('tmp//config/oscam.server','w')
    i=0
    while i <438:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//config/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//config/oscam.server','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00;098C:000000;09C4:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1')

    except IndexError:
        pass
the_pag.close()
#======= NLINES ====================
if os.path.isfile('tmp//Nlines/oscam.server'):
    the_pag=open('tmp//Nlines/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()

if len(the_page)>70:
    the_pag=open('tmp//Nlines/oscam.server','w')
    i=0
    while i <70:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('tmp//Nlines/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('tmp//Nlines/oscam.server','a')
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
the_pag.close()
