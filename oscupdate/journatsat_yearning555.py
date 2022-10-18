import requests,re

cookies = {
    'PHPSESSID': '702b9f9rhgajh3jctj85opvs4h',
    '_ga': 'GA1.2.234181906.1625343291',
    '_gid': 'GA1.2.2139269596.1625343291',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://iptv.journalsat.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://iptv.journalsat.com/login.php',
    'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6,ar;q=0.5',
}

data = {
  'username': 'yearning555',
  'password': 'yearning555',
  'submit': ''
}

r = requests.post('http://iptv.journalsat.com/login.php', headers=headers, cookies=cookies, data=data, verify=False).text.encode('ascii','ignore')

if 'off' in re.findall(r'float-right badge badge(.*?)<',r)[0].lower():
    print re.findall(r'float-right badge badge(.*?)<',r)[0]
    print 'Your server is OFF and will be activated using  \nuser : yearning55\n passwoerd : yearning55\n m3u user = 939810687'
    cookies = {
            'PHPSESSID': '702b9f9rhgajh3jctj85opvs4h',
            '_ga': 'GA1.2.234181906.1625343291',
            '_gid': 'GA1.2.2139269596.1625343291',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://iptv.journalsat.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://iptv.journalsat.com/users.php',
        'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6,ar;q=0.5',
    }
    
    data = {
      'user': '985794251',
      'submit': ''
    }
    
    r1 = requests.post('http://iptv.journalsat.com/activate.php', headers=headers, cookies=cookies, data=data, verify=False).text.encode('ascii','ignore')
else:
    print re.findall(r'float-right badge badge(.*?)<',r)[0]
    if 'on' in re.findall(r'float-right badge badge(.*?)<',r)[0].lower():
        print 'Your server is ON and activated using  \nuser : yearning55\n passwoerd : yearning55\n m3u user = 939810687'
    
    
    
    
    
    
    
    
    
    