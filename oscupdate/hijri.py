# -*- coding: utf-8 -*-


import requests
import re
import urllib3
urllib3.disable_warnings()
import datetime

import sys
PY3 = (sys.version_info[0] == 3)

now = datetime.datetime.now()





def pry(su,nbr):
    su=su.replace(' ','').replace('AM','').replace('PM','').split(':')
    su0=int(su[0])
    su1=int(su[1])+nbr
    if su1 >=60:
        su1=su1-60
        if su0==23:
            su0=0
        else:
            su0=su0+1
    if su0<10:
        su0='0'+str(su0)
    else:
        su0=str(su0)
    if su1<10:
        su1='0'+str(su1)
    else:
        su1=str(su1)
    return su0 + ':' + su1

UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Accept': 'text/html'}
#link1='https://www.islamicfinder.org/world/algeria/40166658/algiers-prayer-times/'
#link1='https://timesprayer.com/en/hijri-date-in-algeria.html'


link="https://www.muslimpro.com/Prayer-times-Tipasa-Algeria-2476028"
f = requests.get(link,headers=UserAgent,timeout=5.0,verify=False)
the_page = f.text
#f1 = requests.get(link1,headers=UserAgent,timeout=1.0,verify=False)
#the_page1 = f1.text.encode('ascii', 'ignore')
"""str1=str(now.day)+'&nbsp;'+now.strftime("%B")+',&nbsp;'+str(now.year)

page=the_page1.split('\n')
for i in range(len(page)):
    if str1 in page[i]:
        break
dat=page[i+1].split('>')[1].strip('</p').replace('&nbsp;',' ')"""

#dat=re.findall('Today Hijri date</td><td>(.*?)<',the_page1)[0]

"""for ii in range(i,len(page)):
    if 'fajr' in page[ii].lower():
        break
farj=page[ii+1].split('>')[1].split('<')[0]

i=ii+1
for ii in range(i,len(page)):
    if '>sunrise' in page[ii].lower():
        break
sun=page[ii+1].split('>')[1].split('<')[0]

i=ii+1
for ii in range(i,len(page)):
    if '>dhuhr' in page[ii].lower():
        break
Dhuhr=page[ii+1].split('>')[1].split('<')[0]

i=ii+1
for ii in range(i,len(page)):
    if '>asr' in page[ii].lower():
        break
Asr=page[ii+1].split('>')[1].split('<')[0]

i=ii+1
for ii in range(i,len(page)):
    if '>maghr' in page[ii].lower():
        break
Maghr=page[ii+1].split('>')[1].split('<')[0]

i=ii+1
for ii in range(i,len(page)):
    if '>isha' in page[ii].lower():
        break
Isha=page[ii+1].split('>')[1].split('<')[0]"""


a=re.findall('prayer-daily-table(.*?)#',the_page)[0].split('<span')

for i in range(len(a)):
    if 'fajr' in a[i].lower():
        break
faj=a[i+1].split('>')[1].split('<')[0]
farj=pry(faj,1)

for i in range(len(a)):
    if 'sunrise' in a[i].lower():
        break
su=a[i+1].split('>')[1].split('<')[0]
sun=pry(su,1)

for i in range(len(a)):
    if 'dhuhr' in a[i].lower():
        break
du=a[i+1].split('>')[1].split('<')[0]
Dhuhr=pry(du,1)

for i in range(len(a)):
    if 'asr' in a[i].lower():
        break

asr=a[i+1].split('>')[1].split('<')[0]
Asr= pry(asr,1)

for i in range(len(a)):
    if 'maghrib' in a[i].lower():
        break

mag=a[i+1].split('>')[1].split('<')[0]

Maghr= pry(mag,1)

for i in range(len(a)):
    if 'sha' in a[i].lower():
        break

ish=a[i+1].split('>')[1].split('<')[0]
Isha= pry(ish,1)

# ===========================================
#          isubqo.com
# ===========================================

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

r = requests.get('https://isubqo.com/prayer-time/algeria/tibazah/tibazah', headers=headers)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')
tables = soup.find_all('table')
# the whole month
#table = soup.find('table', class_='table-striped')

# Today
table = soup.find('table', class_='namaz-time-view')
ada=[]
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if columns !=[]:
        ada.append([ i.text.strip() for i in columns])

import datetime

for i in ada:
    if datetime.datetime.today().strftime('%b %d')==i[0]:
        break


