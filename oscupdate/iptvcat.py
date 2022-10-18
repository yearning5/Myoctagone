# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:25:57 2022

@author: SONA0227
"""
import requests,re
from bs4 import BeautifulSoup

cookies = {
    'ci_session': '1dea1g8p61k8sd01o7b4fofv0bblnb60',
    '_ga': 'GA1.2.1002827630.1647419114',
    '_gid': 'GA1.2.2026471521.1647419114',
    '_gat_gtag_UA_159282801_1': '1',
    '_gat_gtag_UA_44972322_1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://iptvcat.net/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
}

link='https://iptvcat.com/s/equipe'
r = requests.get(link, headers=headers, cookies=cookies).text

if 'Nothing' in r:
    a=0
elif 'data-ci-pagination-page="' not in r:
    a=1
else:
    a=max([int(i) for i in re.findall('data-ci-pagination-page="(.*?)"',r)])
print (a)
if a >=1:    
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all('table', attrs={'class':'table table-xxs stream_table'})
    
    table=max(table,key=len)
    
    table_body = table.find('tbody')
    
    rows = table_body.find_all('tr')
    rows=[ii for ii in rows if 'belongs' in str(ii)]
    ta1=[]
    for row in rows:
        if '.m3u' not in str(row):
            ta=re.findall('title="(.*?)"',str(row))
            ta+= re.findall('class="live green".*?>(.*?)<',str(row))
        elif '.m3u' in str(row):
            ta.append(re.findall('download.*?href="(.*?)"',str(row))[0])   
        #cols = row.find_all('td')
        #cols = [ele.text.strip() for ele in cols]
        #data.append([ele for ele in cols if ele]) # Get rid of empty values
        ta1.append(ta)
if a > 1:
    for i in range(1,a):
        print( i)
        r = requests.get(link+'/'+str(i+1)+'/', headers=headers, cookies=cookies).text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find_all('table', attrs={'class':'table table-xxs stream_table'})
        table=max(table,key=len)
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        rows=[ii for ii in rows if 'belongs' in str(ii)]
        for row in rows:
            if '.m3u' not in str(row):
                ta=re.findall('title="(.*?)"',str(row))
                ta+= re.findall('class="live green".*?>(.*?)<',str(row))
            elif '.m3u' in str(row):
                ta.append(re.findall('download.*?href="(.*?)"',str(row))[0])   
            #cols = row.find_all('td')
            #cols = [ele.text.strip() for ele in cols]
            #data.append([ele for ele in cols if ele]) # Get rid of empty values
            ta1.append(ta)
new_k = []
for elem in ta1:
    if elem not in new_k:
        new_k.append(elem)
ta1 = new_k

ze=[ i for i in ta1 if 'online' in ''.join(i[0]).lower()]
ze1=[ i for i in ze if float(i[-2])>=90]
