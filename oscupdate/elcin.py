#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __init__ import *

import requests, re, io, sys, os, ssl, json
from datetime import datetime,timedelta
from time import sleep,strftime
from requests.adapters import HTTPAdapter
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

headers={
    'Host': 'elcinema.com',
    "Connection": "keep-alive",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
}

nb_channel=["1353-2M Monde","1312-Al Aoula International",'1101-Aloula', '1120-ART_Aflam_1', '1121-ART_Aflam_2', '1122-ART_Hekayat', 
            '1134-ONDrama', '1135-Emirates', '1136-Abu_Dhabi_TV', '1137-Alhayat_TV', 
            '1138-AlhayatDrama', '1145-Mehwar', '1148-RotanaCinema EGY', '1156-NileDrama', 
            '1157-Nile_Cinema', '1158-NileComedy', '1159-NileLife', '1168-LBCI', '1169-Dubai_TV', 
            '1170-AlraiTV', '1173-Dubai_One', '1174-AlKaheraWalNasTV', '1176-Cima', '1177-SamaDubai', 
            '1177-Sama_Dubai', '1178-Abu_Dhabi_Drama', '1179-Dream', '1182-ART_Hekayat_2', 
            '1188-SharjahTV', '1193-Al_Nahar_TV', '1195-ART_Cinema', '1198-CBC', '1199-CBC_Drama', 
            '1203-ONE', '1204-iFILMTV', '1216-AlJadeedTV', '1217-Rotana_Classic', '1223-Al_Nahar_Drama', 
            '1226-SadaElBalad', '1227-SadaElBaladDrama', '1252-AlKaheraWalNasTV2', '1260-CBC_sofra', 
            '1261-Zee_alwan', '1262-Zee_aflam', '1264-AlDafrah', '1269-Alsharqya', '1279-SadaElBalad+2', 
            '1280-TeNTV', '1283-Dubai_Zaman', '1290-DMC', '1292-DMC_DRAMA', '1296-MTVLebnon', '1297-SBC', 
            '1298-Amman', '1299-Roya', '1300-SyriaDrama', '1301-Alsumaria', '1302-Fujairah', '1304-Nessma', 
            '1308-Watania1', '1310-Kuwait', '1313-Lana', '1314-JordanTV', '1317-Oman', '1321-almanar', 
            '1334-Watania2', '1336-MasperoZaman', '1338-SyriaTV', '1339-AlSaeedah', 
            '1339-Al_Saeedah', '1341-LBC', '1342-LanaPlusTV', '1350-SamaTV', '1352-Saudiya_TV', '1355-Mix','1366-Thikrayat']


if not os.path.exists(r'/tmp/api'):
    os.makedirs(r'/tmp/api')
    
os.popen('wget -O /tmp/api/providers.json "https://raw.githubusercontent.com/ziko-ZR1/Epg-plugin/master/src/EPGGrabber/api/providers.json"')
PROVIDERS_ROOT = '/tmp/api/providers.json'
API_PATH = '/tmp/api'
EPG_ROOT = '/etc/epgimport'
def get_tz():
    try:
        url_content = requests.get('http://worldtimeapi.org/api/ip').json()
        js =  {'tz':url_content['utc_offset'].replace(':', '')}
        file = open(API_PATH+'/tz.json','w')
        json.dump(js, file, indent = 4)
        file.close()
    except:
        js = {'tz':strftime('%z')}
        file = open(API_PATH+'/tz.json','w')
        json.dump(js, file, indent = 4)
        file.close()
def tz():
    if os.path.exists(API_PATH+'/tz.json'):
        this_month = datetime.today().strftime('%Y-%m')
        file_date = datetime.fromtimestamp(os.stat(API_PATH+'/tz.json').st_mtime).strftime('%Y-%m')
        if this_month != file_date:
            get_tz()
            file = open(API_PATH+'/tz.json','r')
            timezone = file.read()
            file.close()
            return json.loads(timezone)['tz']
        else:
            file = open(API_PATH+'/tz.json','r')
            timezone = file.read()
            file.close()
            return json.loads(timezone)['tz']
    else:
        get_tz()
        file = open(API_PATH+'/tz.json','r')
        timezone = file.read()
        file.close()
        return json.loads(timezone)['tz']

from sys import version_info
PY3 = version_info[0] == 3

def xml_header(path,channels):
    file = open(path,'w')
    if PY3:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<tv generator-info-name="By ZR1">')
    else:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n'.decode('utf-8'))
        file.write(('<tv generator-info-name="By ZR1">').decode('utf-8'))
    file.close()
    
    for channel in channels:
        with io.open(path,"a",encoding='UTF-8')as f:
            if PY3:
                f.write("\n"+'  <channel id="'+channel+'">'+"\n"+'    <display-name lang="en">'+channel+'</display-name>'+"\n"+'  </channel>\r')
            else:
                f.write(("\n"+'  <channel id="'+channel+'">'+"\n"+'    <display-name lang="en">'+channel+'</display-name>'+"\n"+'  </channel>\r').decode('utf-8'))
def close_xml(path):
    file = open(path,'a')
    if PY3:
        file.write('\n'+'</tv>')
    else:
        file.write(('\n'+'</tv>').decode('utf-8'))
        
    file.close()                
        
time_zone = tz()

REDC =  '\033[31m'                                                              
ENDC = '\033[m'                                                                 
                                                                                
def cprint(text):                                                               
    print(REDC+text+ENDC)


