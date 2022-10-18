#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
	bou1=raw_input('enter bouquet name: \n" thgss "= 1\n" vtpii "=2\n" Alkaicer "=3\n')
	if bou1=='3':
		bou='userbouquet.Alkaicer__tv_.tv'
	elif bou1=='2':
		bou='userbouquet.vtpii__tv_.tv'
	elif bou1=='1':
		bou='userbouquet.things__tv_.tv'
	print ('     ') 	
	u2=raw_input("enter the new username: ")
	print ('     ')   
	p2=raw_input("enter the new password: ")
	print ('     ') 
else:
	bou1=raw_input('enter bouquet name: \n" thgss "= 1\n" vtpii "=2\n" Alkaicer "=3\n')
	if bou1=='3':
		bou='userbouquet.Alkaicer__tv_.tv'
	elif bou1=='2':
		bou='userbouquet.vtpii__tv_.tv'
	elif bou1=='1':
		bou='userbouquet.things__tv_.tv'
	print ('     ') 	
	u2=input("enter the new username: ")
	print ('     ')   
	p2=input("enter the new password: ")
	print ('     ') 

print (bou)      
with open (r'/etc/enigma2/'+bou) as f:
    ff=f.readlines()

with open (r'/etc/enigma2/'+bou) as f:
    ff1=f.read()

for i in ff:
    if len(i.split('/'))>=6:
        break
print (i)  
u1=i.split('/')[-3]
p1=i.split('/')[-2]
print (u1)
print (p1)
with open(r'/etc/enigma2/'+bou,'w') as f:
    f.write(ff1.replace(u1,u2).replace(p1,p2))
import os
os.popen('wget -qO - http://127.0.0.1/web/servicelistreload?mode=2')