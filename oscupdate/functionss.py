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
        Host='allccam-err'
        Port='allccam-err'
        User='allccam-err'
        Pass='allccam-err'
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
                print 'noway...2 times'
                f.status_code='retry errors'
                pass
        if f.status_code=='retry errors':
            f = requests.get(link,headers=UserAgent,timeout=10)
        the_page = f.text.encode('ascii', 'ignore')
        a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
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
def getPage2(link):
    import requests
    link=link.strip('\r\n').strip()
    try:
        f = requests.get(link,headers=UserAgent,timeout=10)
        the_page = f.text
        the_page =the_page.encode('ascii', 'ignore')
        a=the_page.split()
        Host=a[1]
        Port=a[2]
        User=a[3]
        Pass=a[4]
    except:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
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
        Host='ifosat-err'
        Port='ifosat-err'
        User='ifosat-err'
        Pass='ifosat-err'
    return  [Host, Port, User, Pass]
def ccamfree(link):
    link=link.strip('\r\n')
    UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
     'Accept': 'text/html'}
    def f8(seq):
        cc4=sorted(seq,key=lambda x: x[0]and x[1])
        cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
        return cc4
    try:
        f = requests.get(link,headers=UserAgent,timeout=10,verify=False)
        the_page = f.text.encode('ascii', 'ignore')
        list1=re.findall('[C:c]: (.*?) (.*?) (.*?) (.*?)[<: :\n:\t]', the_page)
        list2=[]
        if len(list1)>0:
            for i in list1:
                if len(i)==4 and i[1].isdigit():
                    list2.append(i)
        else:
            list2=[['l-err','l-err','l-err','l-err']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['l-err','l-err','l-err','l-err']]
    return list2
def nlinefree(link):
    link=link.strip('\r\n')
    import requests
    import re
    UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
     'Accept': 'text/html'}
    def f8(seq):
        cc4=sorted(seq,key=lambda x: x[0]and x[1])
        cc4=[cc4[i] for i in range(len(cc4)) if cc4[i][0] != cc4[i-1][0] or i==0 or cc4[i][0] == cc4[i-1][0] and cc4[i][1] != cc4[i-1][1]] or []
        return cc4
    try:
        f = requests.get(link,headers=UserAgent,timeout=10)
        the_page = f.text.encode('ascii', 'ignore')
        list1=re.findall('N: (.*?) (.*?) (.*?) (.*?)[<: :\n:\t]', the_page)
        list2=[]
        if len(list1)>0:
            for i in list1:
                if len(i)==4:
                    list2.append(i)
        else:
            list2=[['l-err','l-err','l-err','l-err']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['l-err','l-err','l-err','l-err']]
    return list2
