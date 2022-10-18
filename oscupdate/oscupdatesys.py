import os
import os.path
import datetime
import re
#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"

def f77(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
def f8(seq):
    cc4=sorted(seq,key=lambda x: x[0]and x[1])
    cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
    return cc4

def allccam(link):
    #import requests
    #short url expand
    link=link.strip('\r\n')
    cmd='wget '+link+' -q -O -'
    the_page=os.popen(cmd).read()
    a=re.findall('[C:c]: (.*?)</h2>',the_page)
    if len(a)>0:
        q=re.findall('[C:c]: (.*?)</h2>',the_page)[0].split()
        Host=q[0]
        Port=re.findall('>(.*?)<',q[2])[0]
        User=q[3]
        Pass=q[4]
    else:
        Host='allccam-err'
        Port='allccam-err'
        User='allccam-err'
        Pass='allccam-err'
    return [Host,Port,User,Pass]

def getPage(link):
    link=link.strip('\r\n')
    cmd='wget '+link+' -q -O -'
    the_page=os.popen(cmd).read()
    a=re.findall('[C:c]:(.*?)[<:\n]',the_page)
    if len(a)>0 and len(a[0].split())==4:
        a=a[0].split()
        Host=a[0]
        Port=a[1]
        if 'freeiptv4u.com' in a[0]:
            User=a[2][:-1]+'7'
        else:
            User=a[2]
        Pass=a[3]
    else:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
    return [Host,Port,User,Pass]

def getPage2(link):
    link=link.strip('\r\n').strip()
    cmd='wget '+link+' -q -O -'
    the_page=os.popen(cmd).read()
    
    if len(the_page)>0:
        a=the_page.split()
        Host=a[1]
        Port=a[2]
        User=a[3]
        Pass=a[4]
    else:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
    return [Host,Port,User,Pass]


def ifosat(link):
    link=link.strip('\r\n').strip()
    cmd='wget '+link+' -q -O -'
    the_page=os.popen(cmd).read()
    if len(the_page)>0:        
        Host=re.findall('host: (.*?)[<: ]', the_page)[0]
        Port=re.findall('port: (.*?)[<: ]', the_page)[0]
        User=re.findall('user: (.*?)[<: ]', the_page)[0]
        Pass=re.findall('pass: (.*?)[<: ]', the_page)[0]
    else:
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
    print i
    servers.append(serv)

if os.path.isfile('/oscupdate/dreamosat.txt'):
    the_file=open('/oscupdate/dreamosat.txt','r')
    the_links =the_file.readlines()
    the_file.close()

for i in range(len(the_links)):
    serv=getPage2(the_links[i])
    print i
    servers.append(serv)
#clines Najmsatcamd
if os.path.isfile('/oscupdate/clines.txt'):
    the_fil=open('/oscupdate/clines.txt','r')
    the_clins =the_fil.readlines()
    the_fil.close()
th_clins=the_clins[0]
th_clins1=the_clins[1]
th_clins2=the_clins[2]
th_clins=th_clins.strip('\r\n')
th_clins1=th_clins1.strip('\r\n')
th_clins2=th_clins2.strip('\r\n')
cmdf='wget '+th_clins+' -q -O -'
th_clins=os.popen(cmdf).read()
cmdf1='wget '+th_clins1+' -q -O -'
th_clins1=os.popen(cmdf1).read()
cmdf2='wget '+th_clins2+' -q -O -'
th_clins2=os.popen(cmdf2).read()
anaj0=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins)
anaj1=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins1)
anaj2=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins2)
anaj=anaj0+anaj1+anaj2
cliness=f8(anaj)
if cliness==[]:
    cliness=[['najmsat-err','najmsat-err','najmsat-err','najmsat-err']]
cliness=sorted(cliness)
cliness=f8(cliness)
clina=[]
for i in cliness:
    if 'fcnoip' not in i[0]:
        clina.append(i)
        
for i in range(len(clina)):
    servers.append(clina[i])

# --------------------------------------------------------
# cccam-live.com
# --------------------------------------------------------

