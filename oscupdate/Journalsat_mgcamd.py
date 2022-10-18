import requests,re, random


uuser= str(random.randrange(1, 10**9))

cookies = {
    '_ga': 'GA1.2.1444096135.1619435351',
    '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
    '_gid': 'GA1.2.112354009.1625736097',
    'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736098969],null,null]',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://cccam.journalsat.com',
    'Connection': 'keep-alive',
    'Referer': 'http://cccam.journalsat.com/index.php',
    'Upgrade-Insecure-Requests': '1',
}

r1 = requests.post('http://cccam.journalsat.com/index.php', headers=headers, cookies=cookies)


cookies = {
    '_ga': 'GA1.2.1444096135.1619435351',
    '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
    '_gid': 'GA1.2.112354009.1625736097',
    'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736098969],null,null]',
    'uername': uuser,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://cccam.journalsat.com/index.php',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

r2 = requests.get('http://cccam.journalsat.com/get.php', headers=headers, cookies=cookies)

cookies = {
    '_ga': 'GA1.2.1444096135.1619435351',
    '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
    '_gid': 'GA1.2.112354009.1625736097',
    'uername': uuser,
    'FCCDCF': '[null,null,[[[],[],[],[],null,null,true],1625736388648],null,null]',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://cccam.journalsat.com',
    'Connection': 'keep-alive',
    'Referer': 'http://cccam.journalsat.com/get.php',
    'Upgrade-Insecure-Requests': '1',
}

params = (
    ('do', 'mgcam'),
)

data = {
  'do': 'mgcam',
  'dgam': 'generate'
}

r3 = requests.post('http://cccam.journalsat.com/get.php', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://cccam.journalsat.com/get.php?do=mgcam', headers=headers, cookies=cookies, data=data)
a=re.findall('N:(.*?)<',r3.text.encode('ascii','ignore'))[0].strip().split(' ')
print uuser,a
