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
import inspect
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno
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
def testccam(cline):
    try:
        #cline="C: s2.satbox.xyz 18801 satbox1000 jazair03"
        cookies = {
            '__cfduid': 'd930257e2e53496f70d8c07d0c26acd9a1617359489',
            '_ga': 'GA1.2.284948668.1617359492',
            '_gid': 'GA1.2.1589687749.1617359492',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'http://www.freecline.com',
            'Alt-Used': 'www.freecline.com:443',
            'Connection': 'keep-alive',
            'Referer': 'http://www.freecline.com/index',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
        }


        data = '{"servers":[{"host":"'+cline.split()[1]+'","port":"'+cline.split()[2]+'","lines":["'+cline+'"]}],"share":false}'

        response = requests.post('http://www.freecline.com/check', headers=headers, cookies=cookies, data=data,timeout=5)
        a=response.text.encode('ascii','ignore')
        res=eval(a)['status'][0]['status']
        if res==1:
            return True
        else:
            return False
    except:
        return False

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
def getPage12(link):
    link=link.strip('\r\n')
    try:
        cmd=('curl -s -L -m 5 "'+link+'"')
        the_page =os.popen(cmd).read()
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

def getPage(link):
    link=link.strip('\r\n')
    try:
        the_page=requests.get(link,verify=False, timeout=5).text.encode('ascii','ignore')
        #cmd=('curl -s -L -m 10 "'+link+'"')
        #the_page =os.popen(cmd).read()
        #a=re.findall('[C:c]:(.*?)[<:\n]',the_page)[0].split()
        a=re.findall('[c |c]: (.*?)[<:\n:":\']',the_page,re.IGNORECASE)
        bb=[]
        for i in a:
            if len(i.split())==4:
                bb.append(i)
        a=bb
        a=random.choice(a)
        a=a.split()
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
        nm= a[1][:15]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
        nm= 'error'
    return [Host,Port,User,Pass,nm]

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
        nm= Host[:15]
    except:
        Host=link.split('/')[2]+'-err'
        Port=link.split('/')[2]+'-err'
        User=link.split('/')[2]+'-err'
        Pass=link.split('/')[2]+'-err'
        nm= 'error'
    return [Host,Port,User,Pass,nm]


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
        nm=Host[:15]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
        nm='error'
    return [Host,Port,User,Pass,nm]

def ifosat(link):
    try:
        data = urllib2.urlopen(link,timeout=5)
        the_page=data.read()
        Host=re.findall('[host:C]: (.*?)[<: ]', the_page,re.DOTALL)[0]
        Port=re.findall('port: (.*?)[<: ]', the_page,re.DOTALL)[0]
        User=re.findall('user: (.*?)[<: ]', the_page,re.DOTALL)[0]
        Pass=re.findall('pass: (.*?)[<: ]', the_page,re.DOTALL)[0]
        nm= Host[:15]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
        nm= 'error'
    return  [Host, Port, User, Pass,nm]

def ccamfree(link,nam):
    nam=nam+'_'
    #import socket
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
            list1=[list(h) for h in list1]
            for i in list1:
                if len(i)==4 and i[1].isdigit():
                    nm=nam+i[0][:16][:-len(nam)]
                    i.append(nm)
                    list2.append(i)
        else:
            list2=[['error','error','error','error','error']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['error','error','error','error','error']]
    return list2

def nlinefree(link,nam):
    nam=nam+'_'
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
                    nm=nam+i[0][:16][:-len(nam)]
                    i.append(nm)
                    list2.append(i)
        else:
            list2=[['error','error','error','error','error']]
        list2=sorted(list2)
        list2=f8(list2)
    except:
        list2=[['error','error','error','error','error']]
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
        nm=Host[:15]
    except:
        Host='error'
        Port='error'
        User='error'
        Pass='error'
        nm='error'
    return [Host,Port,User,Pass,nm]


