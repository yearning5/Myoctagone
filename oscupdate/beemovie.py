import os 

o=os.popen('curl -s https://iptv-org.github.io/iptv/index.country.m3u').read()

oo=o.split('\n')
for i,s in enumerate(oo):
    if 'bee movie' in s.lower() and 'linkastream'  in oo[i+1].lower():
        c1 = oo[i+1]
    elif 'bee thea' in s.lower() and 'linkastream'  in oo[i+1].lower():
        #*print s
        #print oo[i+1]
        c2 = oo[i+1]

f=open('/etc/enigma2/userbouquet.nilesat__tv_.tv','r')
ff=f.readlines()
f.close()
for i,s in enumerate(ff):
    if 'bee movie' in s.lower():
        break
ff[i]=ff[i].replace(ff[i].split(':')[-2],c1.replace(':','%3a'))

for i,s in enumerate(ff):
    if 'bee thea' in s.lower():
        break
ff[i]=ff[i].replace(ff[i].split(':')[-2],c2.replace(':','%3a'))
f=open('/etc/enigma2/userbouquet.nilesat__tv_.tv','w')
for i in ff:
    f.write(i)
f.close()

