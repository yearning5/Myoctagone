
import requests, random, string,os


userr='7274674'
s1=open('/etc/enigma2/iptosat.json','r')
ff1=s1.read()
s1.close()
a1=ff1.find("http://freeiptvgen.com:25461/")
a2=ff1[a1+29:].find("/")
a3=ff1[a1+29:a1+29+a2]
print 'old user : '+a3
s2=open('/etc/enigma2/iptosat.json','w')
s2.write(ff1.replace(a3,userr))   
s2.close()
a=os.popen('wget -qO - http://127.0.0.1/web/servicelistreload?mode=2')
print a.read()

with open('/tmp/freeiptvgen.txt','w') as f:
    f.write(dsf[0]+'\n')
    f.write(dsf[1]+'\n')
