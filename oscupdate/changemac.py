import random, os
perm=os.popen('ethtool -P eth0').read()
print ('============ "_" =============')
print (' ')
print( "The Permanent MAC Address is : \n"+perm)
print (' ')
print ('============ "_" =============')
print (' ')
Maclist = []
p2="".join(random.sample("02468",1))
p1="".join(random.sample("0123456789abcdef",1))
Maclist.append(p1+p2)
for i in range(1,6):
    RANDSTR = "".join(random.sample("0123456789abcdef",2))
    Maclist.append(RANDSTR)
RANDMAC = ":".join(Maclist)
print( "The generated MAC Address is : "+RANDMAC)

os.popen('ip link set eth0 address '+RANDMAC)

newmac=os.popen('cat /sys/class/net/eth0/address').read()

print("The new MAC Address is : "+newmac)