link='wget http://www.cccam-live.com/ -q -O -'
the_page = os.popen(link).read()
st=(datetime.datetime.today()).strftime('%Y-%m-%d')
sr='href="(http://www.cccam.*?'+st+'/)'
a=re.findall(sr,the_page)
if len(a)>0:
    
    link0=a[0]
    link0='wget '+link0+' -q -O -'
    the_page0 = os.popen(link0).read()
    cccamlive=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', the_page0)
    cccamlive=f8(cccamlive)
    if cliness==[]:
        cccamlive=[['cccamlive-err','cccamlive-err','cccamlive-err','cccamlive-err']]
else:
    cccamlive=[['cccamlive-err','cccamlive-err','cccamlive-err','cccamlive-err']]

cccamliv=[]
for i in cccamlive:
    if 'fcnoip' not in i[0]:
        cccamliv.append(i)
        
for i in range(len(cccamliv)):
    servers.append(cccamliv[i])    

if os.path.isfile('/oscupdate/allcccam.txt'):
    the_fil=open('/oscupdate/allcccam.txt','r')
    the_lins =the_fil.readlines()
    the_fil.close()

#servs=[]
for i in range(4):
    serv=allccam(the_lins[i])
    print i
    servers.append(serv)

#======cccamlux===============================
lux=the_lins[5]
lux=lux.strip('\r\n')
lux='wget '+lux+' -q -O -'
lux_page=os.popen(lux).read()
c1=lux_page.find('C: ')
c2=lux_page.find(' port: ')
c3=lux_page.find(' user: ')
c4=lux_page.find(' pass: ')
c5=lux_page[c4:].find('<')
if c1>0 and c2>0 and c3>0 and c4>0 and c5>0:
    
    luxhost=lux_page[c1:c2].split()[1]
    luxpor=lux_page[c2:c3].split()[1]
    luxuser=lux_page[c3:c4].split()[1]
    luxpass=lux_page[c4:c4+c5].split()[1]
    luxccam=[luxhost,luxpor,luxuser,luxpass]
else:
    Host=lux.split('/')[2]+'-err'
    Port=lux.split('/')[2]+'-err'
    User=lux.split('/')[2]+'-err'
    Pass=lux.split('/')[2]+'-err'
    luxccam=[[Host, Port, User, Pass]]
servers.append(luxccam)
#======cccamstore===============================
wee=the_lins[7]
wee=wee.strip('\r\n')
wee='wget '+lux+' -q -O -'
the_page =os.popen(wee).read()
c1=the_page.find('C:')
c2=the_page[c1:].find('<')
b1=c2+c1
c3=the_page[b1:].find('>')
b2=b1+c3
c4=the_page[b2:].find('<')
b3=b2+c4
if c1>0 and c2>0 and c3>0 and c4>0:
    storehost=the_page[c1:b1].split()[1]
    storeport=the_page[c1:b1].split()[2]
    storeuser=the_page[c1:b1].split()[3]
    storepass=the_page[b2+1:b3]
    store=[storehost,storeport,storeuser,storepass]
else:
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
#servers.append(khaled2)
#servers.append(khaled1)
#servers.append(khaledsat)
req4 ='http://s1.satunivers.tv/download1.php?file=srtx4.txt'
req4="wget -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' "+req4+" -q -O -"
the_files=os.popen(req4).read()
the_files=the_files.strip('\n\r')
ssr=[the_files.split()[1],the_files.split()[2],the_files.split()[3],the_files.split()[4]]
#servers.append(ssr)
# ================================= freeclines + testious =================================
link2='http://www.testious.com/free-cccam-servers'
link=link2.strip('\r\n')
link3='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()).strftime('%Y-%m-%d')
lin="wget -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' "+link3+" -q -O -"
the_page = os.popen(lin).read()
tbc=re.findall(r'C: (.*?) #',the_page,re.DOTALL)
if len(tbc)>0:
    tbcc=[b.split(' ') for b in tbc]
    
    testious=f8(tbcc)
    if testious==[]:
        testious=[['testious-err','testious-err','testious-err','testious-err']]

