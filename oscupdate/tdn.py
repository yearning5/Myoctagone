import os

o=open(r'/etc/enigma2/userbouquet.teledunet__tv_.tv','r')
oo=o.readlines()
o.close()
a=int(input('Input channel number :  '))
b=int(input('Input channel pass :  '))


ds=[]
for i in oo:
    try:
        ds.append(i.replace(i.split('/')[-2]+'/'+i.split('/')[-1],str(int(i.split('/')[-1].split('.')[0])-a+b)+'/'+i.split('/')[-1]))
    except:
        ds.append(i)

F=open(r'/etc/enigma2/userbouquet.teledunet__tv_.tv','w')
for i in ds:
    F.write(i)
F.close()