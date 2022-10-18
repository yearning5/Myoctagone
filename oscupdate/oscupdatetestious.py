import urllib2
import urllib
import base64
import os
import os.path
import requests
from urllib2 import Request, urlopen
import httplib
def allccam(link):
    import requests
    #short url expand
    import httplib
    try:
        conn = httplib.HTTPConnection(link.strip().split('/')[2])
        conn.request('HEAD', '/'+link.strip().split('/')[3])
        response = conn.getresponse()
        response.getheader('location')
    except:
         pass
    a=response.getheader('location')
    #get server data
    try:
        f = requests.get(a)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        c1=the_page.find('C:')
        c2=the_page[c1:].find('<')
        b1=c1+c2
        Host=the_page[c1:b1].split()[1]
        c3=the_page[b1:].find('>')
        b2=b1+c3
        c4=the_page[b2:].find('<')
        b3=b2+c4
        Port=the_page[b2+1:b3]
        c5=the_page[b3:].find(' ')
        b4=b3+c5
        c6=the_page[b4:].find('<')
        b5=c6+b4
        User=the_page[b4:b5].split()[0]
        Pass=the_page[b4:b5].split()[1]
    except IndexError:
        ser=['web-err','web-err','web-err','web-err','web-err']
        Host=ser[1]
        Port=ser[2]
        User=ser[3]
        Pass=ser[4]
    return [Host,Port,User,Pass]

def getPage(link):
    import requests
    link=link.strip('\r\n')
    try:
        f = requests.get(link)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        if the_page.find('C:')>-1:
            c1=the_page.find('C:')
            c2=the_page[c1:].find('<')
        elif the_page.find('c:')>-1:
            c1=the_page.find('c:')
            c2=the_page[c1:].find('<')
        the_page[c1:c1+c2]
        host=the_page[c1:c2+c1].split()[1]
        port=the_page[c1:c2+c1].split()[2]
        user=the_page[c1:c2+c1].split()[3]
        Pass =the_page[c1:c2+c1].split()[4]
    except:
        ser=['web-err','web-err','web-err','web-err','web-err']
        host=ser[1]
        port=ser[2]
        user=ser[3]
        Pass=ser[4]
    return [host,port,user,Pass]


def ifosat(link):
    try:
        urllib.urlretrieve(link, ('/tmp/Server_infosat.txt'))
    except:
        ser=['web-err','web-err','web-err','web-err','web-err']
        host=ser[1]
        port=ser[2]
        user=ser[3]
        Pass=ser[4]
        return  [host, port, user, Pass]
    if os.path.isfile('/tmp/Server_infosat.txt'):
        the_pag=open('/tmp/Server_infosat.txt','rt')
        the_page =the_pag.read()
        c1=the_page.find("host: ")
        if any(l in the_page[c1:] for l in('<'))==True:
            c11=the_page[c1:].find("<")
            Host=the_page[c1:c1+c11].split()[1]
        elif any(l in the_page[c1:] for l in('<'))==False:
            c11=the_page[c1+6:].find(" ")
            Host=the_page[c1:c1+6+c11].split()[1]
        c2=the_page.find('port: ')
        if any(l in the_page[c2:] for l in('<'))==True:
            c22=the_page[c2:].find("<")
            Port=the_page[c2:c2+c22].split()[1]
        elif any(l in the_page[c2:] for l in('<'))==False:
            c22=the_page[c2+6:].find(" ")
            Port=the_page[c2:c2+6+c22].split()[1]
        c3=the_page.find('user: ')
        if any(l in the_page[c3:] for l in('<'))==True:
            c33=the_page[c3:].find("<")
            User=the_page[c3:c3+c33].split()[1]
        elif any(l in the_page[c3:] for l in('<'))==False:
            c33=the_page[c3+6:].find(" ")
            User=the_page[c3:c3+6+c33].split()[1]
        c4=the_page.find('pass: ')
        c44=the_page[c4+6:].find(" ") 
        Pass=the_page[c4:c4+6+c44].split()[1]
    
    return  [Host, Port, User, Pass]

def clines(link):
    link=link.strip('\r\n')
    f = requests.get(link)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    serf=[]
    b=0
    if the_page.rfind('C: ')>-1:
        count=the_page.rfind('C: ')
    elif the_page.rfind('c: ')>-1:
        count=the_page.rfind('C: ')
    while b <count+1:
        #print b
        if the_page[b:].find('C: ')>-1:
            c1=the_page[b:].find('C: ')
            c2=the_page[b+c1:].find('<')
        elif the_page.find('c: ')>-1:
            c1=the_page[b:].find('c: ')
            c2=the_page[c1+b:].find('<')
        try:
            the_page[c1+b:b+c1+c2]
            host=the_page[c1+b:b+c1+c2].split()[1]
            port=the_page[c1+b:b+c1+c2].split()[2]
            user=the_page[c1+b:b+c1+c2].split()[3]
            Pass =the_page[c1+b:b+c1+c2].split()[4]
            ser=[host,port,user,Pass]
            serf.append(ser)
        except IndexError:
            pass
        #b=b+c1+c2
        b=b+c1+c2
    servs=[]
    for i in range(len(serf)-1):
        j=i+1
        if serf[i][0] != serf[j][0]:
            servs.append(serf[i])
    servs.append(serf[len(serf)-1])
    return servs