def socks2():
    d=subprocess.check_output('curl -s https://www.socks-proxy.net/',shell=True)
    dd=re.findall('tbody(.*?)tbody',d)
    ddd=re.findall('tr(.*?)tr',dd[0])
    dddd=[re.findall('<td>(.*?)</td>',i) for i in ddd]
    d1=[i[0]+':'+i[1] for i in dddd if i !=[]]
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --socks4 '+i+' --max-time 3 http://ipecho.net/plain').read()
            if a:
                lisst.append(i)
                break
        except:
            pass
        #print i
    return i

def socks_4():
    '''d=subprocess.check_output('curl -s https://proxyscrape.com/free-proxy-list',shell=True)
    req4=re.findall('href="(.*?)" id="downloadiconsocks4',d)[0]
    req4=req4.replace('timeout=10000','timeout=5000')
    the_files=urllib2.urlopen(req4).read()
    d1=the_files.split()
    lisst=[]
    random.shuffle(d1)'''
    aaa=requests.get('https://hidemy.name/en/proxy-list/?type=4&end=256#list',headers={"User-Agent":"Mozilla/5.0"}).text.encode('ascii', 'ignore')
    dff=re.findall(r'<td>(.*?)</td>',aaa,re.DOTALL)
    qsd=[]
    for i in dff:
        try:
            t=float(i.replace('.',''))
            qsd.append(i)
        except:
            pass
    qsq=[]
    for i in range(0,len(qsd),2):
        qsq.append(qsd[i]+':'+qsd[i+1])
    d1=qsq
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        proxies = {'http': "socks4:"+i}
        try:
            a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=3).text.encode('ascii', 'ignore')
            #print a
            if a:
                c=eval(a)['country']
                ip=eval(a)['query']
                lisst.append(i)
                break
        except:
            pass
        #print i
    return [i,ip,c]

