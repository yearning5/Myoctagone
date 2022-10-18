iptv=raw_input('"best 1" "buy 2" "Malt 3" "forest 4"  "soft 5" "ipmag 6" "ccam.ch 7"  =')

user=raw_input('please Username  = ')
passs=raw_input('please Password  = ')

if iptv=='1':
    file=open('/etc/enigma2/userbouquet.bestbuyiptv__tv_.tv','r')
elif iptv=='2':
    file=open('/etc/enigma2/userbouquet.buyiptv__tv_.tv','r')
elif iptv=='3':
    file=open('/etc/enigma2/userbouquet.Maltaipv__tv_.tv','r')
elif iptv=='4':
    file=open('/etc/enigma2/userbouquet.Iptvforest__tv_.tv','r')
elif iptv=='5':
    file=open('/etc/enigma2/userbouquet.SOFTIPTV__tv_.tv','r')
elif iptv=='6':
    file=open('/etc/enigma2/userbouquet.ipmagtv__tv_.tv','r')
elif iptv=='7':
    file=open('/etc/enigma2/userbouquet.janberyan__tv_.tv','r')
lines=file.readlines()
file.close()

new=[]
new.append(lines[0])
i=1
while i<len(lines):
    if iptv=='1' or iptv=='3' or iptv=='4' or iptv=='5' or iptv=='7':
        a=lines[i].replace(lines[i].split('/')[3],user)
        b=a.replace(a.split('/')[4],passs)
    elif iptv=='2' or iptv=='6':
        a=lines[i].replace(lines[i].split('/')[4],user)
        b=a.replace(a.split('/')[5],passs)
    new.append(b)
    new.append(lines[i+1])
    i = i+2

if iptv=='1':
    filee=open('/etc/enigma2/userbouquet.bestbuyiptv__tv_.tv','w')
elif iptv=='2':
    filee=open('/etc/enigma2/userbouquet.buyiptv__tv_.tv','w')
elif iptv=='3':
    filee=open('/etc/enigma2/userbouquet.Maltaipv__tv_.tv','w')
elif iptv=='4':
    filee=open('/etc/enigma2/userbouquet.Iptvforest__tv_.tv','w')
elif iptv=='5':
    filee=open('/etc/enigma2/userbouquet.SOFTIPTV__tv_.tv','w')
elif iptv=='6':
    filee=open('/etc/enigma2/userbouquet.ipmagtv__tv_.tv','w')
elif iptv=='7':
    filee=open('/etc/enigma2/userbouquet.janberyan__tv_.tv','w')

for  aa in new:
    filee.write(aa)

filee.close()