class Elcinema:
    
    def __init__(self,channel):
        self.getData(channel)
        self.prog_start =[]
        self.prog_end=[]
        self.description=[]
        self.now=datetime.today().strftime('%Y %m %d')
        self.titles =[]
        self.Toxml(channel)
    
    def getData(self,ch):
        with requests.Session() as s:
            ssl._create_default_https_context = ssl._create_unverified_context
            s.mount('https://', HTTPAdapter(max_retries=100))
            url = s.get('https://elcinema.com/tvguide/'+ch.split('-')[0]+'/',headers=headers,verify=False)
            self.data = url.text
                  
    def Starttime(self):
        hours = []
        for time in re.findall(r'(\d\d\:\d\d.*)',self.data):
            if PY3:
            	if '??????????' in time or '????????????' in time:
                	start=datetime.strptime(time.replace('</li>','').replace('??????????','PM').replace('????????????','AM'),'%I:%M %p')
                	hours.append(start.strftime('%H:%M'))
            else:
            	if '??????????'.decode('utf-8') in time or '????????????'.decode('utf-8') in time:
                	start=datetime.strptime(time.replace('</li>','').replace('??????????'.decode('utf-8'),'PM').replace('????????????'.decode('utf-8'),'AM'),'%I:%M %p')
                	hours.append(start.strftime('%H:%M'))
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) 
        last_hr = 0
        for d in hours:
            h, m = map(int, d.split(":"))
            if last_hr > h:
                today += + timedelta(days=1)
            last_hr = h
            self.prog_start.append(today + timedelta(hours=h, minutes=m))  
               
        return self.prog_start
    
    def Endtime(self):
        minutes =[]
        for end in re.findall(r'\"subheader\">\[(\d+)',self.data):     
            minutes.append(int(end))
        start = datetime.strptime(datetime.strptime(str(self.Starttime()[0]),'%Y-%m-%d %H:%M:%S').strftime('%Y %m %d %H:%M'),'%Y %m %d %H:%M') 
        for m in minutes:
            x=start+timedelta(minutes=m)
            start += timedelta(minutes=m)
            self.prog_end.append(x)
            
        return self.prog_end
            
    
    def GetDes(self):
        for f,l in zip(re.findall(r'<li>(.*?)<a\shref=\'#\'\sid=\'read-more\'>',self.data),re.findall(r"<span class='hide'>[^\n]+",self.data)):
            self.description.append(f+l.replace("<span class='hide'>",'').replace('</span></li>',''))
        return self.description

    def Gettitle(self):
        self.title = re.findall(r'<a\shref=\"\/work\/\d+\/\">(.*?)<\/a><\/li',self.data)
        mt = re.findall(r'<a\shref=\"\/work\/\d+\/\">(.*?)<\/a><\/li|columns small-7 large-11\">\s+<ul class=\"unstyled no-margin\">\s+<li>(.*?)<\/li>',self.data)
        for m in mt:
            if m[0]=='' and m[1]=='':
                if PY3:
                	self.titles.append("?????????? ???????????? ?????? ?????????????? ?????? ????????????????")
                else:
                	self.titles.append("?????????? ???????????? ?????? ?????????????? ?????? ????????????????".decode('utf-8'))
            elif m[0]=='':
                self.titles.append(m[1])
            else:
                self.titles.append(m[0])
        for index, element in enumerate(self.titles):
            if element not in self.title:
                if PY3:
                	self.GetDes().insert(index,"?????????? ???????????? ?????? ?????????????? ?????? ????????????????")
                else:
                	self.GetDes().insert(index,"?????????? ???????????? ?????? ?????????????? ?????? ????????????????".decode('utf-8'))
                
        return self.titles
    
    def Toxml(self,channel):
        for elem,next_elem,title,des in zip(self.Starttime(),self.Endtime(),self.Gettitle(),self.GetDes()):
            ch=''
            startime=datetime.strptime(str(elem),'%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
            endtime=datetime.strptime(str(next_elem),'%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
            ch+= 2 * ' ' +'<programme start="' + startime + ' '+time_zone+'" stop="' + endtime + ' '+time_zone+'" channel="'+channel.split('-')[1]+'">\n'
            ch+=4*' '+'<title lang="ar">'+title.replace('&#39;',"'").replace('&quot;','"').replace('&amp;','and')+'</title>\n'
            ch+=4*' '+'<desc lang="ar">'+des.replace('&#39;',"'").replace('&quot;','"').replace('&amp;','and').replace('(','').replace(')','').strip()+'</desc>\n  </programme>\r'
            with io.open(EPG_ROOT+"/elcinema.xml","a",encoding='UTF-8')as f:
                f.write(ch)
                
        #print(channel.split('-')[1]+' epg ends at : '+str(self.Endtime()[-1]))
        sys.stdout.flush()          
            
def main():
    from datetime import datetime
    import json
    with open(PROVIDERS_ROOT, 'r') as f:
        data = json.load(f)
    for channel in data['bouquets']:
        if channel["bouquet"]=="elcin":
            channel['date']=datetime.today().strftime('%A %d %B %Y at %I:%M %p')
    with open(PROVIDERS_ROOT, 'w') as f:
        json.dump(data, f)
        
    print('**************ELCINEMA EPG******************')
    sys.stdout.flush()
    
    channels = [ch.split('-')[1] for ch in nb_channel]
    xml_header(EPG_ROOT+"/elcinema.xml",channels)
    
    import time
    Hour = time.strftime("%H:%M")
    start='00:00'
    end='02:00'
    if Hour>=start and Hour<end:
        print('Please come back at 2am to download the epg')
        sys.stdout.flush()
    else:
        for nb in nb_channel:
            try:
                Elcinema(nb)
            except IndexError:
                #cprint('No epg found or missing data for : '+nb.split('-')[1])
                sys.stdout.flush()
                continue
        
             
if __name__=='__main__':
    main()
    
    close_xml(EPG_ROOT+"/elcinema.xml")

    print('**************FINISHED******************')
    sys.stdout.flush()
