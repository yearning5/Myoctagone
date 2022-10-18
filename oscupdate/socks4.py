# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:24:25 2022

@author: HERE
"""
import requests, random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup
cookies = {
    '_ga': 'GA1.2.1593945600.1647617149',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    # 'Cookie': '_ga=GA1.2.1593945600.1647617149',
}

r = requests.get('https://www.socks-proxy.net/', headers=headers, cookies=cookies).text
soup = BeautifulSoup(r, 'html.parser')
table = soup.find_all('table', attrs={'class':'layui-table'})
table = soup.find_all('tbody')
table=max(table,key=len)
rows = table.find_all('tr')

data4=[]

for row in rows:
    #if 'td' in str(row):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) >4:
        data4.append(cols)
        
d4=[i[0]+':'+i[1] for i in data4]
d14=[]
for o in d4:
    if o not in d14:
        d14.append(o)
d4=d14

def socksss4(): 
    random.shuffle(d4)
    try:
        
        for i in d4:
            try:
                proxies = {'http': "socks4://"+i}
                a=requests.get('http://ip-api.com/json', proxies=proxies,timeout=3,verify=False).text
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