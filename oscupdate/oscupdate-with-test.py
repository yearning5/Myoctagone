import urllib2
import urllib
import base64
import os
import os.path
import requests
from urllib2 import Request, urlopen
import httplib
import re
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
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
        f = requests.get(a)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        q=re.findall('[C:c]: (.*?)</h2>',the_page)[0].split()
        Host=q[0]
        Port=re.findall('>(.*?)<',q[2])[0]
        User=q[3]
        Pass=q[4]
    except:
        Host='allccam-err'
        Port='allccam-err'
        User='allccam-err'
        Pass='allccam-err'
    return [Host,Port,User,Pass]

def getPage(link):
    import requests
    link=link.strip('\r\n')
    try:
        f = requests.get(link)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        a=re.findall('[C:c]: (.*?)[<:\n]',the_page)[0].split()
        Host=a[0]
        Port=a[1]
        if 'freeiptv4u.com' in a[0]:
            User=a[2][:-1]+'53'
        else:
            User=a[2]
        Pass=a[3]
    except:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
    return [Host,Port,User,Pass]

def ifosat(link):
    try:
        urllib.urlretrieve(link, ('/tmp/Server_infosat.txt'))
        if os.path.isfile('/tmp/Server_infosat.txt'):
            the_pag=open('/tmp/Server_infosat.txt','rt')
            the_page =the_pag.read()
            the_file.close()
        Host=re.findall('host: (.*?)[<: ]', the_page)[0]
        Port=re.findall('port: (.*?)[<: ]', the_page)[0]
        User=re.findall('user: (.*?)[<: ]', the_page)[0]
        Pass=re.findall('pass: (.*?)[<: ]', the_page)[0]
    except:
        Host='ifosat-err'
        Port='ifosat-err'
        User='ifosat-err'
        Pass='ifosat-err'
    return  [Host, Port, User, Pass]

if os.path.isfile('/oscupdate/my-servers.txt'):
    the_file=open('/oscupdate/my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()
servers=[]
for i in range(len(the_links)):
    serv=getPage(the_links[i])
    servers.append(serv)

#clines
if os.path.isfile('/oscupdate/clines.txt'):
    the_fil=open('/oscupdate/clines.txt','r')
    the_clins =the_fil.readlines()
    the_fil.close()
try:
    th_clins=the_clins[0]
    th_clins=th_clins.strip('\r\n')
    f = requests.get(th_clins,headers=UserAgent)
    th_clins = f.text
    th_clins =th_clins.encode('ascii', 'ignore')
    anaj=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins)
    cc4=sorted(anaj)
    cliness=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or [['err'],['err'],['err'],['err']]
except:
    cliness=[['najmsat-err','najmsat-err','najmsat-err','najmsat-err']]
for i in cliness:
    for a in servers:
        if i[0] in a[0]:
            cliness.remove(i)

for i in range(len(cliness)):
    servers.append(cliness[i])
    
if os.path.isfile('/oscupdate/allcccam.txt'):
    the_fil=open('/oscupdate/allcccam.txt','r')
    the_lins =the_fil.readlines()
    the_fil.close()

#servs=[]
for i in range(4):
    serv=allccam(the_lins[i])
    servers.append(serv)
#======buy-iptv===============================
lubuy=the_lins[9]
lubuy=lubuy.strip('\r\n')
try:
    f = requests.get(lubuy)
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
    Host=lubuy.split('/')[2]+'-err'
    Port=lubuy.split('/')[2]+'-err'
    User=lubuy.split('/')[2]+'-err'
    Pass=lubuy.split('/')[2]+'-err'
    buyiptv=[[Host, Port, User, Pass]]
servers.append(buyiptv)
#======cccamlux===============================
lux=the_lins[5]
lux=lux.strip('\r\n')
try:
    request = Request(lux)
    response = urlopen(request)
    lux_page = response.read()
    c1=lux_page.find('C: ')
    c2=lux_page.find(' port: ')
    c3=lux_page.find(' user: ')
    c4=lux_page.find(' pass: ')
    c5=lux_page[c4:].find('<')
    luxhost=lux_page[c1:c2].split()[1]
    luxpor=lux_page[c2:c3].split()[1]
    luxuser=lux_page[c3:c4].split()[1]
    luxpass=lux_page[c4:c4+c5].split()[1]
    luxccam=[luxhost,luxpor,luxuser,luxpass]
except:
    Host=lux.split('/')[2]+'-err'
    Port=lux.split('/')[2]+'-err'
    User=lux.split('/')[2]+'-err'
    Pass=lux.split('/')[2]+'-err'
    luxccam=[[Host, Port, User, Pass]]