def timeConversion(s):
    s=s.replace(' ','')
    if  "am" in  s.split(':')[1].lower() :
      if float(s.split(':')[0])<10:
        a = str('0' + s.split(':')[0])+':'+re.findall(r'\d+',s.split(':')[1])[0]
      elif float(s.split(':')[0])==12:
        a = str('00:'+re.findall(r'\d+',s.split(':')[1])[0])
      else:
        a = s.split(':')[0]++':'+re.findall(r'\d+',s.split(':')[1])
    else:
        if float(s.split(':')[0])==12:
            a = str(s.split(':')[0])+':'+re.findall(r'\d+',s.split(':')[1])[0]
        else:
            a = str(int(s.split(':')[0])+12)+':'+re.findall(r'\d+',s.split(':')[1])[0]
    return a


# the whole month
'''
farj=timeConversion(i[2])
sun=timeConversion(i[3])
Dhuhr=timeConversion(i[4])
Asr=timeConversion(i[5])
Maghr=timeConversion(i[6])
Isha=timeConversion(i[7])

[['Fajr', '5:32 AM'],
 ['Dhuhr', '12:37 PM'],
 ['Asr', '3:48 PM'],
 ['Asr (Hanafi)', '4:36 PM'],
 ['Maghrib', '6:19 PM'],
 ['Isha', '7:37 PM'],
 ['Sunrise', '6:57 AM'],
 ['Sunset', '6:19 PM'],
 ['Moonrise', '9:58 PM'],
 ['Moonset', '12:35 PM'],
 ['Qibla Direction', '104.36° from North']]
 
'''
# Today

farj=timeConversion(ada[0][1])
sun=timeConversion(ada[6][1])
Dhuhr=timeConversion(ada[1][1])
Asr=timeConversion(ada[2][1])
Maghr=timeConversion(ada[4][1])
Isha=timeConversion(ada[5][1])



try:
    link2='https://www.echoroukonline.com/date'
    f2 = requests.get(link2,headers=UserAgent,timeout=1.0,verify=False)
    the_page2 = f2.text
    #az=re.findall('data-ar-date="(.*?)<',the_page2)[0].split(',')[1]
    '''try:
        az=az.strip('\xd8\xa7\xd9\x84\xd9\x85\xd9\x88\xd8\xa7\xd9\x81\xd9\x82 \xd9\x84\xd9\x80 ')
    except:
        az=az'''
    if len(the_page2.split(',')[1].strip().split())==5:
        az=the_page2.split(',')[1].strip().split()[2]+' '+the_page2.split(',')[1].strip().split()[3]+' '+the_page2.split(',')[1].strip().split()[4]
    elif len(the_page2.split(',')[1].strip().split())==6:
        az=the_page2.split(',')[1].strip().split()[2]+' '+the_page2.split(',')[1].strip().split()[3]+' '+the_page2.split(',')[1].strip().split()[4]+' '+the_page2.split(',')[1].strip().split()[5]
    echo=az
    n1=int(echo.split(' ')[0])
    dsd=str(n1)+' '+' '.join(echo.split(' ')[1:])

    echo1=[n1,dsd+'\n'+farj+'\n'+sun+'\n'+Dhuhr+'\n'+Asr+'\n'+Maghr+'\n'+Isha]
except:
    echo="none"
try:
    link2='https://marw.dz/'
    f2 = requests.get(link2,headers=UserAgent,timeout=2.0,verify=False)
    the_page = f2.text
    az=re.findall('fa fa-calendar-day(.*?)</section>',f2.text,re.DOTALL)[0].split()[3]+ ' '+re.findall('fa fa-calendar-day(.*?)</section>',f2.text,re.DOTALL)[0].split()[4]+ ' '+re.findall('fa fa-calendar-day(.*?)</section>',f2.text,re.DOTALL)[0].split()[5]
    marw=az
    n2=float(marw.split(' ')[0])
    marw1=[n2,az+'\n'+farj+'\n'+sun+'\n'+Dhuhr+'\n'+Asr+'\n'+Maghr+'\n'+Isha]

except:
    marw="none"



if echo !="none" and marw != "none":
    ooo=open('/usr/share/skin.txt','w')
    ooo.write(marw1[1])
    ooo.close()
    #lis2={echo1[1]:echo1[0],marw1[1]:marw1[0]}
    #ooo=open('/usr/share/skin.txt','w')
    #ooo.write(max(lis2, key=lis2.get))
    #ooo.close()
elif echo !="none" and marw == "none":
    ooo=open('/usr/share/skin.txt','w')
    ooo.write(echo1[1])
    ooo.close()
elif echo =="none" and marw != "none":
    ooo=open('/usr/share/skin.txt','w')
    ooo.write(marw1[1])
    ooo.close()

