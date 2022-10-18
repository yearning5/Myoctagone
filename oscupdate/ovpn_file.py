import requests,re,os

a=os.popen('rm -f /etc/openvpn/*.ovpn')
cookies = {
    'sid': '75F5FB8D9BC6',
    '__utma': '159920506.1940414539.1624550885.1624550885.1624550885.1',
    '__utmc': '159920506',
    '__utmz': '159920506.1624550885.1.1.utmcsr=google^|utmccn=(organic)^|utmcmd=organic^|utmctr=(not^%^20provided)',
    '__utmt': '1',
    '_ga': 'GA1.2.1940414539.1624550885',
    '_gid': 'GA1.2.1339668732.1624550886',
    '__utmb': '159920506.2.10.1624550885',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6',
}

response = requests.get('https://www.vpngate.net/en/', headers=headers, cookies=cookies).text

# get first

l1='https://www.vpngate.net/en/'+re.findall(r'href=.*?(do_openvpn.*?)>.*?OpenVPN<BR>Config file',response)[0].strip("'")

r2 = requests.get(l1, headers=headers, cookies=cookies).text

l2='https://www.vpngate.net'+re.findall(r'href="(.*?.ovpn)"',r2)[0].replace('amp;','')

l3=requests.get(l2)
with open('/etc/openvpn/01-opengw.net_udp_1195.ovpn', 'wb') as f:
    f.write(l3.content)

t1=re.findall(r'<tr>(.*?)</tr>',response,re.DOTALL)

lines=[]
for i ,s in enumerate(t1):
    if 'Config file' in s:
        lines.append(s)

links=[]
for i in lines:
    t2=re.findall(r'<td(.*?)</td>',i,re.DOTALL)
    country=t2[0].split('>')[-1]
    link='https://www.vpngate.net/en/'+re.findall('href=(.*?)>',t2[6])[0].replace('amp;','').strip("'")
    el=[country,link]
    links.append(el)
ii=1
for i in links:
    r2 = requests.get(i[1], headers=headers, cookies=cookies).text

    l2='https://www.vpngate.net'+re.findall(r'href="(.*?.ovpn)"',r2)[0].replace('amp;','')

    l3=requests.get(l2)
    with open('/etc/openvpn/'+str(ii)+'_'+i[0] +'_opengw.net_udp_1195.ovpn', 'wb') as f:
        f.write(l3.content)

    ii +=1
    if ii==20:
        break