servers.append(luxccam)
#======cccamstore===============================
wee=the_lins[7]
wee=wee.strip('\r\n')
try:
    request = Request(wee)
    response = urlopen(request)
    the_page = response.read()
    c1=the_page.find('C:')
    c2=the_page[c1:].find('<')
    b1=c2+c1
    c3=the_page[b1:].find('>')
    b2=b1+c3
    c4=the_page[b2:].find('<')
    b3=b2+c4
    storehost=the_page[c1:b1].split()[1]
    storeport=the_page[c1:b1].split()[2]
    storeuser=the_page[c1:b1].split()[3]
    storepass=the_page[b2+1:b3]
    store=[storehost,storeport,storeuser,storepass]
except:
    Host=wee.split('/')[2]+'-err'
    Port=wee.split('/')[2]+'-err'
    User=wee.split('/')[2]+'-err'
    Pass=wee.split('/')[2]+'-err'
    store=[[Host, Port, User, Pass]]
servers.append(store)
#=============================================
#servers.append(servs)
req3 ='http://infosat.satunivers.tv/cgn/index1.php'
khaledsat=ifosat(req3)
req1 ='http://server.satunivers.tv/server2/'
khaled1=ifosat(req1)
req ='http://infosat.satunivers.tv/download1.php?file=srtx5.txt'
khaled2=ifosat(req)
servers.append(khaled2)
servers.append(khaled1)
servers.append(khaledsat)
req4 ='http://s1.satunivers.tv/download1.php?file=srtx4.txt'
urllib.urlretrieve(req4, ('/tmp/Server_infosat.txt'))
the_file=open('/tmp/Server_infosat.txt','rt')
the_files =the_file.read()
ssr=[the_files.split()[1],the_files.split()[2],the_files.split()[3],the_files.split()[4]]
servers.append(ssr)
# ================================= freeclines + testious =================================
try:
    link2='http://www.testious.com/free-cccam-servers'
    link=link2.strip('\r\n')
    f = requests.get(link,headers=UserAgent)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    ta=re.findall(r'C: (.*?)</div><!--text-->',the_page,re.DOTALL)
    tbc=re.findall(r'C: (.*?) #',ta[0],re.DOTALL)
    tbcc=[b.split(' ') for b in tbc]
    tbcc=sorted(tbcc)
    tbbc=[tbcc[i] for i in range(len(tbcc)) if tbcc[i][0] != tbcc[i-1][0] or tbcc[i][0] == tbcc[i-1][0] and tbcc[i][1] != tbcc[i-1][1]]
    testious=tbbc
except:
    Host='testious-err'
    Port='testious-err'
    User='testious-err'
    Pass='testious-err'
    testious=[[Host, Port, User, Pass]]


# free
try:
    link1='http://www.freecline.com/index'
    link=link1.strip('\r\n')
    f = requests.get(link,headers=UserAgent)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    #the_page=the_page.split('\n')
    #reverse list
    a=re.findall(r'status_icon_online(.*?)Show',the_page,re.DOTALL)
    bc=[re.findall(r'href="/info/CCcam/(.*?)/',bb,re.DOTALL) for bb in a]
    bcc=[bb[0].split('_') for bb in bc if bb !=[]] or [['err'],['err'],['err'],['err']]
    bcc=sorted(bcc)
    bbc=[bcc[i] for i in range(len(bcc)) if bcc[i][0] != bcc[i-1][0] or bcc[i][0] == bcc[i-1][0] and bcc[i][1] != bcc[i-1][1]]
    freecline=bbc
except:
    Host='freecline-err'
    Port='freecline-err'
    User='freecline-err'
    Pass='freecline-err'
    freecline=[[Host, Port, User, Pass]]
## 4cardsharing
try:
    card='http://www.4cardsharing.com'
    linkk4=card.strip('\r\n')
    fff4 = requests.get(linkk4,headers=UserAgent)#,proxies=proxiess)
    pag4 = fff4.text
    pag4 =pag4.encode('ascii', 'ignore')
    import datetime
    from datetime import date, timedelta
    teod=(datetime.datetime.now()- timedelta(1)).strftime('%d-%m-%Y')
    yest=(datetime.datetime.now()- timedelta(2)).strftime('%d-%m-%Y')
    c1=pag4.find(teod+'/"')
    c2=pag4.find(yest+'/"')
    ccc4=re.findall(r'C: (.*?) (.*?) (.*?) (.*?)[ :<:\n]',pag4[c1:c2],re.DOTALL)
    cccc4=[s for s in ccc4 if '\n' not in s[2]]
    cc4=sorted(cccc4)
    cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or [['err'],['err'],['err'],['err']]
    card4sh=cc4
except:
    Host='card4sh-err'
    Port='card4sh-err'
    User='card4sh-err'
    Pass='card4sh-err'
    card4sh=[[Host, Port, User, Pass]]