if os.path.isfile('/oscupdate/my-servers.txt'):
    the_file=open('/oscupdate/my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()
servers=[]
for i in range(len(the_links)):
    serv=getPage(the_links[i])
    servers.append(serv)

if os.path.isfile('/oscupdate/clines.txt'):
    the_fil=open('/oscupdate/clines.txt','r')
    the_clins =the_fil.readlines()
    the_fil.close()
cliness=clines(the_clins[0])

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
    buyiptv=['err','err','err','err']
servers.append(buyiptv)
#======cccamlux===============================
lux=the_lins[5]
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
    luxccam=['err','err','err','err']
servers.append(luxccam)
#======cccamstore===============================
wee=the_lins[7]
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
    serv=['err','err','err','err']
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
labels=[]
for i in range(len(servers)):
    labels.append(servers[i][0])
#=============================freecline====================
try:
    link='http://www.freecline.com/index'
    link=link.strip('\r\n')
    f = requests.get(link)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    #the_page=the_page.split('\n')
    #reverse list
    page=the_page[::-1]
    last=the_page.rfind('status_icon_online')
    first=the_page.find('status_icon_online')
    i =0
    c11=0
    freecline=[]
    while i <last:
        # print i,c11
        first=the_page[i:].find('status_icon_online')
        c1=the_page[:first+c11].rfind('>C: ')
        c2=the_page[c1:first+c11].find('<')
        host=the_page[c1:c1+c2].split()[1]
        port=the_page[c1:c1+c2].split()[2]
        user=the_page[c1:c1+c2].split()[3]
        Pass=the_page[c1:c1+c2].split()[4]
        serr=[host,port,user,Pass]
        freecline.append(serr)
        c11=first+c11
        i = i+1 + first
except:
    freecline=['web-err','web-err','web-err','web-err','web-err']
#================================================================
for i in range(len(freecline)):
    for j in range(len(labels)):
        if labels.count(freecline[i][0])==0:
            labels.append(freecline[i][0])
            servers.append(freecline[i])

#=============================testious===========================
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
try:
    link2='http://www.testious.com/free-cccam-servers'
    link=link2.strip('\r\n')
    f = requests.get(link,headers=UserAgent)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    #the_page=the_page.split('\n')
    #reverse list
    page=the_page[::-1]
    first=the_page.find('C: ')
    last=the_page[first:].find('</div><!--text-->')+first
    testou=the_page[first:last]
    serf=[]
    b=0
    if testou.rfind('C: ')>-1:
        count=testou.rfind('C: ')
    elif testou.rfind('c: ')>-1:
        count=testou.rfind('C: ')
    while b <count+1:
        #print b
        if testou[b:].find('C: ')>-1:
            c1=testou[b:].find('C: ')
            c2=testou[b+c1:].find('<')
        elif testou.find('c: ')>-1:
            c1=testou[b:].find('c: ')
            c2=testou[c1+b:].find('<')
        try:
            testou[c1+b:b+c1+c2]
            host=testou[c1+b:b+c1+c2].split()[1]
            port=testou[c1+b:b+c1+c2].split()[2]
            user=testou[c1+b:b+c1+c2].split()[3]
            Pass =testou[c1+b:b+c1+c2].split()[4]
            ser=[host,port,user,Pass]
            serf.append(ser)
        except IndexError:
            pass
        
        #b=b+c1+c2
        b=b+c1+c2
    ttous=[]
    for i in range(len(serf)-1):
        j=i+1
        if serf[i][0] != serf[j][0]:
            ttous.append(serf[i])
    ttous.append(serf[len(serf)-1])
except:
    ttous=['web-err','web-err','web-err','web-err','web-err']
    

#================================================================
for i in range(len(ttous)):
    for j in range(len(labels)):
        if labels.count(ttous[i][0])==0:
            labels.append(ttous[i][0])
            servers.append(ttous[i])

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
for j in range(len(labels)):
    try:
        host=servers[len(labels)-1-j][0]
        port=servers[len(labels)-1-j][1]
        user=servers[len(labels)-1-j][2]
        pasw=servers[len(labels)-1-j][3]
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:032830,030B00;1811:003311;1819:00006D\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
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
        the_pag.write('\n\n[reader]\nlabel= '+str(j+1)+'_' + labels[len(labels)-1-j] + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:032830,030B00;1811:003311;1819:00006D\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1')
            
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
    
    