else:
    Host='testious-err'
    Port='testious-err'
    User='testious-err'
    Pass='testious-err'
    testious=[[Host, Port, User, Pass]]


# free
link1='http://www.freecline.com/index'
link=link1.strip('\r\n')
lin="wget -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' "+link+" -q -O -"
the_page = os.popen(lin).read()
a=re.findall(r'status_icon_online(.*?)Show',the_page,re.DOTALL)
bc=[re.findall(r'href="/info/CCcam/(.*?)/',bb,re.DOTALL) for bb in a]
if len(bc)>0:
    bcc=[bb[0].split('_') for bb in bc if bb !=[]] or [['err'],['err'],['err'],['err']]
    freecline=f8(bcc)
    if freecline==[]:
        freecline=[['freecline-err','freecline-err','freecline-err','freecline-err']]
else:
    Host='freecline-err'
    Port='freecline-err'
    User='freecline-err'
    Pass='freecline-err'
    freecline=[[Host, Port, User, Pass]]
## 4cardsharing
card='http://www.4cardsharing.com'
linkk4=card.strip('\r\n')
lin="wget -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' "+linkk4+" -q -O -"
the_page = os.popen(lin).read()    #fff4 = requests.get(linkk4,headers=UserAgent)#,proxies=proxiess)
from datetime import date, timedelta
teod=(datetime.datetime.now()- timedelta(1)).strftime('%d-%m-%Y')
yest=(datetime.datetime.now()- timedelta(2)).strftime('%d-%m-%Y')
c1=pag4.find(teod+'/"')
c2=pag4.find(yest+'/"')
if c1>0 and c2>0:
    ccc4=re.findall(r'C: (.*?) (.*?) (.*?) (.*?)[ :<:\n]',pag4[c1:c2],re.DOTALL)
    cccc4=[s for s in ccc4 if '\n' not in s[2]]
    #cc4=sorted(cccc4)
    #cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or [['err'],['err'],['err'],['err']]
    #card4sh=cc4
    card4sh=f8(cccc4)
    if card4sh==[]:
        card4sh=[['card4sh-err','card4sh-err','card4sh-err','card4sh-err']]

else:
    Host='card4sh-err'
    Port='card4sh-err'
    User='card4sh-err'
    Pass='card4sh-err'
    card4sh=[[Host, Port, User, Pass]]


serversm=card4sh+freecline+testious
fcnoip11=[]
for i in testious or freecline or card4sh:
    if 'egypt' in i[0] or 'bemhd' in i[0]:
        fcnoip11.append(i)
for i in freecline:
    if 'egypt' in i[0] or 'bemhd' in i[0]:
        fcnoip11.append(i)
fcnoip12=f8(fcnoip11)
if fcnoip12==[]:
    fcnoip12=[['fcnoip12-err','fcnoip12-err','fcnoip12-err','fcnoip12-err']]

for n in fcnoip12:
    servers.append(n)
#from CCcamTester import TestCline
#serversm=[]
#for i in serversmww:
#    s='C: '+i[0]+' '+i[1]+' '+i[2]+' '+i[3]
#    if TestCline(s)==True:
#        serversm.append(i)

#serversm=sorted(serversm)
#serversm=[serversm[i] for i in range(len(serversm)) if serversm[i][0] != serversm[i-1][0] or i==0 or serversm[i][0] == serversm[i-1][0] and serversm[i][1] != serversm[i-1][1]] or [['err'],['err'],['err'],['err']]
serversm=f8(serversm)
if serversm==[]:
    serversm=[['serversm-err','serversm-err','serversm-err','serversm-err']]
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

if len(the_page)>412:
    the_pag=open('/etc/tuxbox/config/gcam.server','w')
    i=0
    while i <412:
        the_pag.write(the_page[i])
        i +=1
    the_pag.close()
the_pag=open('/etc/tuxbox/config/gcam.server','r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open('/etc/tuxbox/config/gcam.server','a')
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

