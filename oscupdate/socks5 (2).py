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

def clinetest(cline):
    cline=cline.strip('C: ')
    num=str(random.randint(11,99))
    #print num
    cookies = {
        'key': num,
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://clinetest.net',
        'Alt-Used': 'clinetest.net',
        'Connection': 'keep-alive',
        'Referer': 'https://clinetest.net/',
        # 'Cookie': 'key=77',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    
    data = {
        'gidecek': cline,
        'cevap': num,
    }
    
    response = requests.post('https://clinetest.net/cam.php', cookies=cookies, headers=headers, data=data,timeout=10)
    #print response.content
    if 'green' in response.content:
        return True
    else:
        return False
    


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

data4=[]

for n in range(10):
    
    try:
        
        params = {
            'type': 'socks4',
            'anonymity': '',
            'country': '',
            'speed': '1000',
            'port': '',
            'page': str(n+1),
        }
        
        r = requests.get('https://www.freeproxy.world/', headers=headers, params=params, cookies=cookies).text
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
                data4.append(cols)
    except:
        pass

d4=[i[0]+':'+i[1] for i in data4]
d14=[]
for o in d4:
    if o not in d14:
        d14.append(o)
d4=d14


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
    random.shuffle(d4)
    try:
        
        for i in d4:
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

print (socksss5())