def socks_4c(ccc=None):
    if not ccc:
        ccc='ALL'
    lis=['AF = Afghanistan', 'AL = Albania', 'DZ = Algeria', 'AX = Aland Islands', 'AS = American Samoa', 'AI = Anguilla', 'AD = Andorra', 'AO = Angola', 'AN = Antilles - Netherlands ', 'AG = Antigua and Barbuda', 'AQ = Antarctica', 'AR = Argentina', 'AM = Armenia', 'AU = Australia', 'AT = Austria', 'AW = Aruba', 'AZ = Azerbaijan', 'BA = Bosnia and Herzegovina', 'BB = Barbados', 'BD = Bangladesh', 'BE = Belgium', 'BF = Burkina Faso', 'BG = Bulgaria', 'BH = Bahrain', 'BI = Burundi', 'BJ = Benin', 'BM = Bermuda', 'BN = Brunei Darussalam', 'BO = Bolivia', 'BR = Brazil', 'BS = Bahamas', 'BT = Bhutan', 'BV = Bouvet Island', 'BW = Botswana', 'BV = Belarus', 'BZ = Belize', 'KH = Cambodia', 'CM = Cameroon', 'CA = Canada', 'CV = Cape Verde', 'CF = Central African Republic', 'TD = Chad', 'CL = Chile', 'CN = China', 'CX = Christmas Island', 'CC = Cocos (Keeling) Islands', 'CO = Colombia', 'CG = Congo', "CI = Cote D'Ivoire (Ivory Coast)", 'CK = Cook Islands', 'CR = Costa Rica', 'HR = Croatia (Hrvatska)', 'CU = Cuba', 'CY = Cyprus', 'CZ = Czech Republic', 'CD = Democratic Republic of the Congo', 'DJ = Djibouti', 'DK = Denmark', 'DM = Dominica', 'DO = Dominican Republic', 'EC = Ecuador', 'EG = Egypt', 'SV = El Salvador', 'TP = East Timor', 'EE = Estonia', 'GQ = Equatorial Guinea', 'ER = Eritrea', 'ET = Ethiopia', 'FI = Finland', 'FJ = Fiji', 'FK = Falkland Islands (Malvinas)', 'FM = Federated States of Micronesia', 'FO = Faroe Islands', 'FR = France', 'FX = France, Metropolitan', 'GF = French Guiana', 'PF = French Polynesia', 'GA = Gabon', 'GM = Gambia', 'DE = Germany', 'GH = Ghana', 'GI = Gibraltar', 'GB = Great Britain (UK)', 'GD = Grenada', 'GE = Georgia', 'GR = Greece', 'GL = Greenland', 'GN = Guinea', 'GP = Guadeloupe', 'GS = S. Georgia and S. Sandwich Islands', 'GT = Guatemala', 'GU = Guam', 'GW = Guinea-Bissau', 'GY = Guyana', 'HK = Hong Kong', 'HM = Heard Island and McDonald Islands', 'HN = Honduras', 'HT = Haiti', 'HU = Hungary', 'ID = Indonesia', 'IE = Ireland', 'IL = Israel', 'IN = India', 'IO = British Indian Ocean Territory', 'IQ = Iraq', 'IR = Iran', 'IT = Italy', 'JM = Jamaica', 'JO = Jordan', 'JP = Japan', 'KE = Kenya', 'KG = Kyrgyzstan', 'KI = Kiribati', 'KM = Comoros', 'KN = Saint Kitts and Nevis', 'KP = Korea (North)', 'KR = Korea (South)', 'KW = Kuwait', 'KY = Cayman Islands', 'KZ = Kazakhstan', 'LA = Laos', 'LB = Lebanon', 'LC = Saint Lucia', 'LI = Liechtenstein', 'LK = Sri Lanka', 'LR = Liberia', 'LS = Lesotho', 'LT = Lithuania', 'LU = Luxembourg', 'LV = Latvia', 'LY = Libya', 'MK = Macedonia', 'MO = Macao', 'MG = Madagascar', 'MY = Malaysia', 'ML = Mali', 'MW = Malawi', 'MR = Mauritania', 'MH = Marshall Islands', 'MQ = Martinique', 'MU = Mauritius', 'YT = Mayotte', 'MT = Malta', 'MX = Mexico', 'MA = Morocco', 'MC = Monaco', 'MD = Moldova', 'MN = Mongolia', 'MM = Myanmar', 'MP = Northern Mariana Islands', 'MS = Montserrat', 'MV = Maldives', 'MZ = Mozambique', 'NA = Namibia', 'NC = New Caledonia', 'NE = Niger', 'NF = Norfolk Island', 'NG = Nigeria', 'NI = Nicaragua', 'NL = Netherlands', 'NO = Norway', 'NP = Nepal', 'NR = Nauru', 'NU = Niue', 'NZ = New Zealand (Aotearoa)', 'OM = Oman', 'PA = Panama', 'PE = Peru', 'PG = Papua New Guinea', 'PH = Philippines', 'PK = Pakistan', 'PL = Poland', 'PM = Saint Pierre and Miquelon', 'CS = Serbia and Montenegro', 'PN = Pitcairn', 'PR = Puerto Rico', 'PS = Palestinian Territory', 'PT = Portugal', 'PW = Palau', 'PY = Paraguay', 'QA = Qatar', 'RE = Reunion', 'RO = Romania', 'RU = Russian Federation', 'RW = Rwanda', 'SA = Saudi Arabia', 'WS = Samoa', 'SH = Saint Helena', 'VC = Saint Vincent and the Grenadines', 'SM = San Marino', 'ST = Sao Tome and Principe', 'SN = Senegal', 'SC = Seychelles', 'SL = Sierra Leone', 'SG = Singapore', 'SK = Slovakia', 'SI = Slovenia', 'SB = Solomon Islands', 'SO = Somalia', 'ZA = South Africa', 'ES = Spain', 'SD = Sudan', 'SR = Suriname', 'SJ = Svalbard and Jan Mayen', 'SE = Sweden', 'CH = Switzerland', 'SY = Syria', 'SU = USSR (former)', 'SZ = Swaziland', 'TW = Taiwan', 'TZ = Tanzania', 'TJ = Tajikistan', 'TH = Thailand', 'TL = Timor-Leste', 'TG = Togo', 'TK = Tokelau', 'TO = Tonga', 'TT = Trinidad and Tobago', 'TN = Tunisia', 'TR = Turkey', 'TM = Turkmenistan', 'TC = Turks and Caicos Islands', 'TV = Tuvalu', 'UA = Ukraine', 'UG = Uganda', 'AE = United Arab Emirates', 'UK = United Kingdom', 'US = United States', 'UM = United States Minor Outlying Islands', 'UY = Uruguay', 'UZ = Uzbekistan', 'VU = Vanuatu', 'VA = Vatican City State', 'VE = Venezuela', 'VG = Virgin Islands (British)', 'VI = Virgin Islands (U.S.)', 'VN = Viet Nam', 'WF = Wallis and Futuna', 'EH = Western Sahara', 'YE = Yemen', 'YU = Yugoslavia (former)', 'ZM = Zambia', 'ZR = Zaire (former)', 'ZW = Zimbabwe']
    params = (
        ('request', 'getproxies'),
        ('proxytype', 'socks4'),
        ('timeout', '10000'),
        ('country', ccc),
    )
    response = requests.get('https://api.proxyscrape.com/', params=params)
    d1=response.text.encode('ascii','ignore').split()
    #d1=subprocess.check_output('curl -s "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country='+ccc+'"',shell=True).split()
    #lisst=[]
    random.shuffle(d1)
    for i in d1[:20]:
        try:
            a=os.popen('curl -L -s --connect-timeout 2 --socks4 '+i+' ip-api.com/json').read()
            if a:
                c=eval(a)['country']
                ip=eval(a)['query']
                cit_reg=eval(a)['city']+'_'+eval(a)['regionName']
                #lisst.append(i)
                out=[i,ip,cit_reg,c]
                break
        except:
            pass
    try:
        return out
    except:
        return ''

