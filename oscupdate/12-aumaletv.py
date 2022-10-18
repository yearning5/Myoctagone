import requests,re
from datetime import datetime
try:
        
    a_session = requests.Session()
    a_session.get('https://aumaletv.com/update.php')
    session_cookies = a_session.cookies
    cookies_dictionary = session_cookies.get_dict()
    
    
    
    cookies = {
        '__gads': 'ID=9860f329e43195a1-2254746963c90076:T=1625487045:RT=1625487045:S=ALNI_MZCZn_2CgjqHnlmXx4tCM8HBXEQfQ',
        '__tawkuuid': 'e::aumaletv.com::Z4FGbjGgoPN8bPQ35Znppd1ATL0SWGRNdF2edM8YNPA3toXdnKb+qms7soKk3r8h::2',
        'PHPSESSID': cookies_dictionary['PHPSESSID'],
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://aumaletv.com',
        'Connection': 'keep-alive',
        'Referer': 'https://aumaletv.com/update.php',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    
    data = {
      'username': 'yearning55',
      'password': 'yearning55',
      'update_user': ''
    }
    
    r = requests.post('https://aumaletv.com/update.php', headers=headers, cookies=cookies, data=data).text.encode('ascii','ignore')
    #link=re.findall('url=(.*?)"',r)[0]
    #print link
    
    
    cookies = {
        '__gads': 'ID=9860f329e43195a1-2254746963c90076:T=1625487045:RT=1625487045:S=ALNI_MZCZn_2CgjqHnlmXx4tCM8HBXEQfQ',
        '__tawkuuid': 'e::aumaletv.com::Z4FGbjGgoPN8bPQ35Znppd1ATL0SWGRNdF2edM8YNPA3toXdnKb+qms7soKk3r8h::2',
        'PHPSESSID': cookies_dictionary['PHPSESSID'],
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }
    
    
    r1 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
    
    r2 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
        
    try:
        da=re.findall('id="expired_date".*?value=(.*?)>',r2)[0].split('"')[1]
        da=float(da)
        expp=datetime.fromtimestamp(float(da)).strftime('%d-%m-%Y @ %H:%M:%S')
        with open('/tmp/aumaletv_expr.txt','w') as f:
            f.write('Aumaletv successufly run and updated\n it will expire on\n'+expp)
        print 'Aumaletv successufly run and updated\n it will expire on\n'+expp
        with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','r') as f:
            ff=f.readlines()
        fff=ff[1].split(':')[-3].strip()+':'+ff[1].split(':')[-2]+':'+ff[1].split(':')[-1].split(' ')[0]
        ff[1]=ff[1].replace(fff,expp)
        fff1=ff[2].split(':')[-3].strip()+':'+ff[2].split(':')[-2]+':'+ff[2].split(':')[-1].split(' ')[0]
        ff[2]=ff[2].replace(fff1,expp)
        
        with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','w') as f:
            for i in ff:
                f.write(i)
        
    except:
        with open('/tmp/aumaletv_expr.txt','w') as f:
            f.write('Aumaletv FAILED to run ')
        print 'Aumaletv FAILED to run '
except:
    with open('/tmp/aumaletv_expr.txt','w') as f:
        f.write('Aumaletv FAILED to run ')
    print 'Aumaletv FAILED to run '
        

