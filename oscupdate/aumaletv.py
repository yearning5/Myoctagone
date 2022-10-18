import requests,re , random , string, os
from datetime import datetime

USERR=''.join((random.choice(string.ascii_letters+string.digits) for x in range(10)))

a_session = requests.Session()
a_session.get('https://aumaletv.com/')
session_cookies = a_session.cookies
cookies_dictionary = session_cookies.get_dict()

try:
    if os.path.exists('/etc/enigma2/userbouquet.aumaletv__tv_.tv'):
        with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','r') as f:
            ff=f.readlines()
        for i in ff:
            if 'SERVICE' in i and 'http' in i:
                break
        existusr=i.split('/')[-3]
    
        cookies = {
            'PHPSESSID':  cookies_dictionary['PHPSESSID'],
            '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
            'TawkConnectionTime': '0',
            '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://aumaletv.com',
            'Connection': 'keep-alive',
            'Referer': 'https://aumaletv.com/login.php',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }
        
        data = {
          'login_username': existusr,
          'login_password': existusr,
          'login': ''
        }
        
        r1 = requests.post('https://aumaletv.com/login.php', headers=headers, cookies=cookies, data=data).text
        
        subdate=re.findall('Subscription date.*?>(.*?)<',r1,re.DOTALL)
        print ('Existing User is = '+existusr+'\n')
        print("Subscription date : " +subdate[0]+'\n')
        expdate=re.findall('Expiring date.*?>(.*?)<',r1,re.DOTALL)
        print("Expiring date : " +expdate[0]+'\n')
        
        if datetime.now().strftime("%Y-%m-%d %H:%M:"+expdate[0].split(':')[-1])>=expdate[0]:
            print('\n\nsubscription expired\n\n')
            print('New user is =  '+USERR)
            cookies = {
                'PHPSESSID':  cookies_dictionary['PHPSESSID'],
                '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
                'TawkConnectionTime': '0',
                '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
            }
    
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://aumaletv.com',
                'Connection': 'keep-alive',
                'Referer': 'https://aumaletv.com/create.php',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
    
            data = {
              'name': USERR,
              'pass': USERR,
              'bouquet': '[1,2,44,31,9,22,8,16,18,19,10,6,4,12,7,13,24]',
              'create_user': ''
            }
    
            response = requests.post('https://aumaletv.com/create.php', headers=headers, cookies=cookies, data=data)
            cookies = {
                'PHPSESSID':  cookies_dictionary['PHPSESSID'],
                '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
                'TawkConnectionTime': '0',
                '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
            }
    
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://aumaletv.com',
                'Connection': 'keep-alive',
                'Referer': 'https://aumaletv.com/login.php',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
    
            data = {
              'login_username': USERR,
              'login_password': USERR,
              'login': ''
            }
    
            response = requests.post('https://aumaletv.com/login.php', headers=headers, cookies=cookies, data=data)
            cookies = {
                'PHPSESSID':  cookies_dictionary['PHPSESSID'],
                '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
                'TawkConnectionTime': '0',
                '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
            }
    
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://aumaletv.com',
                'Connection': 'keep-alive',
                'Referer': 'https://aumaletv.com/dashboard.php',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
    
            data = {
              'username': USERR,
              'password': USERR,
              'update_user': ''
            }
    
            response = requests.post('https://aumaletv.com/update1996.php', headers=headers, cookies=cookies, data=data)
    
    
            cookies = {
                'PHPSESSID':  cookies_dictionary['PHPSESSID'],
                '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
                'TawkConnectionTime': '0',
                '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
            }
    
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Referer': 'https://forex-trnd.com/',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
            }
            r1 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
            r2 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
            print(r2)
            
            try:
                da=re.findall('id="expired_date".*?value=(.*?)>',r2)[0].split('"')[1]
                da=float(da)
                #expp=re.findall('Expiring date.*?>(.*?)<',response.text,re.DOTALL)
                expp=datetime.fromtimestamp(float(da)).strftime('%d-%m-%Y @ %H:%M:%S')
                with open('/tmp/aumaletv_expr.txt','w') as f:
                    f.write('Aumaletv successufly run and updated\n it will expire on\n'+expp+'\n'+USERR)
                print ('Aumaletv successufly run and updated\n it will expire on\n'+expp)
                with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','r') as f:
                    ff=f.readlines()
                fff=ff[1].split(':')[-3].strip()+':'+ff[1].split(':')[-2]+':'+ff[1].split(':')[-1].split(' ')[0]
                ff[1]=ff[1].replace(fff,expp)
                fff1=ff[2].split(':')[-3].strip()+':'+ff[2].split(':')[-2]+':'+ff[2].split(':')[-1].split(' ')[0]
                ff[2]=ff[2].replace(fff1,expp)
                for i in ff:
                    if 'SERVICE' in i and 'http' in i:
                        break
                oldusr=i.split('/')[-3]
                oldpas=i.split('/')[-2]
                f1=[i.replace(oldusr,USERR).replace(oldpas,USERR) for i in ff ]
                with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','w') as f:
                    for i in f1:
                        f.write(i)
                
            except:
                with open('/tmp/aumaletv_expr.txt','w') as f:
                    f.write('Aumaletv FAILED to run ')
                print('Aumaletv FAILED to run ')
        else: 
            print('Aumaletv still Active till  '+expdate[0]+'\n'+'with user  = '+existusr)
    else:
        cookies = {
            'PHPSESSID':  cookies_dictionary['PHPSESSID'],
            '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
            'TawkConnectionTime': '0',
            '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://aumaletv.com',
            'Connection': 'keep-alive',
            'Referer': 'https://aumaletv.com/create.php',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }

        data = {
          'name': USERR,
          'pass': USERR,
          'bouquet': '[1,2,44,31,9,22,8,16,18,19,10,6,4,12,7,13,24]',
          'create_user': ''
        }

        response = requests.post('https://aumaletv.com/create.php', headers=headers, cookies=cookies, data=data)
        cookies = {
            'PHPSESSID':  cookies_dictionary['PHPSESSID'],
            '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
            'TawkConnectionTime': '0',
            '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://aumaletv.com',
            'Connection': 'keep-alive',
            'Referer': 'https://aumaletv.com/login.php',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }

        data = {
          'login_username': USERR,
          'login_password': USERR,
          'login': ''
        }

        response = requests.post('https://aumaletv.com/login.php', headers=headers, cookies=cookies, data=data)
        cookies = {
            'PHPSESSID':  cookies_dictionary['PHPSESSID'],
            '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
            'TawkConnectionTime': '0',
            '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://aumaletv.com',
            'Connection': 'keep-alive',
            'Referer': 'https://aumaletv.com/dashboard.php',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }

        data = {
          'username': USERR,
          'password': USERR,
          'update_user': ''
        }

        response = requests.post('https://aumaletv.com/update1996.php', headers=headers, cookies=cookies, data=data)


        cookies = {
            'PHPSESSID':  cookies_dictionary['PHPSESSID'],
            '__gads': 'ID=44c6c3a24a7f782e-22687ff7f3d0001b:T=1645641282:RT=1645641282:S=ALNI_Ma9vrtluC0aZA1s2sFDfM6OQ1_2_g',
            'TawkConnectionTime': '0',
            '__tawkuuid': 'e::aumaletv.com::e9ZxrqLqInqiDGiJ8AKZWyE2AM95Lt+YaDlZkEdMFTWdgiFfIp1onmgicWLLxdG9::2',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://forex-trnd.com/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
        }
        r1 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
        r2 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')
        print(r2)
        
        try:
            #da=re.findall('id="expired_date".*?value=(.*?)>',r2)[0].split('"')[1]
            #da=float(da)
            expp=re.findall('Expiring date.*?>(.*?)<',response.text,re.DOTALL)
            with open('/tmp/aumaletv_expr.txt','w') as f:
                f.write('Aumaletv successufly run and updated\n it will expire on\n'+expp+'\n'+USERR)
            print ('Aumaletv successufly run and updated\n it will expire on\n'+expp)
            with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','r') as f:
                ff=f.readlines()
            fff=ff[1].split(':')[-3].strip()+':'+ff[1].split(':')[-2]+':'+ff[1].split(':')[-1].split(' ')[0]
            ff[1]=ff[1].replace(fff,expp)
            fff1=ff[2].split(':')[-3].strip()+':'+ff[2].split(':')[-2]+':'+ff[2].split(':')[-1].split(' ')[0]
            ff[2]=ff[2].replace(fff1,expp)
            for i in ff:
                if 'SERVICE' in i and 'http' in i:
                    break
            oldusr=i.split('/')[-3]
            oldpas=i.split('/')[-2]
            f1=[i.replace(oldusr,USERR).replace(oldpas,USERR) for i in ff ]
            with open('/etc/enigma2/userbouquet.aumaletv__tv_.tv','w') as f:
                for i in f1:
                    f.write(i)
            
        except:
            with open('/tmp/aumaletv_expr.txt','w') as f:
                f.write('Aumaletv FAILED to run ')
            print('Aumaletv FAILED to run ')
        
except:
    with open('/tmp/aumaletv_expr.txt','w') as f:
        f.write('Aumaletv FAILED to run ')
    print ('Aumaletv FAILED to run ')
        

