import requests,random

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
    
    response = requests.post('https://clinetest.net/cam.php', cookies=cookies, headers=headers, data=data)
    #print response.content
    if 'green' in response.content:
        return True
    else:
        return False
    
    