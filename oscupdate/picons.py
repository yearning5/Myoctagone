import requests,os, re
import shutil


nile="7.0W"
astra='19.2E'
thor='0.8W'
hispa='30.0W'
badr='26.0E'
hotbird='13.0E'
cookies = {
    '_ga': 'GA1.2.1469267885.1651189139',
    '_gid': 'GA1.2.1013217857.1651189139',
    '_gat_gtag_UA_167951831_1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://picon.cz/download-picons/',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.1469267885.1651189139; _gid=GA1.2.1013217857.1651189139; _gat_gtag_UA_167951831_1=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

r1 = requests.get('https://picon.cz/download-picons/picontransparent-400x170/', cookies=cookies, headers=headers)

#sats=["7.0W",'19.2E','0.8W','30.0W','26.0E','13.0E']
sats=["7.0W"]
links=[]
for i in sats:
    a1=r1.content.find(i)
    a2=r1.content[:a1].rfind('href="')
    a3=r1.content[a2:a1]
    a4=re.findall(r'href="(.*?)"',a3)[0]
    reg="("+i+".*?)\t"
    links.append([a4,re.findall(reg,r1.content)[0]])

if os.path.exists(r"/tmp/ere"):
    shutil.rmtree(r"/tmp/ere", ignore_errors=True)
    os.makedirs(r"/tmp/ere")
else:
    os.makedirs(r"/tmp/ere")
for i in links:
    r = requests.get(i[0], cookies=cookies, headers=headers)

    with open(r'/tmp/ere/' +i[1], 'wb') as out:
        out.write(r.content)
    print('File '+i[1]+' is created')