def socks_4cc(ccc=None):
    if not ccc:
        ccc='ALL'
    lis=['AF = Afghanistan', 'AL = Albania', 'DZ = Algeria', 'AX = Aland Islands', 'AS = American Samoa', 'AI = Anguilla', 'AD = Andorra', 'AO = Angola', 'AN = Antilles - Netherlands ', 'AG = Antigua and Barbuda', 'AQ = Antarctica', 'AR = Argentina', 'AM = Armenia', 'AU = Australia', 'AT = Austria', 'AW = Aruba', 'AZ = Azerbaijan', 'BA = Bosnia and Herzegovina', 'BB = Barbados', 'BD = Bangladesh', 'BE = Belgium', 'BF = Burkina Faso', 'BG = Bulgaria', 'BH = Bahrain', 'BI = Burundi', 'BJ = Benin', 'BM = Bermuda', 'BN = Brunei Darussalam', 'BO = Bolivia', 'BR = Brazil', 'BS = Bahamas', 'BT = Bhutan', 'BV = Bouvet Island', 'BW = Botswana', 'BV = Belarus', 'BZ = Belize', 'KH = Cambodia', 'CM = Cameroon', 'CA = Canada', 'CV = Cape Verde', 'CF = Central African Republic', 'TD = Chad', 'CL = Chile', 'CN = China', 'CX = Christmas Island', 'CC = Cocos (Keeling) Islands', 'CO = Colombia', 'CG = Congo', "CI = Cote D'Ivoire (Ivory Coast)", 'CK = Cook Islands', 'CR = Costa Rica', 'HR = Croatia (Hrvatska)', 'CU = Cuba', 'CY = Cyprus', 'CZ = Czech Republic', 'CD = Democratic Republic of the Congo', 'DJ = Djibouti', 'DK = Denmark', 'DM = Dominica', 'DO = Dominican Republic', 'EC = Ecuador', 'EG = Egypt', 'SV = El Salvador', 'TP = East Timor', 'EE = Estonia', 'GQ = Equatorial Guinea', 'ER = Eritrea', 'ET = Ethiopia', 'FI = Finland', 'FJ = Fiji', 'FK = Falkland Islands (Malvinas)', 'FM = Federated States of Micronesia', 'FO = Faroe Islands', 'FR = France', 'FX = France, Metropolitan', 'GF = French Guiana', 'PF = French Polynesia', 'GA = Gabon', 'GM = Gambia', 'DE = Germany', 'GH = Ghana', 'GI = Gibraltar', 'GB = Great Britain (UK)', 'GD = Grenada', 'GE = Georgia', 'GR = Greece', 'GL = Greenland', 'GN = Guinea', 'GP = Guadeloupe', 'GS = S. Georgia and S. Sandwich Islands', 'GT = Guatemala', 'GU = Guam', 'GW = Guinea-Bissau', 'GY = Guyana', 'HK = Hong Kong', 'HM = Heard Island and McDonald Islands', 'HN = Honduras', 'HT = Haiti', 'HU = Hungary', 'ID = Indonesia', 'IE = Ireland', 'IL = Israel', 'IN = India', 'IO = British Indian Ocean Territory', 'IQ = Iraq', 'IR = Iran', 'IT = Italy', 'JM = Jamaica', 'JO = Jordan', 'JP = Japan', 'KE = Kenya', 'KG = Kyrgyzstan', 'KI = Kiribati', 'KM = Comoros', 'KN = Saint Kitts and Nevis', 'KP = Korea (North)', 'KR = Korea (South)', 'KW = Kuwait', 'KY = Cayman Islands', 'KZ = Kazakhstan', 'LA = Laos', 'LB = Lebanon', 'LC = Saint Lucia', 'LI = Liechtenstein', 'LK = Sri Lanka', 'LR = Liberia', 'LS = Lesotho', 'LT = Lithuania', 'LU = Luxembourg', 'LV = Latvia', 'LY = Libya', 'MK = Macedonia', 'MO = Macao', 'MG = Madagascar', 'MY = Malaysia', 'ML = Mali', 'MW = Malawi', 'MR = Mauritania', 'MH = Marshall Islands', 'MQ = Martinique', 'MU = Mauritius', 'YT = Mayotte', 'MT = Malta', 'MX = Mexico', 'MA = Morocco', 'MC = Monaco', 'MD = Moldova', 'MN = Mongolia', 'MM = Myanmar', 'MP = Northern Mariana Islands', 'MS = Montserrat', 'MV = Maldives', 'MZ = Mozambique', 'NA = Namibia', 'NC = New Caledonia', 'NE = Niger', 'NF = Norfolk Island', 'NG = Nigeria', 'NI = Nicaragua', 'NL = Netherlands', 'NO = Norway', 'NP = Nepal', 'NR = Nauru', 'NU = Niue', 'NZ = New Zealand (Aotearoa)', 'OM = Oman', 'PA = Panama', 'PE = Peru', 'PG = Papua New Guinea', 'PH = Philippines', 'PK = Pakistan', 'PL = Poland', 'PM = Saint Pierre and Miquelon', 'CS = Serbia and Montenegro', 'PN = Pitcairn', 'PR = Puerto Rico', 'PS = Palestinian Territory', 'PT = Portugal', 'PW = Palau', 'PY = Paraguay', 'QA = Qatar', 'RE = Reunion', 'RO = Romania', 'RU = Russian Federation', 'RW = Rwanda', 'SA = Saudi Arabia', 'WS = Samoa', 'SH = Saint Helena', 'VC = Saint Vincent and the Grenadines', 'SM = San Marino', 'ST = Sao Tome and Principe', 'SN = Senegal', 'SC = Seychelles', 'SL = Sierra Leone', 'SG = Singapore', 'SK = Slovakia', 'SI = Slovenia', 'SB = Solomon Islands', 'SO = Somalia', 'ZA = South Africa', 'ES = Spain', 'SD = Sudan', 'SR = Suriname', 'SJ = Svalbard and Jan Mayen', 'SE = Sweden', 'CH = Switzerland', 'SY = Syria', 'SU = USSR (former)', 'SZ = Swaziland', 'TW = Taiwan', 'TZ = Tanzania', 'TJ = Tajikistan', 'TH = Thailand', 'TL = Timor-Leste', 'TG = Togo', 'TK = Tokelau', 'TO = Tonga', 'TT = Trinidad and Tobago', 'TN = Tunisia', 'TR = Turkey', 'TM = Turkmenistan', 'TC = Turks and Caicos Islands', 'TV = Tuvalu', 'UA = Ukraine', 'UG = Uganda', 'AE = United Arab Emirates', 'UK = United Kingdom', 'US = United States', 'UM = United States Minor Outlying Islands', 'UY = Uruguay', 'UZ = Uzbekistan', 'VU = Vanuatu', 'VA = Vatican City State', 'VE = Venezuela', 'VG = Virgin Islands (British)', 'VI = Virgin Islands (U.S.)', 'VN = Viet Nam', 'WF = Wallis and Futuna', 'EH = Western Sahara', 'YE = Yemen', 'YU = Yugoslavia (former)', 'ZM = Zambia', 'ZR = Zaire (former)', 'ZW = Zimbabwe']
    d1=subprocess.check_output('curl -s "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country='+ccc+'"',shell=True).split()
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --max-time 3 --socks4 '+i+' ip-api.com/json').read()
            if a:
                c=eval(a)['country']
                ip=eval(a)['query']
                cit_reg=eval(a)['city']+'_'+eval(a)['regionName']
                lisst.append(i)
                out=[i,ip,cit_reg,c]
                break
        except:
            pass
    try:
        return out
    except:
        return ''


