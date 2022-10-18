import os, subprocess
import re,random,string

import urllib3
urllib3.disable_warnings()
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

UserAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; Linux x86_64; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Safari/537.36',
            'Accept': 'text/html'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def getPage(link):
    link=link.strip('\r\n')
    try:
        cmd=('curl -s -L -m 5 "'+link+'"')
        the_page =subprocess.check_output(cmd,shell=True)
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('c |c: (.*?)[<:\n:"]',the_page,re.IGNORECASE)
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
        nm= a[0][:15]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
        nm='error'
    return [Host,Port,User,Pass,nm]

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

# infosat MgCAMD2

try:
    serv=getPage('http://www.vipcccam.net/freetest.php')
    lab='My_'+serv[4]
    print serv[2]
    if lab!='':
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if lab in read[i]:
                read[i+3]='user                          = '+serv[2]+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass



# infosat MgCAMD2

try:
    try:
        aa=subprocess.check_output('curl -s --max-time 10 "http://infosat.satunivers.tv/mgfr/" --data "user=anaana&pass=anaana"', shell=True)
    except:
        aa=os.popen('curl -s --max-time 10 "http://infosat.satunivers.tv/mgfr/" --data "user=anaana&pass=anaana"').read()
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
                print mguser
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
    try:
        aa1=subprocess.check_output('curl -s --max-time 10 "http://infosat.satunivers.tv/mg/" --data "user=anaana&pass=anaana"', shell=True)
    except:
        aa1=os.popen('curl -s --max-time 10 "http://infosat.satunivers.tv/mg/" --data "user=anaana&pass=anaana"').read()
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
                print mguser1
                break
        ffii=open(source,'w')
        for i in read1:
            ffii.write(i)
        ffii.close()
except:
    pass

if os.path.isfile('/oscupdate/my-servers.txt'):
    the_file=open('/oscupdate/my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()

# ccamtiger
my_servers=[]
for i in range(len(the_links)):
    serv=getPage(the_links[i])
    serv[4]='My_'+serv[4]
    #print i
    my_servers.append(serv)

my_servers1=[]
for  i in my_servers:
    if 'error' not in i:
        my_servers1.append(i)


ffii=open(source,'r')
read=ffii.readlines()
ffii.close()
for j in my_servers1:
    for i in range(len(read)):
        if all(x in read[i] for x in ['label',j[4]]):
            read[i+2]='device                        = '+j[0]+','+j[1]+'\n'
            read[i+3]='user                          = '+j[2]+'\n'
            read[i+4]='password                      = '+j[3]+'\n'
            print j[4]

fii=open(source,'w')
for i in read:
    fii.write(i)
fii.close()