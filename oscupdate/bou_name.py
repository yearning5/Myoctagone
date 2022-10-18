
iplist=raw_input('bouquet name ==  ')
user=raw_input('please provide new user ==  ')
passs=raw_input('please provide new pass ==  ')
o=open(r'/etc/enigma2/userbouquet.'+str(iplist)+'__tv_.tv')
oo=o.readlines()
o.close()

oo1=[]
for i in oo:
    if '#SERVICE' in i:
        i=i.replace(i.split('/')[-3],str(user))
        i=i.replace(i.split('/')[-2],str(passs))
    oo1.append(i)

o=open(r'/etc/enigma2/userbouquet.'+str(iplist)+'__tv_.tv','w')
for i in oo1:
    o.write(i)
o.close()
