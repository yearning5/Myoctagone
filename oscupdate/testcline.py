import requests,random

def tescline(cline):
    cookiescl = {
        'apbct_urls': '%7B%22www.testious.com%2F%22%3A%5B1664824932%5D%2C%22testious.com%2F%22%3A%5B1664826758%2C1664826769%2C1664826871%2C1664827158%2C1664827216%5D%7D',
        'apbct_site_referer': 'UNKNOWN',
        'apbct_timestamp': '1664827216',
        'apbct_site_landing_ts': '1664824933',
        'apbct_page_hits': '11',
        'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%25221a796c1f30cd9fd1caad13a248a8a9a2%2522%257D',
        'ct_sfw_pass_key': 'f38a193d4a33e0166599ee795659f8d90',
        'ct_ps_timestamp': '1664827230',
        'ct_fkp_timestamp': '1664827235',
        'ct_pointer_data': '%5B%5B240%2C752%2C353%5D%2C%5B235%2C435%2C528%5D%2C%5B228%2C447%2C917%5D%2C%5B179%2C572%2C953%5D%2C%5B277%2C878%2C1120%5D%2C%5B305%2C865%2C1270%5D%2C%5B288%2C815%2C1436%5D%2C%5B288%2C685%2C1586%5D%2C%5B291%2C597%2C1754%5D%2C%5B288%2C590%2C1914%5D%2C%5B287%2C592%2C2067%5D%2C%5B285%2C628%2C2220%5D%2C%5B284%2C630%2C2383%5D%2C%5B288%2C647%2C2537%5D%2C%5B288%2C682%2C2707%5D%2C%5B288%2C687%2C2847%5D%2C%5B284%2C730%2C3004%5D%2C%5B281%2C734%2C3157%5D%2C%5B286%2C812%2C3321%5D%2C%5B284%2C811%2C3494%5D%2C%5B309%2C802%2C3621%5D%2C%5B329%2C799%2C3776%5D%2C%5B336%2C742%2C3937%5D%2C%5B339%2C745%2C4127%5D%2C%5B334%2C749%2C5152%5D%2C%5B302%2C788%2C5187%5D%2C%5B285%2C803%2C5407%5D%5D',
        'ct_timezone': '1',
        'ct_screen_info': '%7B%22fullWidth%22%3A1903%2C%22fullHeight%22%3A2299%2C%22visibleWidth%22%3A1903%2C%22visibleHeight%22%3A605%7D',
        'apbct_headless': 'false',
        'apbct_pixel_url': 'https%3A%2F%2Fmoderate10.cleantalk.org%2Fpixel%2F2c4431aeefc355ba69b9bede8a1f7d9a.gif',
        'ct_checked_emails': '0',
        'ct_checkjs': '2973468',
        'cookielawinfo-checkbox-necessary': 'yes',
        'cookielawinfo-checkbox-non-necessary': 'yes',
        'bp-activity-oldestpage': '1',
        'ct_mouse_moved': 'true',
        'PHPSESSID': 'mtj1midaqp4rqtaso8cjq45cv3',
        'ct_has_scrolled': 'true',
    }
    
    headerscl = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://testious.com',
        'Connection': 'keep-alive',
        'Referer': 'https://testious.com/',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'apbct_urls=%7B%22www.testious.com%2F%22%3A%5B1664824932%5D%2C%22testious.com%2F%22%3A%5B1664826758%2C1664826769%2C1664826871%2C1664827158%2C1664827216%5D%7D; apbct_site_referer=UNKNOWN; apbct_timestamp=1664827216; apbct_site_landing_ts=1664824933; apbct_page_hits=11; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%25221a796c1f30cd9fd1caad13a248a8a9a2%2522%257D; ct_sfw_pass_key=f38a193d4a33e0166599ee795659f8d90; ct_ps_timestamp=1664827230; ct_fkp_timestamp=1664827235; ct_pointer_data=%5B%5B240%2C752%2C353%5D%2C%5B235%2C435%2C528%5D%2C%5B228%2C447%2C917%5D%2C%5B179%2C572%2C953%5D%2C%5B277%2C878%2C1120%5D%2C%5B305%2C865%2C1270%5D%2C%5B288%2C815%2C1436%5D%2C%5B288%2C685%2C1586%5D%2C%5B291%2C597%2C1754%5D%2C%5B288%2C590%2C1914%5D%2C%5B287%2C592%2C2067%5D%2C%5B285%2C628%2C2220%5D%2C%5B284%2C630%2C2383%5D%2C%5B288%2C647%2C2537%5D%2C%5B288%2C682%2C2707%5D%2C%5B288%2C687%2C2847%5D%2C%5B284%2C730%2C3004%5D%2C%5B281%2C734%2C3157%5D%2C%5B286%2C812%2C3321%5D%2C%5B284%2C811%2C3494%5D%2C%5B309%2C802%2C3621%5D%2C%5B329%2C799%2C3776%5D%2C%5B336%2C742%2C3937%5D%2C%5B339%2C745%2C4127%5D%2C%5B334%2C749%2C5152%5D%2C%5B302%2C788%2C5187%5D%2C%5B285%2C803%2C5407%5D%5D; ct_timezone=1; ct_screen_info=%7B%22fullWidth%22%3A1903%2C%22fullHeight%22%3A2299%2C%22visibleWidth%22%3A1903%2C%22visibleHeight%22%3A605%7D; apbct_headless=false; apbct_pixel_url=https%3A%2F%2Fmoderate10.cleantalk.org%2Fpixel%2F2c4431aeefc355ba69b9bede8a1f7d9a.gif; ct_checked_emails=0; ct_checkjs=2973468; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; bp-activity-oldestpage=1; ct_mouse_moved=true; PHPSESSID=mtj1midaqp4rqtaso8cjq45cv3; ct_has_scrolled=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    
    
    
    for i in range(50):
        data = {
            'line': cline,
            'captcha': str(random.randint(0, 4)),
        }
        
        response = requests.post('https://testious.com/tester/check.php', cookies=cookiescl, headers=headerscl, data=data)
        print i
        if 'wrong' not in response.content:
            #print response.content
            break
    if 'o' == response.content[0]:
        return True
    else:
        return False