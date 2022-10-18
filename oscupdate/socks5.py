
import requests, random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
}

params = {
    'type': 'socks5',
    'anonymity': '',
    'country': '',
    'speed': '1000',
}


r=requests.get('https://www.freeproxy.world/', headers=headers, params=params).text

soup = BeautifulSoup(r, 'html.parser')
table = soup.find_all('table', attrs={'class':'layui-table'})
table = soup.find_all('tbody')
table=max(table,key=len)
rows = table.find_all('tr')

data = []
for row in rows:
    #if 'td' in str(row):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) >4:
        data.append(cols)
        
d1=[i[0]+':'+i[1] for i in data]    


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

def socksss4(): 
    random.shuffle(d1)
    try:
        
        for i in d1:
            try:
                proxies = {'http': "socks4://"+i}
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