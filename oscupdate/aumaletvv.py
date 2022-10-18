import requests,re

cookies = {
    '__gads': 'ID=9860f329e43195a1-2254746963c90076:T=1625487045:RT=1625487045:S=ALNI_MZCZn_2CgjqHnlmXx4tCM8HBXEQfQ',
    'PHPSESSID': 'kshcgfg49e70letkk6e84ibe9d',
    'TawkConnectionTime': '1625910630307',
    '__tawkuuid': 'e::aumaletv.com::Z4FGbjGgoPN8bPQ35Znppd1ATL0SWGRNdF2edM8YNPA3toXdnKb+qms7soKk3r8h::2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://aumaletv.com',
    'Connection': 'keep-alive',
    'Referer': 'https://aumaletv.com/update.php',
    'Upgrade-Insecure-Requests': '1',
}

data = {
  'username': 'yearning55',
  'password': 'yearning55',
  'update_user': ''
}

r = requests.post('https://aumaletv.com/update.php', headers=headers, cookies=cookies, data=data).text.encode('ascii','ignore')

link=re.findall('url=(.*?)"',r)[0]
print link

a_session = requests.Session()
a_session.get('https://aumaletv.com/result.php')
session_cookies = a_session.cookies
cookies_dictionary = session_cookies.get_dict()

cookies = {
    'PHPSESSID': cookies_dictionary['PHPSESSID'],
    '__gads': 'ID=e6cd674b2c4cae13-2257848f62c9004c:T=1625486870:RT=1625486870:S=ALNI_MazmiX4TCOG0GX9DT7YnRD51zv4JA',
    '__tawkuuid': 'e::aumaletv.com::nHnkUFVbwtySVEWvrbrSJGgPFCZiZg+B84BwF39hVXy049Q5Rnf7KYF87e64DVsq::2',
    'TawkConnectionTime': '0',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6,ar;q=0.5',
}

r1 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')

r2 = requests.get('https://aumaletv.com/result.php', headers=headers, cookies=cookies).text.encode('ascii','ignore')