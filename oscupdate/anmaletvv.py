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

