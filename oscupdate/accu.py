# -*- coding: utf-8 -*-
import subprocess, requests
import re,random,string
#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"
import urllib3
urllib3.disable_warnings()
UserAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; Linux x86_64; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Safari/537.36',
            'Accept': 'text/html'}

link='https://www.accuweather.com/en/dz/tipaza/6474/daily-weather-forecast/6474'
f=requests.get(link,headers=UserAgent)
a=f.text.encode('utf-8')
b=re.findall('forecast-list-card forecast-card(.*?)/a',a,re.DOTALL)

strings = ["Day_%d" % int(x+1) for x in range(len(b))]
forecast=[]
for i,s in enumerate(b):
    day_0=[x.strip('\n\t') for x in re.findall('\t(.*?)\n',s)]
    day_0_day=day_0[3]
    day_0_date=day_0[6]
    day_0_tempH=day_0[11].split('>')[1].split('<')[0].split('&')[0].strip(' /')
    day_0_tempL=day_0[12].split('>')[1].split('<')[0].split('&')[0].strip(' /')
    day_0_com=day_0[15]
    day_0_prec=day_0[21].split('>')[1].split('<')[0]
    wheat=[strings[i],day_0_day,day_0_date,day_0_tempH,day_0_tempL,day_0_com,day_0_prec]
    forecast.append(wheat)

