import requests
import os
import re
a=os.popen('curl -s -d "user="anaana"&pass="anaana"" -X POST http://infosat.satunivers.tv/mgfr/')
import time
time.sleep(2.4)
aa=a.read()
mghost=re.findall('host: (.*?)<',aa)[0].strip()
mgport=re.findall('port: (.*?)<',aa)[0].strip()
mguser=re.findall('user: (.*?)<',aa)[0].strip()
mgpass=re.findall('pass: (.*?)<',aa)[0].strip()
ffii=open('C:\Users\HERE\Desktop\erase-me\oscam.server','r')
read=ffii.readlines()
ffii.close()
for i in range(len(read)):
    if 'infosat.satunivers.tv,30000' in read[i]:
        break

read[i]='device                        = '+mghost+','+mgport+'\n'
read[i+2]='user                          = '+mguser+'\n'
read[i+3]='password                      = '+mgpass+'\n'
ffii=open('C:\Users\HERE\Desktop\erase-me\oscam.server','w')
for i in read:
    ffii.write(i)
ffii.close()
a1=os.popen('curl -s -d "user="anaana"&pass="anaana"" -X POST http://infosat.satunivers.tv/mg/')
import time
time.sleep(2.4)
aa1=a1.read()
mghost1=re.findall('host: (.*?)<',aa1)[0].strip()
mgport1=re.findall('port: (.*?)<',aa1)[0].strip()
mguser1=re.findall('user: (.*?)<',aa1)[0].strip()
mgpass1=re.findall('pass: (.*?)<',aa1)[0].strip()
ffii1=open('C:\Users\HERE\Desktop\erase-me\oscam.server','r')
read1=ffii1.readlines()
ffii1.close()
for i in range(len(read1)):
    if 'infosat.satunivers.tv,24000' in read1[i]:
        break

read1[i]='device                        = '+mghost+','+mgport+'\n'
read1[i+2]='user                          = '+mguser+'\n'
read1[i+3]='password                      = '+mgpass+'\n'

ffii1=open('C:\Users\HERE\Desktop\erase-me\oscam.server','w')
for i in read1:
    ffii1.write(i)
ffii1.close()