# cccam.date
try:
    amdat='http://cccam.date'
    linkk5=amdat.strip('\r\n')
    fff5 = requests.get(linkk5,headers=UserAgent)#,proxies=proxiess)
    pag5 = fff5.text
    pag5 =pag5.encode('ascii', 'ignore')
    amdat2=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :\n]', pag5)
    cc4=sorted(amdat2)
    dat=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or [['err'],['err'],['err'],['err']]
except:
    Host='m.date-err'
    Port='m.date-err'
    User='m.date-err'
    Pass='m.date-err'
    dat=[[Host, Port, User, Pass]]
                                                       
serversmww=card4sh+freecline+testious+dat

from CCcamTester import TestCline
serversm=[]
for i in serversmww:
    s='C: '+i[0]+' '+i[1]+' '+i[2]+' '+i[3]
    if TestCline(s)==True:
        serversm.append(i)

serversm=sorted(serversm)
serversm=[serversm[i] for i in range(len(serversm)) if serversm[i][0] != serversm[i-1][0] or i==0 or serversm[i][0] == serversm[i-1][0] and serversm[i][1] != serversm[i-1][1]] or [['err'],['err'],['err'],['err']]
labelsm=[]
for i in range(len(serversm)):
    labelsm.append(serversm[i][0])
# =========================================================================================
#======= oscam ====================
if os.path.isfile('/etc/tuxbox/oscam-emu/oscam.server'):
    the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>412:
    the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','w')
    i=0
    while i <412:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','a')
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
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
    except IndexError:
        pass
the_pag.close()
#======= Ncam ====================
if os.path.isfile('/etc/tuxbox/config/ncam.server'):
    the_pag=open('/etc/tuxbox/config/ncam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>16:
    the_pag=open('/etc/tuxbox/config/ncam.server','w')
    i=0
    while i <16:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/config/ncam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/config/ncam.server','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
    except IndexError:
        pass
the_pag.close()
#======= G-CAMD ====================
if os.path.isfile('/etc/tuxbox/config/gcam.server'):
    the_pag=open('/etc/tuxbox/config/gcam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>16:
    the_pag=open('/etc/tuxbox/config/gcam.server','w')
    i=0
    while i <16:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/config/gcam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/config/gcam.server','a')
        #mecccam
for j in range(len(labelsm)):
    try:
        host=serversm[len(labelsm)-1-j][0]
        port=serversm[len(labelsm)-1-j][1]
        user=serversm[len(labelsm)-1-j][2]
        pasw=serversm[len(labelsm)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labelsm[len(labelsm)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
    except IndexError:
        pass
the_pag.close()
#======= wicardd ====================
if os.path.isfile('/etc/tuxbox/config/wicardd.conf'):
    the_pag=open('/etc/tuxbox/config/wicardd.conf','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>253:
    the_pag=open('/etc/tuxbox/config/wicardd.conf','w')
    i=0
    while i <253:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/config/wicardd.conf','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/config/wicardd.conf','a')
        #mecccam
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n[reader]\nname= ' + labels[len(labels)-1-j] + '\nactive= 1\ntype= cccam\naccount=' + user + ':' + pasw + '@' + host + ':' + port + '\ndebug = 1\nreconnect_delay = 1\nemm_cache = 1\necm_ttl = 15000\nreconnect_to_account_ip =1')
    except IndexError:
        pass
the_pag.close()
# ============================== oscam Modern ========================================
if os.path.isfile('/etc/tuxbox/oscammodern/oscam.server'):
    the_pag=open('/etc/tuxbox/oscammodern/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>412:
    the_pag=open('/etc/tuxbox/oscammodern/oscam.server','w')
    i=0
    while i <412:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/oscammodern/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/oscammodern/oscam.server','a')
        #mecccam
for j in range(len(labelsm)):
    try:
        host=serversm[len(labelsm)-1-j][0]
        port=serversm[len(labelsm)-1-j][1]
        user=serversm[len(labelsm)-1-j][2]
        pasw=serversm[len(labelsm)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= ' +str(j)+'_'+ labelsm[len(labelsm)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
    except IndexError:
        pass
the_pag.close()
# ============================== oscam @ config folder  ========================================
if os.path.isfile('/etc/tuxbox/config/oscam.server'):
    the_pag=open('/etc/tuxbox/config/oscam.server','r')
    the_page =the_pag.readlines()
    the_pag.close()
    
if len(the_page)>412:
    the_pag=open('/etc/tuxbox/config/oscam.server','w')
    i=0
    while i <412:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/config/oscam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/config/oscam.server','a')
        #mecccam
for j in range(len(labelsm)):
    try:
        host=serversm[len(labelsm)-1-j][0]
        port=serversm[len(labelsm)-1-j][1]
        user=serversm[len(labelsm)-1-j][2]
        pasw=serversm[len(labelsm)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= ' +str(j)+'_'+ labelsm[len(labelsm)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:030B00\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
    except IndexError:
        pass
the_pag.close()
    
