
import os
import requests
from urllib.request import  Request, urlopen
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
        a=response.text
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
        the_page =the_page
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
        the_page=requests.get(link,verify=False, timeout=5).text
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
        the_page = f.text
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
        the_page =the_page
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

        the_page = f.data.decode('utf-8')
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
        f = http.request('GET',link,headers=UserAgent)
        the_page =f.data.decode('utf-8')
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
        data = urlopen(link,timeout=5)
        the_page=data.read()
        Host=re.findall(b'[host:C]: (.*?)[<: ]', the_page,re.DOTALL)[0].decode('utf-8')
        Port=re.findall(b'port: (.*?)[<: ]', the_page,re.DOTALL)[0].decode('utf-8')
        User=re.findall(b'user: (.*?)[<: ]', the_page,re.DOTALL)[0].decode('utf-8')
        Pass=re.findall(b'pass: (.*?)[<: ]', the_page,re.DOTALL)[0].decode('utf-8')
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
        the_page = f.text
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
        the_page = f.text
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
        the_page = f.text
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
    aaa=requests.get('https://hidemy.name/en/proxy-list/?type=4&end=256#list',headers={"User-Agent":"Mozilla/5.0"}).text
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
            a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=3).text
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
    d1=response.text.split()
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
    the_files=urlopen(req4).read()
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


# ======    Message on screen =========================================================================

message_script=os.system('wget -O /dev/null -q "http://localhost/web/message?text= \nOscupdate script by GUIRA is Running ......&type=2&timeout=6"')

#======================================================================================================

