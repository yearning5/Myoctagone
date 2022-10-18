import os

#filename=raw_input('please provide the opvpn file name : \n')
filename='01-opengw.net_udp_1195.ovpn'
chkkern = os.popen('uname -r').read().strip('\n')
'''try:
    os.system('opkg install kernel-module-tun-' + chkkern)
    os.system('opkg install kernel-module-tun')
    os.system('opkg install enigma2-plugin-utilities-openvpn')
except:
    pass'''


try:
    os.system('modprobe tun')
    os.popen('killall -9 openvpn')
    #print '\nYour ip is\n'
    os.system('/oscupdate/getip.sh')
    print '\nTrying to put on your server please check your ip\nRun\n/oscupdate/getip.sh\n'
    os.system('openvpn --config /etc/openvpn/'+str(filename)+' --daemon')

except:
    print ' no thing is done'
