import requests
import re
import urllib3
urllib3.disable_warnings()
import datetime
import os


UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0', 'Accept': 'text/html'}
link='https://gitlab.com/Rgysoft/iptv-host-e2iplayer/-/tree/master/IPTVPlayer/tsiplayer'

f2 = requests.get(link,headers=UserAgent,timeout=1.0,verify=False)
the_page = f2.text.encode('utf-8')
az=re.findall('download=".*?href="(.*?).zip">',the_page)
link2='https://gitlab.com'+az[0]+'.zip'

#import  urllib

#resp = urllib.urlretrieve(link2,'/tmp/iptvplaye.zip')

import requests, zipfile, StringIO
r = requests.get(link2, stream=True)
archive = zipfile.ZipFile(StringIO.StringIO(r.content))

#archive = zipfile.ZipFile('/tmp/iptvplaye.zip')
listt=archive.namelist()

tsip=next( i for i in listt if 'tsiplayer/' in i )
archive.extractall('/tmp/')
cmd='cp -TR /tmp/'+tsip+' /usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/'+tsip.split('/')[-2]
os.system(cmd)
