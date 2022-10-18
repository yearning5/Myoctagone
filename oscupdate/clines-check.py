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
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ccmd='export PYTHONWARNINGS="ignore:Unverified HTTPS request"'
os.system(ccmd)
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
the_clins=['http://najmsatcamd.blogspot.com','http://free-cccamm.blogspot.com/','http://www.cccam2.com/daily-cccam/']

try:
    th_clins=the_clins[0]
    th_clins1=the_clins[1]
    th_clins2=the_clins[2]
    th_clins=th_clins.strip('\r\n')
    th_clins1=th_clins1.strip('\r\n')
    th_clins2=th_clins2.strip('\r\n')
    f = requests.get(th_clins,headers=UserAgent)
    f1 = requests.get(th_clins1,headers=UserAgent)
    f2 = requests.get(th_clins2,headers=UserAgent)
    th_clins = f.text.encode('ascii', 'ignore')
    th_clins1 = f1.text.encode('ascii', 'ignore')
    th_clins2 = f1.text.encode('ascii', 'ignore')
    anaj0=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins)
    anaj1=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins1)
    anaj2=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :&#:":=:\n]', th_clins2)
    anaj=anaj0+anaj1+anaj2
    #cc4=sorted(anaj)
    #cliness=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or [['err'],['err'],['err'],['err']]
    cliness=f8(anaj)
    if cliness==[]:
        cliness=[['najmsat-err','najmsat-err','najmsat-err','najmsat-err']]
except:
    cliness=[['najmsat-err','najmsat-err','najmsat-err','najmsat-err']]

a=f8(cliness)

for i in cliness:
    for a in servers:
        if i[0] in a[0]:
            cliness.remove(i)

for i in range(len(cliness)):
    servers.append(cliness[i])
