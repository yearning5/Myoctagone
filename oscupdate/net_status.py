import urllib3
urllib3.disable_warnings()
import os
import urllib
try:
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except:
    status = "Disconnected"

ff=os.popen('route -n').read()

if 'wlan' in ff:
    if status == "Connected" :
        statt=  'Wifi_Ok'
    else:
        statt= 'Wifi_NOT'
elif 'eth' in ff:
    if status == "Connected" :
        statt=  'LAN_Ok'
    else:
        statt= 'LAN_NOT'
else:
    statt= 'NO Connection'

with open('/tmp/skin.txt') as f:
    l=f.readlines()
if len(l)==7:
    l.append('\n'+statt)
else:
    l[7] =statt
with open('/tmp/skin.txt','w') as f:
    for i in l:
        f.write(i)
