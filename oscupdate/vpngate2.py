from bs4 import BeautifulSoup
import requests, re , os ,urllib

url='https://www.vpngate.net/en/'
page = requests.get(url)

page1=page.text.encode('ascii', 'ignore')
links=re.findall(r'(do_openvpn.aspx.*?)>',page1,re.DOTALL)
links=['https://www.vpngate.net/en/'+i.strip("'") for i in links]
con=re.findall(r'/><br>(.*?)do_openvpn.aspx.*?/tr>',page1,re.DOTALL)
cons=[i.split('<')[0] for i in con]

list1=[[cons[i],links[i]] for i in range(min(len(links),len(cons)))]
nojapan=[i for i in list1 if  'japan' not in i[0].lower() and 'korea' not in i[0].lower() ]

# ovpn
'''ovpnl=[]
for link in nojapan:
    page = requests.get(link[1]).text.encode('ascii', 'ignore')
    ll=[]
    for i in page.split('\n'):
        if '.ovpn"' in i:
            ii='https://www.vpngate.net'+re.findall('href="(.*?)"',i)[0].replace('amp;','')
            ll.append(ii)
    ovpnl +=ll



if os.path.isdir('/tmp/vpngate'):
    f=os.popen('rm -r /tmp/vpngate')
    f=os.popen('mkdir /tmp/vpngate')
else:
    f=os.popen('mkdir /tmp/vpngate')
for i in ovpnl:
    name=i.split('/')[-1]
    urllib.urlretrieve(i, ('/tmp/vpngate/'+name))'''
ovpnl1=[]
for link in nojapan:
    page = requests.get(link[1]).text.encode('ascii', 'ignore')
    ll=[]
    for i in page.split('\n'):
        if '.ovpn"' in i:
            ii='https://www.vpngate.net'+re.findall('href="(.*?)"',i)[0].replace('amp;','')
            iii=[link[0],ii]
            ll.append(iii)
    ovpnl1 +=ll



if os.path.isdir('/tmp/vpngate'):
    f=os.popen('rm -r /tmp/vpngate')
    f=os.popen('mkdir /tmp/vpngate')
else:
    f=os.popen('mkdir /tmp/vpngate')
for i in ovpnl1:
    name=i[0]+'_'+i[1].split('/')[-1]
    urllib.urlretrieve(i[1], ('/tmp/vpngate/'+name))

