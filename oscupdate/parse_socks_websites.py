# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:04:05 2022

@author: SONA0227
"""

import requests ,re
import urllib3 
urllib3.disable_warnings()


from bs4 import BeautifulSoup

prox = {"http":"http://hmdwsapxy:80",
     "https":"http://hmdwsapxy:80"}






# r = requests.get("https://www.google.com", proxies=a)



cookies = {
    '_ga': 'GA1.2.2106925822.1649059411',
    '_gid': 'GA1.2.1290515425.1649059411',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}


# ======================= https://proxyscrape.com/free-proxy-list ==============================

timeout='1000'
protocol='socks5'



r5 = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol='+protocol+'&timeout='+timeout+'&country=all&simplified=true', headers=headers,verify=False)

html_content = r5.content

list5=r5.content.replace('\r','').strip().split('\n')
print 'proxyscrape'
proxyscrape=list5






# ======================= socks-proxy.net/ ==============================



r = requests.get('https://www.socks-proxy.net/', headers=headers, cookies=cookies,verify=False)



a = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}\b',r.content,re.DOTALL)



html_content = r.content

soup = BeautifulSoup(html_content, "lxml")

# print the parsed data of html
# print(soup.prettify())

# print the title of the webpage
# print(soup.title)

# get the text without the HTML tags
# print(soup.title.text)

#  first get all three table headings

gdp_table = soup.find("table", attrs={"class": "table table-striped table-bordered"})

gdp_table_data = gdp_table.tbody.find_all("tr") 

list1=[]
for td in gdp_table_data:
    td1=[]
    for td in td:
        td1.append(td.text)
    
    list1.append([td1[0]+':'+td1[1],td1[4]])
print( 'socksproxynet')    
socksproxynet=[ i[0] for i in list1]    

# ======================= https://www.proxy-list.download/SOCKS5   ==============================

r2 = requests.get('https://www.proxy-list.download/SOCKS5', headers=headers,verify=False)

html_content = r2.content

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-bordered table-striped dataTable dtr-inline"})

gdp_table_data = gdp_table.tbody.find_all("tr") 

list2=[]
for td in gdp_table_data:
    td1=[]
    for td in td:
        try:
            td1.append( str(td.text).strip())
        except:
            pass
    
    
    list2.append([td1[0]+':'+td1[1],td1[4]])
proxylistdownload=[ i[0] for i in list2]   
print ('proxylistdownload')
# ======================= https://hidemy.name/en/proxy-list/  ==============================


r3 = requests.get('https://hidemy.name/en/proxy-list/?type=5#list', headers=headers,verify=False)
html_content = r3.content

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table")

gdp_table_data = gdp_table.tbody.find_all("tr") 

list3=[]

for td in gdp_table_data:
    td1=[]
    for td in td:
        td1.append(td.text)
   
    list3.append([td1[0]+':'+td1[1],td1[4]])
hidemyname=[ i[0] for i in list3]   
print( 'hidemyname')

# ======================= https://geonode.com/free-proxy-list/ ==============================


protocol='socks5'  # http%2Chttps%2Csocks4%2Csocks5

r4 = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=200&page=1&sort_by=lastChecked&sort_type=desc&protocols='+protocol, headers=headers,verify=False)

html_content = r4.content
a1=re.findall(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b).*?"port":"(.*?)"',r4.content,re.DOTALL)
list4=[]
for i in a1:
    list4.append(i[0]+':'+i[1])
geonode= list4

print('geonode')

# ======================= https://spys.one/en/socks-proxy-list/ ==============================

def isnumber(x):
    try:
        float(x)
        return True
    except:
        return False

r6 = requests.get('https://spys.one/en/socks-proxy-list/', headers=headers,verify=False)
html_content = r6.content


z='('+html_content[html_content[:html_content.find('=0^')].rfind(';')+1:html_content.find('=0^')]+'^'+html_content[html_content.find('=0^')+3:html_content.find('=0^')+html_content[html_content.find('=0^'):].find(';')]+')'
z1='('+html_content[html_content[:html_content.find('=1^')].rfind(';')+1:html_content.find('=1^')]+'^'+html_content[html_content.find('=1^')+3:html_content.find('=1^')+html_content[html_content.find('=1^'):].find(';')]+')'
z2='('+html_content[html_content[:html_content.find('=2^')].rfind(';')+1:html_content.find('=2^')]+'^'+html_content[html_content.find('=2^')+3:html_content.find('=2^')+html_content[html_content.find('=2^'):].find(';')]+')'
z3='('+html_content[html_content[:html_content.find('=3^')].rfind(';')+1:html_content.find('=3^')]+'^'+html_content[html_content.find('=3^')+3:html_content.find('=3^')+html_content[html_content.find('=3^'):].find(';')]+')'
z4='('+html_content[html_content[:html_content.find('=4^')].rfind(';')+1:html_content.find('=4^')]+'^'+html_content[html_content.find('=4^')+3:html_content.find('=4^')+html_content[html_content.find('=4^'):].find(';')]+')'
z5='('+html_content[html_content[:html_content.find('=5^')].rfind(';')+1:html_content.find('=5^')]+'^'+html_content[html_content.find('=5^')+3:html_content.find('=5^')+html_content[html_content.find('=5^'):].find(';')]+')'
z6='('+html_content[html_content[:html_content.find('=6^')].rfind(';')+1:html_content.find('=6^')]+'^'+html_content[html_content.find('=6^')+3:html_content.find('=6^')+html_content[html_content.find('=6^'):].find(';')]+')'
z7='('+html_content[html_content[:html_content.find('=7^')].rfind(';')+1:html_content.find('=7^')]+'^'+html_content[html_content.find('=7^')+3:html_content.find('=7^')+html_content[html_content.find('=7^'):].find(';')]+')'
z8='('+html_content[html_content[:html_content.find('=8^')].rfind(';')+1:html_content.find('=8^')]+'^'+html_content[html_content.find('=8^')+3:html_content.find('=8^')+html_content[html_content.find('=8^'):].find(';')]+')'
z9='('+html_content[html_content[:html_content.find('=9^')].rfind(';')+1:html_content.find('=9^')]+'^'+html_content[html_content.find('=9^')+3:html_content.find('=9^')+html_content[html_content.find('=9^'):].find(';')]+')'


dic={z:'0',z1:'1', z2:'2', z3:'3',z4:'4',z5:'5',z6:'6',z7:'7',z8:'8',z9:'9'}

l1=re.findall(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b).*?document.write.*?"<font class=spy2>:<\\/font>"\+(.*?)\)<.*?<font class=spy1>(.*?)<.*?<font class=spy1>(.*?)<.*?<font class=spy1>(.*?)<.*?<font class=spy1>(.*?)<',r6.content,re.DOTALL)
list66=[]
for i in l1:
    
    ii=i[1].split('+')
    port=[]
    for n in range(len(ii)):
        port.append(dic[ii[n]])
    if isnumber(i[4]):
        tt=i[4]
    elif isnumber(i[5]):
        tt=i[5]
    list66.append([i[0]+':'+''.join(port),tt] )   
    
list66=sorted(list66, key=lambda x:x[1])    
list6=[ i[0] for i in list66]
print('spysone')
spysone=list6
# ======================= http://proxydb.net/?protocol=socks5&country=  ==============================


r7 = requests.get('http://proxydb.net/?protocol=socks5&country=', headers=headers,verify=False)
html_content = r7.content

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "table table-sm table-hover table-bordered"})

gdp_table_data = gdp_table.tbody.find_all("tr") 

list7=[]

for td in gdp_table_data:
    td1=[]
    for td in td:
        try:
            td1.append( str(td.text).strip())
        except:
            pass
    
    list7.append(td1[0])

print( 'proxydb')
proxydb=list7

# =======================  https://www.proxyscan.io/download?type=socks5  ==============================

r8 = requests.get('https://www.proxyscan.io/download?type=socks5', headers=headers,verify=False)
html_content = r8.content

list8=r8.content.replace('\r','').strip().split('\n')
print 'proxyscan'
proxyscan=list8