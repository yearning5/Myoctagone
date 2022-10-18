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
import re
#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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
def f8(seq):
    cc4=sorted(seq,key=lambda x: x[0]and x[1])
    cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
    return cc4
try:
    link2='http://www.testious.com/free-cccam-servers'
    link=link2.strip('\r\n')
    import datetime
    link3='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()).strftime('%Y-%m-%d')
    #f = requests.get(link3,headers=UserAgent)
    ff=urllib2.Request(link3, headers=hdr)
    f=urllib2.urlopen(ff)
    #the_page = f.text
    #the_page =the_page.encode('ascii', 'ignore')
    the_page =f.read()
    #ta=re.findall(r'C: (.*?)</div><!--text-->',the_page,re.DOTALL)
    tbc=re.findall(r'C: (.*?) #',the_page,re.DOTALL)
    tbcc=[b.split(' ') for b in tbc]
    #tbcc=sorted(tbcc)
    #tbbc=[tbcc[i] for i in range(len(tbcc)) if tbcc[i][0] != tbcc[i-1][0] or tbcc[i][0] == tbcc[i-1][0] and tbcc[i][1] != tbcc[i-1][1]]
    #testious=tbbc
    testious=f8(tbcc)
    if testious==[]:
        testious=[['testious-err','testious-err','testious-err','testious-err']]

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
    f = requests.get(link1,headers=UserAgent)
    #ff=urllib2.Request(link3, headers=hdr)
    #f=urllib2.urlopen(ff)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    #the_page =f.read()
    #the_page=the_page.split('\n')
    #reverse list
    a=re.findall(r'status_icon_online(.*?)Show',the_page,re.DOTALL)
    bc=[re.findall(r'href="/info/CCcam/(.*?)/',bb,re.DOTALL) for bb in a]
    bcc=[bb[0].split('_') for bb in bc if bb !=[]] or [['err'],['err'],['err'],['err']]
    #bcc=sorted(bcc)
    #bbc=[bcc[i] for i in range(len(bcc)) if bcc[i][0] != bcc[i-1][0] or bcc[i][0] == bcc[i-1][0] and bcc[i][1] != bcc[i-1][1]]
    #freecline=bbc
    freecline=f8(bcc)
    if freecline==[]:
        freecline=[['freecline-err','freecline-err','freecline-err','freecline-err']]
except:
    Host='freecline-err'
    Port='freecline-err'
    User='freecline-err'
    Pass='freecline-err'
    freecline=[[Host, Port, User, Pass]]

fcnoip11=[]
for i in testious:
    if 'fcnoip' in i[0] or 'bemhd' in i[0]:
        fcnoip11.append(i)
fcnoip21=[]
for i in freecline:
    if 'fcnoip' in i[0] or 'bemhd' in i[0]:
        fcnoip21.append(i)
fcnoip12=f8(fcnoip11)
fcnoip22=f8(fcnoip21)