stt=open('/tmp/oscupdate_status.txt','w')
#activation servsat
try:
    try:
        acct=subprocess.check_output('curl -s --max-time 10 "http://www.serversat.net/cccam.php" --data "author=anaana"', shell=True)
    except:
        ecct=os.popen('curl -s --max-time 10 "http://www.serversat.net/cccam.php" --data "author=anaana"')
    print ('done serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print ('pass serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
#print "servsat updated"
#activation servsat MGCAMD
try:
    try:
        acct=subprocess.check_output('curl -s --max-time 10 "http://www.serversat.net/mgcamd.php" --data "author=anaana"', shell=True)
    except:
        acct=os.popen('curl -s --max-time 10 "http://www.serversat.net/mgcamd.php" --data "author=anaana"')
    print ('done MG serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done MG serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except  Exception as e:
    print ('pass serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

#print "servsat MG updated"

# Journalsat mgcamd
try:    
    uuser= str(random.randrange(1, 10**9))
    
    cookies = {
        '_ga': 'GA1.2.1444096135.1619435351',
        '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
        '_gid': 'GA1.2.112354009.1625736097',
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736098969],null,null]',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://cccam.journalsat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://cccam.journalsat.com/index.php',
        'Upgrade-Insecure-Requests': '1',
    }
    
    r1 = requests.post('http://cccam.journalsat.com/index.php', headers=headers, cookies=cookies)
    
    
    cookies = {
        '_ga': 'GA1.2.1444096135.1619435351',
        '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
        '_gid': 'GA1.2.112354009.1625736097',
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736098969],null,null]',
        'uername': uuser,
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://cccam.journalsat.com/index.php',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    r2 = requests.get('http://cccam.journalsat.com/get.php', headers=headers, cookies=cookies)
    
    cookies = {
        '_ga': 'GA1.2.1444096135.1619435351',
        '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
        '_gid': 'GA1.2.112354009.1625736097',
        'uername': uuser,
        'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736388648],null,null]',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://cccam.journalsat.com',
        'Connection': 'keep-alive',
        'Referer': 'http://cccam.journalsat.com/get.php',
        'Upgrade-Insecure-Requests': '1',
    }
    
    params = (
        ('do', 'mgcam'),
    )
    
    data = {
      'do': 'mgcam',
      'dgam': 'generate'
    }
    
    r3 = requests.post('http://cccam.journalsat.com/get.php', headers=headers, params=params, cookies=cookies, data=data)
    
    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.post('http://cccam.journalsat.com/get.php?do=mgcam', headers=headers, cookies=cookies, data=data)
    a=re.findall('N:(.*?)<',r3.text)[0].split()
    with open(source,'r') as f: ff=f.readlines()
    for i ,s in enumerate(ff):
        if 'MG-journalsat' in s:
            break
    if len(a)!=18:
        a=['err','err','err','err']
    ff[i+3]='device                        = '+a[0]+','+a[1]+'\n'
    ff[i+5]='user                          = '+a[2]+'\n'
    ff[i+6]='password                      = '+a[3]+'\n'
    fd= open(source,'w')
    for  i in ff:
        fd.write(i)
    fd.close()
    print ('done MG Journalsat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done MG Journalsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass Journalsat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write('pass Journalsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass
#activation algsat mgcamd
'''
try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    try:
        a11=subprocess.check_output('curl -s -m 5 --cookie-jar - "http://algsat.ddns.net/" --data-raw "Username='+user+'&Username='+user+'&addf1="', shell=True)
        coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
        b=subprocess.check_output('curl -s -m 5 "http://algsat.ddns.net/mgcamd.php" -H "Cookie: PHPSESSID='+coki+'" --data-raw "Username='+user+'&Username='+user+'&addf1="', shell=True)
    except:
        a11=os.popen('curl -s -m 5 --cookie-jar - "http://algsat.ddns.net/" --data-raw "Username='+user+'&Username='+user+'&addf1="').read()
        coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
        b=os.popen('curl -s -m 5 "http://algsat.ddns.net/mgcamd.php" -H "Cookie: PHPSESSID='+coki+'" --data-raw "Username='+user+'&Username='+user+'&addf1="').read()
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
    print 'done  algsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done  algsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass algsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass algsat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
#print "algsat MG updated"

# kcccam
'''
try:
    ip = os.popen('curl -s http://ipecho.net/plain').readlines(-1)[0].strip()
    try:
        a=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" --data "protocol=mgcam&server=f3.kcccam.com&vehicle1=agree"', shell=True)
        a1=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" -H "cookie: already='+ip+'"&', shell=True)
        b=a1
    except:
        a=os.popen('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" --data "protocol=mgcam&server=f3.kcccam.com&vehicle1=agree"')
        a1=os.popen('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" -H "cookie: already='+ip+'"&').read()
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
    print 'done Kccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done Kccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass kccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass kccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
#cccamcard.com

'''
try:
    ip = os.popen('curl -s -L --max-time 3 http://ipecho.net/plain').read().strip()
    try:
        a=subprocess.check_output('curl -s -m 5 "https://cccamcard.com/free-cccam-server.php" --data-raw "protocol=mgcam&server=f3.cccamcard.com&vehicle1=agree"',shell=True)
        a1=subprocess.check_output('curl -s -m 5 "https://cccamcard.com/free-cccam-server.php" -H "cookie: TawkConnectionTime=0; already='+ip+'"',shell=True)
        b=a1
    except:
        a=os.popen('curl -s -m 5 "https://cccamcard.com/free-cccam-server.php" --data-raw "protocol=mgcam&server=f3.cccamcard.com&vehicle1=agree"')
        a1=os.popen('curl -s -m 5 "https://cccamcard.com/free-cccam-server.php" -H "cookie: TawkConnectionTime=0; already='+ip+'"').read()
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
            if all(x in read[i] for x in ['label','MG_cccamcard']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+5]='user                          = '+user+'\n'
                read[i+6]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print 'done cccamcard '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done cccamcard '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass ccamcard '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass ccamcard '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
#print "algsat MG2 updated"

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
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print ('done khaled Mg2 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done khaled Mg2 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass khaled Mg2 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write('pass khaled Mg2 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
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
                break
        ffii=open(source,'w')
        for i in read1:
            ffii.write(i)
        ffii.close()
    print ('done khaled Mg1 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done khaled Mg1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except  Exception as e:
    print ('pass khaled Mg1 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass khaled Mg1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass
#print "infosat MG1 updated"



#   OSN
'''
try:
    #user='85469512'
    user=''.join(random.choice(string.digits) for _ in range(8))
    #cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="'
    #d=open('/tmp/excution.txt','w')
    #d.close()
    socc=socks_4()
    #print 'saqr1',socc
    try:
        b=subprocess.check_output('curl -L -s --max-time 10 --socks4 '+socc[0]+' "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="',shell=True)
    except:
        b=os.popen('curl -L -s --max-time 10 --socks4 '+socc[0]+' "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="').read()
    #b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #print 'saqr',socc
    d=open('/tmp/excution.txt','w')
    d.write('the socks used for saqr is: '+socc[0]+' from '+socc[2]+' '+socc[3]+' \n')
    d.close()
    host= re.findall('host.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    port= re.findall('port.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    Pass= re.findall('pass.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    a=[host,port,user,Pass]
    #print a
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','saqr_Mgcam']):
                read[i+5]='user                          = '+user+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print 'done sqr '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done sqr '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass sqr '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass sqr '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
#topservercccam
'''
try:
    #user='85469512'
    user=''.join(random.choice(string.digits) for _ in range(5))
    #cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="'
    bb=socks_4()
    #print 'speeds1',bb
    try:
        a=subprocess.check_output('curl -s -L --max-time 15 --socks4 '+bb[0]+' "https://free.speeds.tv/mgcamd/index.php"  --data-raw "user='+user+'&pass=topservercccam"',shell=True)
    except:
        a=os.popen('curl -s -L --max-time 15 --socks4 '+bb[0]+' "https://free.speeds.tv/mgcamd/index.php"  --data-raw "user='+user+'&pass=topservercccam"').read()
    #b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #print 'speeds',bb
    d=open('/tmp/excution.txt','a')
    d.write('the socks used for topservercccam is: '+bb[0]+' from '+bb[2]+' '+bb[3]+' \n')
    d.close()
    if 'already have a line' in a:
        host= 'free.speeds.tv'
        port= '52114'
        Pass= 'topservercccam'
        a2=[host,port,user,Pass]
    else:
        host= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[0]
        port= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[1]
        Pass= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[3]
        a3=[host,port,user,Pass]
    #print a
    if all(i!='' for i in a2):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','MG_free.speeds']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print 'done speeds '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done speeds '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass speeds '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass speeds '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass

'''
'''
try:
    #user='85469512'
    user=''.join(random.choice(string.digits) for _ in range(5))
    #cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="'
    bb=socks_4()
    #print 'speeds1',bb
    try:
        a=subprocess.check_output('curl -s -L --max-time 15 --socks4 '+bb[0]+' "https://free.speeds.tv/cccam/"  --data-raw "user='+user+'&pass=topservercccam"',shell=True)
    except:
        a=os.popen('curl -s -L --max-time 15 --socks4 '+bb[0]+' "https://free.speeds.tv/cccam/"  --data-raw "user='+user+'&pass=topservercccam"').read()
    #b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #print 'speeds',bb
    d=open('/tmp/excution.txt','a')
    d.write('the socks used for topservercccam is: '+bb[0]+' from '+bb[2]+' '+bb[3]+' \n')
    d.close()
    if 'already have a line' in a:
        host= 'free.speeds.tv'
        port= '52115'
        Pass= 'topservercccam'
        a2=[host,port,user,Pass]
    else:
        host= re.findall('c: (.*?)<',a,re.IGNORECASE)[0].split(' ')[0]
        port= re.findall('c: (.*?)<',a,re.IGNORECASE)[0].split(' ')[1]
        Pass= re.findall('c: (.*?)<',a,re.IGNORECASE)[0].split(' ')[3]
        a3=[host,port,user,Pass]
    #print a
    if all(i!='' for i in a2):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','C_free.speeds.tv']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+3]='user                          = '+user+'\n'
                read[i+4]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print 'done speeds cccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done speeds cccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass speeds cccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass speeds cccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
# urliptv
'''
try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    try:
        b=subprocess.check_output('curl -s --max-time 5 "https://urliptv.com/CCcam/" --data "Username='+user+'&cline="', shell=True)
    except:
        b=subprocess.check_output('curl -s --max-time 5 "https://urliptv.com/CCcam/" --data "Username='+user+'&cline="').reaad()
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
    print 'done urliptv '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done urliptv '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass urliptv '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass urliptv '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
# firecccam
'''
try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    maill=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))+'@gmail.com'
    cmd='curl -s -m 5 "https://firecccam.com/mgcamd.php" --data-raw "Username='+user+'&Password='+user+'&Email='+maill+'&addf="'
    #cmd1='curl -s --max-time 5 "http://firecccam.com/mgcamd02.php"  --data "Username='+user+'&Password='+user+'&Email='+user+'@yahoo.com^&addf="'
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    try:
        ho=re.findall('n: (.*?)<',b,re.IGNORECASE)[1].split()
    except:
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
    print 'done Fireccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done Fireccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass Fireccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass Fireccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
try:
    '''cmd='curl -s -m 5 "https://www.realcccam.com/index.php" --data-raw "addf=addf"'
    try:
        a1=subprocess.check_output(cmd, shell=True)
    except:
        a1=os.popen(cmd).read()
    ho=re.findall('c: (.*?)[<:\n]',a1,re.IGNORECASE)[0].split(' ')
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]'''
    data = {
      'addf': 'addf'
    }

    response = requests.post('https://realcccam.com/freecccam/index.php', data=data).text

    host=re.findall(r'server.*?:(.*?)<',response,re.IGNORECASE)[0].strip()
    port=re.findall(r'port.*?:(.*?)<',response,re.IGNORECASE)[0].strip()
    user=re.findall(r'user.*?:(.*?)<',response,re.IGNORECASE)[0].strip()
    Pass=re.findall(r'pass.*?:(.*?)<',response,re.IGNORECASE)[0].strip()
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','realcccam']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+3]='user                          = '+user+'\n'
                read[i+4]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print ('done realcccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+user+Pass)
    stt.write(    'done realcccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('done realcccam '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done realcccam '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

servers1=[]
servers2=[]
my_servers=[]
try:
    try:
        aa=subprocess.check_output('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/server2/index.php"', shell=True)
    except:
        aa=os.popen('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/server2/index.php"  --data-raw "user=azazaza&pass=satunivers.net&secret="%"3C"%"3F+echo+"%"24secret"%"3B+"%"3F"%"3E"').read()
    mhost=re.findall('host:(.*?)<',aa)[0].strip()
    mport=re.findall('port:(.*?)<',aa)[0].strip()
    muser=re.findall('user:(.*?)<',aa)[0].strip()
    mpass=re.findall('pass:(.*?)\n',aa)[0].strip()
    a=[mhost,mport,muser,mpass,'khaled_cccam2']
    if all(i!='' for i in a):
        my_servers.append(a)
    print ('done khaled cccam 2 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done khaled cccam 2 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass khaled cccam 2'+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass khaled cccam 2'+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

try:
    try:
        aa=subprocess.check_output('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/index1.php"', shell=True)
    except:
        aa=os.popen('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/index1.php"').read()
    mhost=re.findall('host:(.*?)<',aa)[0].strip()
    mport=re.findall('port:(.*?)<',aa)[0].strip()
    muser=re.findall('user:(.*?)<',aa)[0].strip()
    mpass=re.findall('pass:(.*?)\n',aa)[0].strip()
    a=[mhost,mport,muser,mpass,'khaled_cccam1']
    if all(i!='' for i in a):
        my_servers.append(a)
    print ('done khaled cccam 1 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done khaled cccam 1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass khaled cccam 1'+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass khaled cccam 1'+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass
#print "infosat cccam updated"
try:
    r=requests.get('http://dream4evertwo.info/index.php?pages/D4E/',headers=UserAgent).text
    hosts=re.findall(r'host:(.*?)</span>',r,re.IGNORECASE)
    ports=re.findall(r'port:(.*?)</span>',r,re.IGNORECASE)
    users=re.findall(r'user:(.*?)</span>',r,re.IGNORECASE)
    psses=re.findall(r'pass:(.*?)</span>',r,re.IGNORECASE)
    hot1=[]
    for i in hosts:
        hot1.append(i.split('>')[-1].strip().strip('&nbsp;'))
    port1=[]
    for i in ports:
        port1.append(i.split('>')[-1].strip().strip('&nbsp;'))
    user1=[]
    for i in users:
        user1.append(i.split('>')[-1].strip().strip('&nbsp;'))
    pas1=[]
    for i in psses:
        pas1.append(i.split('>')[-1].strip().strip('&nbsp;'))
    for i in range(4):
        host= hot1[i]
        port= port1[i]
        user= user1[i]
        Pass= pas1[i]
        nm='My_'+host[:15]+'_'+str(i)
        a=[host,port,user,Pass,nm]
        if all(i!='' for i in a):
            oscalm=[host,port,user,Pass,nm]
            my_servers.append(oscalm)
        print ('done dream4evertwo '+'_'+str(i)+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
        stt.write(        'done dream4evertwo '+'_'+str(i)+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass dream4evertwo '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass dream4evertwo '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

# skyhd
'''
try:
    #print 'start socks'
    aa=socks_4c()
    #print aa
    try:
        ab=os.popen('curl -L -s --socks4 '+aa[0]+' --max-time 6 http://skyhd.xyz/freetest/test1.php').read()
        ho=re.findall('C: (.*?)<',ab)[0].split()
    except:
        cmd='curl -L -s --socks4 '+aa[0]+' --max-time 6 http://skyhd.xyz/freetest/test1.php'
        ab=subprocess.check_output(cmd, shell=True)
        ho=re.findall('C: (.*?)<',ab)[0].split()

    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    nm='My_'+host[:15]
    a=[host,port,user,Pass,nm]
    if all(i!='' for i in a):
        skyhd1=[host,port,user,Pass,nm]
        my_servers.append(skyhd1)
        #print 'added to my-servers'
    print 'done skyhd1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done skyhd1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass skyhd1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass skyhd1 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
# linux24

try:
    user=''.join(random.choice(string.ascii_lowercase +string.digits) for _ in range(8))
    cmd='curl -s -m 5 "http://test.linux24.tk/test/" --data-raw "Username='+user+'&cline="'
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    ho=re.findall('C: (.*?)<',b,re.DOTALL)[0].strip('\n').split(' ')
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    nm='My_'+host[:15]
    a=[host,port,user,Pass,nm]
    if all(i!='' for i in a):
        linux24=[host,port,user,Pass,nm]
        my_servers.append(linux24)
        #print 'added to my-servers'
    print ('done linux24 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done linux24 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass linux24 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass linux24 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass


try:
    try:
        a1=requests.get('http://www.masrawysat.com/vb/showthread.php?t=3067398',headers=UserAgent,timeout=5).text
    except:
        a1=requests.get('http://www.masrawysat.com/vb/showthread.php?t=3067398',headers=UserAgent,timeout=5).text
    if '<a class="smallfont" href="' in a1:
        lstpage='http://www.masrawysat.com/vb/'+''.join(re.findall('<a class="smallfont" href="(.*?)s=.*?;(.*?)"',a1)[-1]).replace('&amp;','&')
        f = requests.get(lstpage,headers=UserAgent,timeout=5)
        a2=f.text
    else:
        a2=a1
    if len(re.findall('host.*?:(.*?)[":<:\n]',a2,re.IGNORECASE))>1:
        #host=re.findall('host.*?:(.*?)[":<:\n]',a2,re.IGNORECASE)[-2].strip()
        host='storesat.tk'
        #port=re.findall('port.*?:(.*?)[":<:\n]',a2,re.IGNORECASE)[-1].strip()
        port='23000'
        #user=re.findall('user.*?:(.*?)[":<:\n]',a2,re.IGNORECASE)[-2].strip()
        user='storesat'
        try:
            Pass=re.findall('Pass.*?:(.*?)[":<:\n]',a2)[-2].strip()
        except:
            a2=os.popen('curl -s "https://arabdayz.com/%d8%b3%d9%8a%d8%b1%d9%81%d8%b1-%d8%b3%d9%8a%d8%b3%d9%83%d8%a7%d9%85-cccam-%d9%85%d9%86-%d8%b3%d8%aa%d8%a7%d9%84%d8%a7%d9%8a%d8%aa-%d8%b3%d8%aa%d9%88%d8%b1-%d8%a8%d8%a7%d9%84%d9%85%d8%ac%d8%a7%d9%86/%d8%a3%d8%ae%d8%a8%d8%a7%d8%b1-%d8%b3%d8%a7%d8%aa%d9%84%d8%a7%d9%8a%d8%aa/"').read()
            Pass=re.findall('Pass.*?:(.*?)[":<:\n]',a2)[-2].strip()
        nm='My_Masr.storesat'
        a=[host,port,user,Pass,nm]
    else:
        a=['err','err','','err']
    if all(i!='' for i in a):
        masr=[host,port,user,Pass,nm]
        my_servers.append(masr)
        #print 'added to my-servers'
    print ('done masrawysat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done masrawysat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass masrawysat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass masrawysat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass
'''
try:
    bb=socks_4()
    #print 'My_cccamsupreme1'+bb
    try:
        a=subprocess.check_output('curl -L -s  --max-time 10 --socks4 '+bb[0]+' https://cccamsupreme.com/cccamfree/get.php',shell=True)
    except:
        a=os.popen('curl -L -s  --max-time 10 --socks4 '+bb[0]+' https://cccamsupreme.com/cccamfree/get.php').read()
    #re.findall('c |c: (.*?)[<:\n]',a,re.IGNORECASE)[0].split()
    host=re.findall('c |c: (.*?)[<:\n]',a,re.IGNORECASE)[0].split()[0]
    port=re.findall('c |c: (.*?)[<:\n]',a,re.IGNORECASE)[0].split()[1]
    user=re.findall('c |c: (.*?)[<:\n]',a,re.IGNORECASE)[0].split()[2]
    Pass=re.findall('c |c: (.*?)[<:\n]',a,re.IGNORECASE)[0].split()[3]
    nm='My_cccamsupreme'
    #print nm
    a=[host,port,user,Pass,nm]
    if all(i!='' for i in a):
        masr1=[host,port,user,Pass,nm]
        my_servers.append(masr1)
        #print 'added to my-servers'
    print 'done cccamsupreme '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done cccamsupreme '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass cccamsupreme '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass cccamsupreme '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
# cccambtc
'''
try:
    cmd=('curl -s -L -m 5 "'+'https://cccambtc.com/'+'"')
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    l1=re.findall(r'headline.*?href="(.*?)"',b)[0]
    l2=re.findall(r'headline.*?href="(.*?)"',b)[1]
    nm=getPage(l1)
    nm[4]='My_'+nm[4]
    my_servers.append(nm)
    nm=getPage(l2)
    nm[4]='My_'+nm[4]
    my_servers.append(nm)
    print 'done cccambtc '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done cccambtc '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass cccambtc '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass cccambtc '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass
'''
# cccamx

try:
    cmd=('curl -s -L -m 5 "'+'https://cccamx.com/free-cccam.php'+'"')
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    nm=[]
    nm.append(re.findall(r'host:(.*?)<strong>',b,re.IGNORECASE)[0].split('>')[-1].strip())
    nm.append(re.findall(r'port:(.*?)<strong>',b,re.IGNORECASE)[0].split('>')[-1].strip())
    nm.append(re.findall(r'user:(.*?)<strong>',b,re.IGNORECASE)[0].split('>')[-1].strip())
    nm.append(re.findall(r'pass:.*?<(.*?)<',b,re.IGNORECASE)[0].split('>')[-1].strip())
    nm.append('My_'+nm[0])
    my_servers.append(nm)
    print ('done cccamx '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done cccamx '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass cccamx '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass cccamx '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

# tvlivepro

try:
    b=requests.get('https://www.tvlivepro.com/free_cccam_48h/', headers=UserAgent,verify=False)
    b=b.text
    nm=[]
    nm.append(re.findall(r'host.*?<th>(.*?)</th>',b,re.IGNORECASE)[0].strip())
    nm.append(re.findall(r'port.*?<th>(.*?)</th>',b,re.IGNORECASE)[0].strip())
    nm.append(re.findall(r'user.*?<th>(.*?)</th>',b,re.IGNORECASE)[0].strip())
    nm.append(re.findall(r'passw.*?<th>(.*?)</th>',b,re.IGNORECASE)[0].strip())
    nm.append('My_'+nm[0])
    my_servers.append(nm)
    print ('done tvlivepro '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done tvlivepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass tvlivepro '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass tvlivepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

#cccamtiger

try:
    cmd=('curl -s -L -m 10 "'+'https://cccamtiger.com/fcccam/'+'"')
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    nm=[]
    nm.append(re.findall(r'Host  </th><th>(.*?)<',b,re.IGNORECASE)[0])
    nm.append(re.findall(r'Port  </th><th>(.*?)<',b,re.IGNORECASE)[0])
    nm.append(re.findall(r'User  </th><th>(.*?)<',b,re.IGNORECASE)[0])
    nm.append(re.findall(r'Password  </th><th>(.*?)<',b,re.IGNORECASE)[0])
    nm.append('My_'+nm[0])
    my_servers.append(nm)
    print ('done cccamtiger '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done cccamtiger '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass cccamtiger '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass cccamtiger '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass


# vipcccam.xyz

try:
    user=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    data = {
      'username': user,
      'password': user,
      'access': 'Rizwan'
    }
    r= requests.post('http://vipcccam.xyz/test/gen.php', headers=UserAgent, data=data, verify=False)
    a=r.text.split('\n')
    for i in a:
        if user in i:
            break
    h=i.split('<')[0].split()
    nm=[]
    nm.append(h[0])
    nm.append(h[1])
    nm.append(h[2])
    nm.append(h[3])
    nm.append('My_'+nm[0])
    if all(i!='' for i in h):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if 'My_'+nm[0] in read[i]:
                read[i+2]='device                        = '+nm[0] +','+nm[1] +'\n'
                read[i+3]='user                          = '+nm[2] +'\n'
                read[i+4]='password                      = '+nm[3] +'\n'
                print (user)
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
    print ('done vipcccam.xyz '+str(lineno())+' '+str(datetime.datetime.now()-now1))
except Exception as e:
    print ('pass vipcccam.xyz '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    print ('The error exception is :  '+str(e))
    pass

if os.path.isfile('/oscupdate/my-servers.txt'):
    the_file=open('/oscupdate/my-servers.txt','r')
    the_links =the_file.readlines()
    the_file.close()


# ===               

try:
    lastname="0"+''.join(random.choice(string.digits) for _ in range(9))
    vowels = 'aeiou'
    consonants = 'bcdfghijklmnpqrstvwxz'
    firstname=string.capitalize(random.choice(consonants))+random.choice(vowels)+random.choice(consonants)+random.choice(vowels)+random.choice(consonants)
    email=firstname+'_' +str(random.randint(11,99)) +'@yahoo.com'
    satmood=random.choice(('7700','8000','9000'))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://drsharing.com',
        'Connection': 'keep-alive',
        'Referer': 'http://drsharing.com/box/usertestnew.php',
        'Upgrade-Insecure-Requests': '1',
    }    
    data = {
      'firstname': firstname,
      'lastname': lastname,
      'email': email,
      'satmood': 'ALLSAT',
      'port': satmood,
      'usercn': 'usercccam',
      'submit': '\u062D\u0641\u0638 \u0628\u064A\u0646\u0627\u062A \u0627\u0644\u062A\u0633\u062C\u064A\u0644'
    }
    response = requests.post('http://drsharing.com/box/usertestnew.php', headers=headers, data=data,verify=False)
    aa= response.text
    ho1=re.findall('domain .*?>(.*?)<',aa,re.IGNORECASE)[0].strip()
    ho2=re.findall('port.*?>(.*?)<',aa,re.IGNORECASE)[0].strip()
    ho3=re.findall('user n.*?>(.*?)<',aa,re.IGNORECASE)[0].strip()
    ho4=re.findall('password.*?>(.*?)<',aa,re.IGNORECASE)[0].strip()
    nm=[]
    nm.append(ho1)
    nm.append(ho2)
    nm.append(ho3)
    nm.append(ho4)
    nm.append('My_drsharing')
    my_servers.append(nm)
    print ('done drsharing '+str(lineno())+' '+str(datetime.datetime.now()-now1))
except Exception as e:
    print ('pass drsharing '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    print ('The error exception is :  '+str(e))
    pass
# ccamtiger

for i in range(len(the_links)):
    serv=getPage(the_links[i])
    serv[4]='My_'+serv[4]
    #print i
    my_servers.append(serv)
    strrrr=the_links[i].replace('https://www.','').replace('http://www.','').replace('https://','').replace('http://','').split('.')[0]
    print ("appended "+ serv[4]+'  '+strrrr+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    "appended "+ serv[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')

# 62.171.144.145
try:
    lin='https://testious.com/?s=C%3A+62.171.144.145'
    f = requests.get(lin,headers=UserAgent,timeout=5)
    b = f.text
    ho=re.findall('[C:c]: (62.171.144.145) (.*?) (.*?) (.*?)[<: :\n:\t]', b)
    def innt(n):
        try:
            b=int(n)
            return True
        except:
            return False
    for i in ho:
        if innt(i[1]):
            hoo=i
            break
    host= hoo[0]
    port= hoo[1]
    user= hoo[2]
    Pass= hoo[3]
    nm='My_Danhill'
    a=[host,port,user,Pass,nm]
    if all(i!='' for i in a):
        mboss=[host,port,user,Pass,nm]
        my_servers.append(mboss)
        #print 'added to my-servers'
    print ('done My_Danhill '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'done My_Danhill '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass My_Danhill '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass My_Danhill '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass

# iconepro
'''try:
    lin='https://testious.com/?s=C%3A+iconepro.me'
    f = requests.get(lin,headers=UserAgent,timeout=5)
    b = f.text
    ho=re.findall('[C:c]: (iconepro.me) (.*?) (.*?) (.*?)[<: :\n:\t]', b)
    def innt(n):
        try:
            b=int(n)
            return True
        except:
            return False
    hoo=[]
    for i in ho:
        if innt(i[1]):
            hoo.append(i)
    from CCcamTester import TestCline
    for i in hoo:
        s='C: '+i[0]+' '+i[1]+' '+i[2]+' '+i[3]
        if TestCline(s)==True:
            break
    host= i[0]
    port= i[1]
    user= i[2]
    Pass= i[3]
    nm='My_Iconepro'
    a=[host,port,user,Pass,nm]
    if all(i!='' for i in a):
        mboss=[host,port,user,Pass,nm]
        my_servers.append(mboss)
        #print 'added to my-servers'
    print 'done iconepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'done iconepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    print 'pass iconepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'pass iconepro '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    pass '''


#print "my-servers.txt updated"

if os.path.isfile('/oscupdate/dreamosat.txt'):
    the_file=open('/oscupdate/dreamosat.txt','r')
    the_links =the_file.readlines()
    the_file.close()

for i in range(len(the_links)):
    serv=getPage4(the_links[i])
    serv[4]='Osat_'+serv[4][:-4]
    servers1.append(serv)
    print ('appended '+serv[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'appended '+serv[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')

#print "dreamosat updated"
#clines Najmsatcamd

if os.path.isfile('/oscupdate/clines.txt'):
    the_fil=open('/oscupdate/clines.txt','r')
    the_clins =the_fil.readlines()
    the_fil.close()
#anaj0=ccamfree(the_clins[0],'Najm')
#anaj1=ccamfree(the_clins[1],'free_ccam')
#anaj2=ccamfree(the_clins[2],'Flylinks')
anaj3=ccamfree(the_clins[0],'Cccam2')
anaj4=ccamfree(the_clins[1],'Cccam7')
anaj5=ccamfree(the_clins[2],'Cccam3')
anaj=anaj3+anaj4+anaj5#+anaj0+anaj1+anaj2
cliness=f8(anaj)
cliness=f8(cliness)
clina=[]
for i in cliness:
    if 'fcnoip' not in i[0]:
        clina.append(i)

for i in range(len(clina)):
    servers2.append(clina[i])
    print ('appended '+clina[i][4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'appended '+clina[i][4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')

#print "najmsat updated"

#========================================================
#====                NLINES                            ======
#========================================================
'''
nl0=nlinefree(the_clins[0],'Najm')
nl1=nlinefree(the_clins[1],'free_ccam')
nl2=nlinefree(the_clins[2],'Flylinks')
nl=nl0+nl1+nl2
ness=f8(nl)

ncamd=[]

for line in ness:
    ncamd.append(line)
    print 'appended '+line[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    stt.write(    'appended '+line[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
#print "nlines updated" 
'''

'''
# --------------------------------------------------------
# cccam-live.com
# --------------------------------------------------------

try:
    link='http://www.cccam-live.com/'
    f = requests.get(link,headers=UserAgent,timeout=5)
    the_page = f.text
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
'''
if os.path.isfile('/oscupdate/allcccam.txt'):
        the_fil=open('/oscupdate/allcccam.txt','r')
        the_lins =the_fil.readlines()
        the_fil.close()
'''
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
    the_page =the_page
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
    lx2 = lx2.text
    lux=lux+re.findall('href="(.*?)">Free CCcam<',lx2)[0]
    lx1=requests.get(lux,headers=UserAgent,timeout=5)
    lx1 = lx1.text
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
khaledsat[4]='Khal_'+khaledsat[4][:-5]
req1 ='http://server.satunivers.tv/server2/'
khaled1=ifosat(req1)
khaled1[4]='Khal_'+khaled1[4][:-5]
try:
    try:
        acct=subprocess.check_output('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/free2.php"  --data-raw "user=ghaza&pass=www.satunivers.net&secret=^%^3C^%^3F+echo+^%^24secret^%^3B+^%^3F^%^3E"', shell=True)
    except:
        acct=os.popen('curl -s --max-time 10 "http://infosat.satunivers.tv/cgn/free2.php"  --data-raw "user=ghaza&pass=www.satunivers.net&secret=^%^3C^%^3F+echo+^%^24secret^%^3B+^%^3F^%^3E"').read()
    ho=re.findall(b'c: (.*?)<',acct,re.IGNORECASE)[0].split()

    if len(ho)>1:
        a=[ho[0],ho[1],ho[2],'www.satunivers.net','My_'+ho[0][:15]]
    else:
        a=['err','err','','err']
    if all(i!='' for i in a):
        kh=a
        my_servers.append(kh)
    print ('appended '+'My_'+ho[0][:15]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'appended '+'My_'+ho[0][:15]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except Exception as e:
    print ('pass append serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass append serversat '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass
#my_servers.append(khaled1)
my_servers.append(khaledsat)
print ('appended '+khaledsat[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('appended '+khaledsat[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
req4 ='http://s1.satunivers.tv/download1.php?file=srtx4.txt'
try:
    the_files=urlopen(req4).read()
    ssr1=re.findall(b'host:(.*?)\n',the_files)[0].decode('utf-8').strip()
    ssr2=re.findall(b'port:(.*?)\n',the_files)[0].decode('utf-8').strip()
    ssr3=re.findall(b'user:(.*?)\n',the_files)[0].decode('utf-8').strip()
    ssr4=re.findall(b'pass:(.*?)\n',the_files)[0].decode('utf-8').strip()
    ssr=[ssr1,ssr2,ssr3,ssr4]
except:
    Host="error"
    Port="error"
    User="error"
    Pass="error"
    nm='error'
    ssr=[[Host, Port, User, Pass,nm]]
ssr[4]='Khal_'+ssr[4][:-5]
my_servers.append(ssr)
print ('appended '+ssr[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('appended '+ssr[4]+' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
#print "infosat servers updated"
# ================================= freeclines + testious =================================
try:
    linktest1='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()).strftime('%Y-%m-%d')
    linktest2='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()-datetime.timedelta(1)).strftime('%Y-%m-%d')

    if requests.get(linktest1,headers=UserAgent,timeout=5).status_code==200:
        link3=linktest1
    elif requests.get(linktest2,headers=UserAgent,timeout=5).status_code==200:
        link3=linktest2
    else:
        link3='http://www.testious.com/free-cccam-servers/'+(datetime.datetime.today()-datetime.timedelta(2)).strftime('%Y-%m-%d')
    testious=ccamfree(link3,'Testious')
    #ntestious=nlinefree(link3,'Testious')
    #for lne in ntestious:
    #    ncamd.append(lne)
    #    print 'appended '+lne[4] +' '+str(lineno())+' '+str(datetime.datetime.now()-now1)
    #    stt.write(        'appended '+lne[4] +' '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    nm='error'
    testious=[[Host, Port, User, Pass,nm]]
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
    the_page=f.text
    a1=re.findall('(c: .*?)status_icon_online',the_page,re.DOTALL|re.IGNORECASE)
    a2=[re.findall('c: (.*?)<',i,re.DOTALL|re.IGNORECASE)[-1] for i in a1]
    a2=[i.split(' ') for i in a2]
    a3=[]
    for i in a2:
        i.append('Freecline_'+i[0][:9])
        a3.append(i)

    freecline=f8(a3)
    if freecline==[]:
        freecline=[['error','error','error','error','error','error']]
    # free N-lines
    the_pagea=ff.text
    aa1=re.findall('(n: .*?)status_icon_online',the_pagea,re.DOTALL|re.IGNORECASE)
    aa2=[re.findall('n: (.*?)<',i,re.DOTALL|re.IGNORECASE)[-1] for i in aa1]
    aaa2=[[i.split()[0],i.split()[1],i.split()[2],i.split()[3],'Freecline_'+i.split()[0][:9]] for i in aa2]
    #bcd=[bb[0].split('_') for bb in bd if bb !=[]] or [['err'],['err'],['err'],['err']]
    #bbc=[]
    #for i in bcd:
        #bbc.append([i[0],i[1],i[2],i[3]])
    freeN=f8(aaa2)
    if freeN==[]:
        freeN=[['error','error','error','error','error']]

    for lnee in freeN:
        ncamd.append(lnee)
except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    nm='error'
    freecline=[[Host, Port, User, Pass,nm]]

try:
    f = requests.get('https://www.cccam3.com/free-mgcamd-server/',headers=UserAgent,timeout=5)
    the_page=f.text
    ccam3=re.findall(r'CWS =.*?>(.*?)<.*?>(.*?)<.*?>(.*?)<.*?>(.*?)<',the_page,re.IGNORECASE)
    try:
        at1 = int(ccam3[-1][2].strip(' ')[-2:])-13
        at1=ccam3[-1][2].strip(' ')[:-2] + str(at1)
    except:
        at1=ccam3[-1][2].strip(' ')
    cccam3=[ccam3[-1][0].strip(' '),ccam3[-1][1].strip(' '),at1,ccam3[-1][3].strip(' '),'Cccam3_'+ccam3[-1][0].strip(' ')[:10]]
    ncamd.append(cccam3)
except Exception as e:
    print ('pass cccam3 '+str(lineno())+' '+str(datetime.datetime.now()-now1))
    stt.write(    'pass cccam3 '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
    print ('The error exception is :  '+str(e))
    pass


## 4cardsharing
try:
    card='http://www.4cardsharing.net'
    linkk4=card.strip('\r\n')
    fff4 = requests.get(linkk4,headers=UserAgent,timeout=5)#,proxies=proxiess)
    pag4 = fff4.text
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
    fff4 = ccamfree(linkk4,'4cardsh')
    card4sh=f8(fff4)
    if card4sh==[]:
        card4sh=[['error','error','error','error','error']]

except:
    Host='error'
    Port='error'
    User='error'
    Pass='error'
    nm='error'
    card4sh=[[Host, Port, User, Pass,nm]]

# cccam.date
amdat='http://cccam.date'
dat=ccamfree(amdat,'CcamDat')
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
    fcnoip12=[['error','error','error','error','error']]

for n in fcnoip12:
    servers2.append(n)
ghg=freecline+testious
ghg=f8(ghg)
for nj in ghg:
    servers2.append(nj)
servers2=f8(servers2)
print ('appended servers2 line '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('appended servers2 line '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
#print "testious freecline and dat updated"

serverss=[]
for lline in (servers1+servers2):
    if len(lline)==5:
        serverss.append(lline)
servers=f8(serverss)
allservers=[]
for i in servers:
    if not 'cardserver' in i[0].lower():
        allservers.append(i)
servers=f8(allservers)
print ('appended all servers line '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('appended all servers line '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
#print "all servers sorted and filtred"

#print "duckdns updated"


my_servers1=[]
for i in my_servers:
    if not any( x in i[0] for x in ['err' ,'s2.6g']):
        my_servers1.append(i)

#import socket
test101=[]
for i in my_servers1:
    try:
        a=socket.gethostbyname(i[0])
        print ('my_servers IP conversion '+str(lineno())+' '+str(datetime.datetime.now()-now1))
        stt.write('my_servers IP conversion '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
        i[0]=a
        test101.append(i)
    except:
        pass
my_servers1=f8(test101)
my_servers=my_servers1

print ('convert to IP my_servers  '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('convert to IP my_servers  '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
"""newservers=[]
for new in servers:
    if not 'err' in new[0] and not '51.38.48.10' in new[0] :
        newservers.append(new)"""
#import socket
test1=[]
for i in servers:
    try:
        a=socket.gethostbyname(i[0])
        print ('servers IP conversion '+str(lineno())+' '+str(datetime.datetime.now()-now1))
        stt.write('servers IP conversion '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
        i[0]=a
        test1.append(i)
    except:
        pass
servers=f8(test1)

with open('/tmp/names_servers.txt','w') as ff:
    for nn in servers:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')
print (' a_servers.txt writen '+str(lineno())+' '+str(datetime.datetime.now()-now1))
print ('convert to IP servers '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('convert to IP servers '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
servers=[i for i in servers if not any(i[0]  in j for j in my_servers)]

drop1=['topservercccam','alkaicer','serversat','generator3','freeiptv4u','dzpros-forum']
servers=[i for i in servers if not any(j in i[3]  for j in drop1)]
drop2=['egygold','.egy']
servers=[i for i in servers if not any(j in i[4]  for j in drop2)]
servers=servers
#drop=['168.119.10.42','95.217.83.239','95.216.224.34','173.249.43.66','164.68.102.81','95.216.229.60','147.135.169.166','49.12.126.182','5.189.132.43','37.48.90.76','178.157.91.151','37.187.161.201','144.91.110.37','217.182.16.96','80.211.57.154','err','speeds','51.38.48.10','178.128.200.245','54.38.5.104','207.180.233.72','95.217.216.41']
drop=['95.217.192.171','168.119.208.240','207.180.211.167','194.163.149.241']
servers=[i for i in servers if not any(j in i[0]  for j in drop)]
drop3=['s1.eg','s2.eg','s3.eg','s4.eg','s5.eg','s6.eg',]
servers=[i for i in servers if not any(j in i[4]  for j in drop3)]
#pass drop

my_servers=[i for i in my_servers if not any(j in i[0]  for j in drop)]
#drop1=[]

#print "remover err from servers"


#====================================================
with open('/tmp/a_servers.txt','w') as ff:
    for nn in servers:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')
print (' a_servers.txt writen '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write(' a_servers.txt writen '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')
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
    if len(lline)==5:
        serverssm.append(lline)
serversm=f8(serverssm)

print ('finish filter serversm '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('finish filter serversm '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')

with open('/tmp/a_serversm.txt','w') as ff:
    for nn in serversm:
        s='C: '+nn[0]+' '+nn[1]+' '+nn[2]+' '+nn[3]
        ff.write(s+'\n')
print ('finish append serversm to a_servers '+str(lineno())+' '+str(datetime.datetime.now()-now1))
stt.write('finish append serversm to a_servers '+str(lineno())+' '+str(datetime.datetime.now()-now1)+'\n')

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

if len(the_page)>479:
    the_pag=open(source,'w')
    i=0
    while i <479:
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
'''try:
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
    url="http://cccam.freeiptv4u.com/jkggd5gcgg/"
    try:
        r = s.post(url,data=parames)
    except:
        pass
 except:
    pass
'''
#print "freeiptv4u updated"
'''
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
'''
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
now12=datetime.datetime.now()
diffe12nce =now12 - now1
print (' start writing  oscam.server after '+str(diffe12nce)+' line: '+str(lineno()))
stt.write(' start writing  oscam.server after '+str(diffe12nce)+' line: 1974 '+'\n')
the_pag=open(source,'r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open(source,'a')
        #mecccam

servers=my_servers+servers
'''clinetess=[]
for io in servers:
    llpp='C: '+' '.join(io[:4])
    if clinetester(llpp):
        print 'clinetess appended'+llpp
        clinetess.append(io)
servers=clinetess'''
with open('/tmp/allservers.txt','w') as f:
    for nkb in servers:
        f.write(' '.join(nkb)+'\n')

'''
print 'start test cccam'
aiaia= datetime.datetime.now()

testt=[]
for testtt in servers:
    if testccam('C: '+' '.join(testtt[:-1])):
        testt.append(testtt)

servers=testt

print 'End test cccam'
print datetime.datetime.now()-aiaia

'''
jn=0
for j in servers:
    jn=jn+1
    try:
        host=j[0]
        port=j[1]
        user=j[2]
        pasw=j[3]
        #exxcept_art=['135.181.78.48','88.99.91.253','5.189.161.183','195.154.200.18','135.181.136.120','95.216.112.104','62.171.129.84','49.12.129.210','168.119.39.46','85.203.33.242','62.171.181.10','95.217.192.171','62.171.131.113','164.132.53.24','5.189.134.13','207.180.206.80','54.38.5.104','178.238.236.25','176.31.156.44','213.136.94.35','167.86.119.185','185.22.173.58','5.135.75.42','5.189.156.56','178.238.232.233','116.202.196.126','178.128.200.245','51.77.220.127','37.59.80.83','94.130.220.50','94.130.199.50','144.91.117.213','178.63.69.157']
        #exxcept_moviestar=['164.132.53.24','62.171.131.113','49.12.129.210','185.22.173.58','5.189.161.183','173.249.17.127']
        #exxcept_skyde=['185.22.173.58']
        #================= print duplicates in list  =================
        #================= stt.write(        #================= duplicates in list  =================+'\n')
        # [x for n, x in enumerate(z) if x in z[:n]]
        #==============================================================
        #exxcept_thor=['185.22.173.58','213.32.93.193']
        #exxcept_osn=['135.181.78.48','151.80.62.94','135.181.134.21','88.99.91.253','95.217.192.171','49.12.129.204','80.211.8.149','168.119.38.151','168.119.10.43','49.12.129.205','49.12.129.202','95.217.200.25','49.12.129.210','5.189.161.183','135.181.78.47','168.119.39.46','136.243.129.249','49.12.129.203']
        #exxcept_tnt=['54.38.93.53','168.119.39.46','164.132.53.24','144.91.115.78','135.181.136.120','94.176.232.235','173.212.234.202','168.119.10.43','78.46.68.145','95.217.192.171','62.171.181.141','95.111.247.147','144.91.81.136','144.91.121.8','62.171.140.28','173.249.13.170']

        #exxcept_art=['95.217.200.25:8801','195.154.200.18:8403','147.135.169.166:13000','5.9.116.12,33000']
        exxcept_art=['5.135.75.42', '135.181.136.120', '116.202.196.126', '185.22.173.58', '94.130.220.50', '144.91.117.213', '62.171.131.113', '95.217.192.171', \
        '5.189.161.183', '195.154.200.18', '94.130.199.50', '95.216.112.104', '37.59.80.83', '85.203.33.242', '62.171.181.10', '167.86.119.185', '178.63.69.157', \
        '178.238.236.25', '5.189.156.56', '168.119.39.46', '51.77.220.127', '207.180.206.80', '135.181.78.48', '164.132.53.24', '178.238.232.233', '176.31.156.44', \
        '213.136.94.35', '54.38.5.104', '95.217.200.25', '88.99.91.253', '147.135.169.166', '5.9.116.12', '178.128.200.245', '62.171.129.84', '49.12.129.210', \
        '5.189.134.13','54.38.5.111','54.36.151.64','161.97.76.252','95.111.247.212','80.211.103.106','168.119.10.42','168.119.208.201','51.91.153.76', \
        '136.243.129.249','168.119.208.199','135.181.78.47','168.119.208.198','51.210.47.128','144.76.62.176','144.76.105.169','173.249.13.170','144.91.114.11', \
        '95.111.245.239','46.20.36.27','168.119.208.202','5.196.123.106','167.86.108.31','5.189.163.8','161.97.170.138','51.159.52.147']
        #exxcept_moviestar=['51.91.252.58:14511','147.135.169.166:13000','5.189.161.183:50000','161.97.76.252:14404','144.91.124.239:5200','94.23.97.10,22000', \
        #'161.97.76.252,13303','46.105.114.36,26500','178.238.232.233,25008','94.140.115.124,23000','51.75.71.151,10800','80.211.180.50,13065', \
        #'195.154.200.18,8403']
        exxcept_moviestar=['46.105.114.36', '94.140.115.124', '147.135.169.166', '164.132.53.24', '178.238.232.233', '195.154.200.18', '62.171.131.113', '51.91.252.58', \
        '173.249.17.127', '49.12.129.210', '80.211.180.50', '144.91.124.239', '5.189.161.183', '51.75.71.151', '161.97.76.252', '94.23.97.10', \
        '185.22.173.58','51.15.4.152','54.38.5.111','80.211.66.85','136.243.129.249','168.119.10.43','135.181.78.47','5.196.123.106','5.189.156.56', \
        '80.211.103.106','54.38.5.104','144.76.176.103','144.76.196.145','213.239.217.67','148.251.49.142','51.91.72.232','176.9.206.161','79.143.181.22', \
        '62.171.138.97','94.130.104.94','173.249.33.183','173.249.53.163','92.222.120.170','171.22.25.143','163.172.24.13','88.99.91.253','51.159.52.147', \
        '5.189.178.94','80.209.228.204','51.79.71.166','157.90.183.170','80.211.114.138','168.119.124.87','62.171.187.48','5.189.134.72' ,'167.86.80.103', \
        '95.111.231.165']
        #exxcept_skyde=['147.135.169.166,13000']
        exxcept_skyde=['147.135.169.166','185.22.173.58','54.38.5.111','5.189.161.183','80.211.66.85','136.243.129.249','195.154.200.18','51.210.47.128', \
        '173.249.43.66','145.239.150.86','89.207.129.33','167.86.80.103','173.212.254.248','168.119.10.43','51.75.71.151','135.181.78.47','144.76.62.176', \
        '213.239.207.195','144.91.117.36','168.119.38.151','5.196.123.106','207.180.238.178','95.217.192.171','137.74.64.168','80.209.226.116','62.171.138.183', \
        '167.86.108.31','95.111.231.165']
        #exxcept_thor=['161.97.76.252,14404','147.135.169.166,13000','37.187.161.201,1003','94.23.97.10,24000','51.91.252.58,14511','49.12.126.182,11000', \
        #'5.189.161.183,50000','161.97.76.252,13303']
        exxcept_thor=['147.135.169.166', '51.91.252.58', '37.187.161.201', '49.12.126.182', '5.189.161.183', '213.32.93.193', '161.97.76.252', '94.23.97.10', \
        '185.22.173.58','195.154.200.18','54.38.5.111','62.171.184.85','51.89.40.86','217.117.29.123','91.205.174.17','173.249.44.114','144.91.117.36', \
        ]
        #exxcept_osn=['95.217.200.25:8800','95.217.192.171:8801','49.12.129.210:8800','49.12.129.210:8801','168.119.39.46:18803','136.243.129.249:8802', \
        #'168.119.10.43:8807','168.119.10.42:18804','168.119.10.42:8800','95.217.200.25:8801','95.217.200.25:8806','49.12.129.210:8803','49.12.126.182:51002', \
        #'49.12.126.182:20001','147.135.169.166,13000','198.251.72.43,52000','5.189.161.183,50000','5.189.151.151,19000','91.205.174.17,13000', \
        #]
        exxcept_osn=['5.189.151.151', '95.217.200.25', '5.189.161.183', '135.181.134.21', '91.205.174.17', '95.217.192.171', '49.12.129.203', '49.12.129.202', \
        '49.12.129.205', '49.12.129.204', '168.119.39.46', '135.181.78.48', '135.181.78.47', '151.80.62.94', '80.211.8.149', '136.243.129.249', '88.99.91.253', \
        '147.135.169.166', '198.251.72.43', '49.12.129.210', '49.12.126.182', '168.119.38.151', '168.119.10.42', '168.119.10.43']
        #exxcept_tnt=['168.119.39.46,18801','147.135.169.166,13000','161.97.76.252,14404','136.243.129.249,8803','135.181.136.35,8801','5.189.156.56,13000', \
        #'95.217.200.25,8800','49.12.129.210,18806','135.181.136.35,8800','168.119.10.42,18806','135.181.78.47,18801','135.181.78.47,8800','135.181.78.47,18802', \
        #'95.217.192.171,8803','135.181.78.47,18803','49.12.129.202,18803','136.243.129.249,8800','95.217.192.171,8801','173.212.234.202,65000','168.119.10.43,8803', \
        #'5.189.156.56,13200','178.238.232.233,25008','135.181.136.35,8803','135.181.136.35,8802','207.180.238.178,13008','135.181.78.48,18803', \
        #'135.181.78.47,8801','135.181.78.47,8802','135.181.78.47,8803','135.181.78.47,8804','135.181.78.47,8805','49.12.126.182,20001','80.211.180.50,13065', \
        #'95.217.83.239,51006','5.189.163.8,18100','148.251.235.104,35000','49.12.129.210,8804','49.12.126.182,51001','49.12.129.210,8805','135.181.78.48,8802', \
        #'54.38.93.53,27808','62.171.131.113,2021','95.217.200.25,8806','168.119.39.46,18804','49.12.129.210,8803','95.217.192.171,8800','168.119.10.43,8807', \
        #'135.181.134.21,18801','49.12.126.182,51002','168.119.38.151,8801','168.119.208.199,18803','95.217.83.239,15001','168.119.10.42,18801','148.251.49.142,31000', \
        #'49.12.129.202,8802']
        exxcept_tnt=['144.91.121.8', '173.212.234.202', '135.181.136.120', '95.217.83.239', '62.171.181.141', '148.251.235.104', '54.38.93.53', '168.119.208.199', '62.171.131.113', \
        '95.217.192.171', '62.171.140.28', '135.181.134.21', '207.180.238.178', '173.249.13.170', '135.181.136.35', '95.111.247.147', '144.91.115.78', '49.12.129.202', \
        '5.189.163.8', '161.97.76.252', '5.189.156.56', '168.119.39.46', '78.46.68.145', '135.181.78.48', '164.132.53.24', '135.181.78.47', '178.238.232.233', '148.251.49.142', \
        '94.176.232.235', '80.211.180.50', '95.217.200.25', '136.243.129.249', '147.135.169.166', '49.12.129.210', '49.12.126.182', '144.91.81.136', '168.119.38.151', '168.119.10.42', \
        '168.119.10.43','54.38.5.111','168.119.208.240','62.171.129.84','168.119.208.198','173.212.254.248','137.74.4.134','190.2.148.36','144.91.117.36','95.216.112.104', \
        '188.40.71.184','51.77.140.248','168.119.208.202','185.22.173.58','5.9.116.12','173.249.43.66','173.249.56.124','88.99.91.253','196.117.60.126', '54.37.74.42', \
        '164.68.116.254','190.2.152.21','95.111.231.165','78.47.33.170','190.2.155.98','213.136.86.212','109.104.158.139','168.119.208.203','5.9.30.34', \
        '94.130.161.203','95.216.9.165','161.97.145.32','173.249.48.167','207.180.195.166','168.119.208.237','173.249.47.215','157.90.183.170','85.203.33.242', \
        '173.249.12.28','135.181.18.121','207.180.227.213','94.130.104.94','65.21.130.105','5.189.178.94','207.180.211.167','185.197.249.102']
        #exxcept_syfra=['195.154.200.18,8403','95.217.200.25,8803']
        exxcept_syfra=['195.154.200.18','95.217.200.25','161.97.76.252','80.211.180.50','54.38.5.111','95.217.83+.239','80.211.66.85','185.22.173.58', \
                       '212.8.252.43','80.208.229.118','178.238.232','163.172.24.13','190.2.148.36','207.180.227.213','178.238.232.233','190.2.155.99', \
                           '194.163.178.97']
        exxcept_polsat=['207.180.233.131',"207.180.238.178",'5.196.123.106','144.91.117.36','95.111.245.239','80.211.180.50','51.158.112.115','194.99.21.190', \
        '137.74.64.168']
        jj=j[4]
        def aawrt(jn,jj,host,port,user,pasw):
            art=''
            mov=''
            sk=''
            thr=''
            osn=''
            tnt=''
            syfra=''
            polsat=''
            if any(host in i for i in exxcept_art):
               art='!ART'
            if any(host in i  for i in exxcept_moviestar):
               mov='!moviestar'
            if any(host in i for i in exxcept_skyde):
               sk='!sky_ger'
            if any(host in i for i in exxcept_thor):
                thr='!thor'
            if any(host in i for i in exxcept_osn):
                osn='!osn'
            if any(host in i for i in exxcept_tnt):
                tnt='!tnt'
            if any(host in i for i in exxcept_syfra):
                syfra='!syfra'
            if any(host in i for i in exxcept_polsat):
                polsat='!polsat'

            sers=[art,mov,sk,thr,osn,tnt,syfra,polsat]
            if any(x=='' for x in sers) and not all(x=='' for x in sers): 
                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+jj + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = '+','.join(i for i in sers if i!='')+'\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            elif  all(x=='' for x in sers):
                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+jj + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            elif all(x!='' for x in [art,mov,sk,thr,tnt]):
                print (jj ,' blocked')
                stt.write(                jj ,' blocked'+'\n')
                wrte=''
            elif len([ i for i in sers if i!=''])>=4:
                print( jj ,' blocked')
                stt.write(                jj ,' blocked'+'\n')
                wrte=''
            else:
                print (jj ,' blocked')
                stt.write(                jj ,' blocked'+'\n')
                wrte=''
            return wrte

        '''if any(host in i for i in exxcept_art):
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            if any(host in i for i in exxcept_moviestar):
                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART,!moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        elif any(host in i for i in exxcept_moviestar):
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            if any(host in i for i in exxcept_art):
                 wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART,!moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        else:
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        #the_pag.write(wrte)'''
        aawrt1=aawrt(jn,jj,host,port,user,pasw)
        if  aawrt1!='':
            the_pag.write(aawrt1)
    except IndexError:
        pass
the_pag.close()

'''
ncamd1=[]
for i in ncamd:
    if len(i)==5:
        ncamd1.append(i)
drop=['err','speeds','algsat','saqr','kcccam','firecccam','satunivers','serversat','masrawysat.expresstun']
#drop=[]
ncamd1=[i for i in ncamd1 if not any(j in i[0]  for j in drop)]
ncamd=f8(ncamd1)
try:
    #lin='https://www.google.com/search?rlz=1C1AVFC_enTD866TD866&sxsrf=ALeKk00Uv4oOkMLit4cUJTGnqaRvTS5rlg%3A1586723680804&ei=YHuTXpPLMMWLlwTpgIOgBA&q=satkeys.biz+mgcamd&oq=satkeys.biz'
    #f=requests.get(lin,headers=UserAgent,timeout=3.0,verify=False)
    #the_page = f.text
    #a=re.findall('href="(https://satkeys.biz/index.*?)"',the_page)[0]
    a='https://satkeys.biz/index.php?topic=93755.0'
    f=requests.get(a,headers=UserAgent,timeout=5.0,verify=False)
    b = f.text
    ho=re.findall('CWS(.*?)<',b,re.IGNORECASE)
    ser=[]
    for i in ho:
        ii=i.split()
        ser.append([ii[1].replace(' ',''),ii[2].replace(' ',''),ii[3].replace(' ',''),ii[4].replace(' ',''),'Satkeys'+ii[1].replace(' ','')[:8]])
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


t_pag.close() '''
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
print (difference)


# print message of termination
# stt.write(# message of termination+'\n')
difference=str(difference).rsplit('.',1)[0].split(':')
difference=difference[0]+' hr '+difference[1]+' min and '+difference[2]+' sec'
message_script2=os.system('wget -O /dev/null -q "http://localhost/web/message?text= \nOscupdate script by GUIRA is updated in ......\n'+'\n'+difference+'&type=2&timeout=15"')
