#!/bin/bash

MYSTRING="Getting Free Socks5 proxy"
echo $MYSTRING

python - << EOF
import requests, random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

data = []

for n in range(10):
    
    try:
        
        params = {
            'type': 'socks5',
            'anonymity': '',
            'country': '',
            'speed': '1000',
            'port': '',
            'page': str(n+1),
        }
        
        r = requests.get('https://www.freeproxy.world/', params=params, headers=headers).content
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find_all('table', attrs={'class':'layui-table'})
        table = soup.find_all('tbody')
        table=max(table,key=len)
        rows = table.find_all('tr')
        
        for row in rows:
            #if 'td' in str(row):
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if len(cols) >4:
                data.append(cols)
    except:
        pass

d1=[i[0]+':'+i[1] for i in data]
d11=[]
for o in d1:
    if o not in d11:
        d11.append(o)
d1=d11

def socksss5(): 
    random.shuffle(d1)
    try:
        
        for i in d1:
            try:
                proxies = {'http': "socks5h://"+i}
                a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=5,verify=False).text
                if a:
                    c=eval(a)['country']
                    ip=eval(a)['query']
                    portt=i.split(':')[1]
                    cit_reg=eval(a)['city']+'_'+eval(a)['regionName']
                    #lisst.append(i)
                    out=[i,ip,portt,cit_reg,c]
                    break
            except:
                pass
    except:
        out=''

    return out
	
print (socksss5())

EOF

echo "Back to bash"