def socks_5():
    d=subprocess.check_output('curl -s https://proxyscrape.com/free-proxy-list',shell=True)
    req4=re.findall('href="(.*?)" id="downloadiconsocks5',d)[0]
    the_files=urllib2.urlopen(req4).read()
    d1=the_files.split()
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --socks5 '+i+' --max-time 3 http://ipecho.net/plain').read()
            if a:
                lisst.append(i)
                break
        except:
            pass
        #print i
    return i

def clinetester(cline):
    for i in range(10):
        import random
        ho=random.randrange(5)
        cookies = {
            'cookielawinfo-checkbox-necessary': 'yes',
            'cookielawinfo-checkbox-non-necessary': 'yes',
            'bp-activity-oldestpage': '1',
            'PHPSESSID': 'eg9kmlbkuhkab6bs0oh57kkc4g',
            '__utma': '221372957.1189044888.1629478001.1629478001.1629478001.1',
            '__utmb': '221372957.1.10.1629478001',
            '__utmc': '221372957',
            '__utmz': '221372957.1629478001.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '__utmt': '1',
            '__gads': 'ID=f7f6b67a81d5aaca-22b8a422b0c900cb:T=1629478004:RT=1629478004:S=ALNI_MZLhQ1Y3ZjtYfqXqNsdBfL5qzwXCg',
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://testious.com',
            'Connection': 'keep-alive',
            'Referer': 'https://testious.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        
        data = {
          'line': cline,
          'captcha': str(ho)
        }
        
        r = requests.post('https://testious.com/tester/check.php', headers=headers, cookies=cookies, data=data)
        #print r.text
        if 'wrong captcha' not in r.text.lower():
            break
    if r.text[0]=='o':
        return True
    else:
        return False