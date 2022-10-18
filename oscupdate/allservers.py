import subprocess
image_v=subprocess.check_output('grep "."  /etc/issue | tail -1',shell=True)[:-6]

f=open('/tmp/allservers.txt','r')
a=f.readlines()
f.close()

servers=[i.split() for i in a]

if 'pkt' in image_v.lower():
    source='/var/keys/oscam.server'
    source_wic='/var/keys/wicardd.conf'
    pkt_cp='cp /var/keys/oscam.server /var/keys/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /var/keys/oscam.server /var/keys/gcam.server > /dev/null 2>&1'

elif 'vix' in image_v.lower():
    source='/etc/tuxbox/config/oscam.server'
    source_wic='/etc/tuxbox/config/wicardd.conf'
    pkt_cp='cp /etc/tuxbox/config/oscam.server /etc/tuxbox/config/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /etc/tuxbox/config/oscam.server /etc/tuxbox/config/gcam.server > /dev/null 2>&1'
else:
    source='/etc/tuxbox/oscam-emu/oscam.server'
    source_wic='/etc/tuxbox/config/wicardd.conf'
    pkt_cp='cp /etc/tuxbox/oscam-emu/oscam.server /etc/tuxbox/config/ncam.server > /dev/null 2>&1'
    pkt_cp1='cp /etc/tuxbox/oscam-emu/oscam.server /etc/tuxbox/config/gcam.server > /dev/null 2>&1'


the_pag=open(source,'r')
the_page =the_pag.readlines()
the_pag.close()
the_pag=open(source,'a')




jn=0
for j in servers:
    jn=jn+1
    try:
        host=j[0]
        port=j[1]
        user=j[2]
        pasw=j[3]
        #exxcept_art=['135.181.78.48','88.99.91.253','5.189.161.183','195.154.200.18','135.181.136.120','95.216.112.104','62.171.129.84','49.12.129.210','168.119.39.46','85.203.33.242','62.171.181.10','95.217.192.171','62.171.131.113','164.132.53.24','5.189.134.13','207.180.206.80','54.38.5.104','178.238.236.25','176.31.156.44','213.136.94.35','167.86.119.185','185.22.173.58','5.135.75.42','5.189.156.56','178.238.232.233','116.202.196.126','178.128.200.245','51.77.220.127','37.59.80.83','94.130.220.50','94.130.199.50','144.91.117.213','178.63.69.157']
        #exxcept_moviestar=['164.132.53.24','62.171.131.113','49.12.129.210','185.22.173.58','5.189.161.183','173.249.17.127']
        #exxcept_skyde=['185.22.173.58']
        #exxcept_thor=['185.22.173.58','213.32.93.193']
        #exxcept_osn=['135.181.78.48','151.80.62.94','135.181.134.21','88.99.91.253','95.217.192.171','49.12.129.204','80.211.8.149','168.119.38.151','168.119.10.43','49.12.129.205','49.12.129.202','95.217.200.25','49.12.129.210','5.189.161.183','135.181.78.47','168.119.39.46','136.243.129.249','49.12.129.203']
        #exxcept_tnt=['54.38.93.53','168.119.39.46','164.132.53.24','144.91.115.78','135.181.136.120','94.176.232.235','173.212.234.202','168.119.10.43','78.46.68.145','95.217.192.171','62.171.181.141','95.111.247.147','144.91.81.136','144.91.121.8','62.171.140.28','173.249.13.170']
        exxcept_art=['95.217.200.25:8801','195.154.200.18:8403','147.135.169.166:13000']
        exxcept_moviestar=['51.91.252.58:14511','147.135.169.166:13000','5.189.161.183:50000','161.97.76.252:14404','144.91.124.239:5200','94.23.97.10,22000', \
        ]
        exxcept_skyde=['147.135.169.166,13000']
        exxcept_thor=['161.97.76.252,14404','147.135.169.166,13000','37.187.161.201,1003','94.23.97.10,24000','51.91.252.58,14511','49.12.126.182,11000', \
        ]
        exxcept_osn=['95.217.200.25:8800','95.217.192.171:8801','49.12.129.210:8800','49.12.129.210:8801','168.119.39.46:18803','136.243.129.249:8802', \
        '168.119.10.43:8807','168.119.10.42:18804','168.119.10.42:8800','95.217.200.25:8801','95.217.200.25:8806','49.12.129.210:8803','49.12.126.182:51002', \
        '49.12.126.182:20001','147.135.169.166,13000']
        exxcept_tnt=['147.135.169.166,13000','161.97.76.252,14404']
        jj=j[4]
        def aawrt(jn,jj,host,port,user,pasw):
            art=''
            mov=''
            sk=''
            thr=''
            osn=''
            tnt=''
            if any(host+':'+port in i or host+','+port in i for i in exxcept_art):
               art='!ART'
            if any(host+':'+port in i or host+','+port in i for i in exxcept_moviestar):
               mov='!moviestar'
            if any(host+':'+port in i or host+','+port in i for i in exxcept_skyde):
               sk='!sky_ger'
            if any(host+':'+port in i or host+','+port in i for i in exxcept_thor):
                thr='!thor'
            if any(host+':'+port in i or host+','+port in i for i in exxcept_osn):
                osn='!osn'
            if any(host+':'+port in i or host+','+port in i for i in exxcept_tnt):
                tnt='!tnt'
            sers=[art,mov,sk,thr,osn,tnt]
            if any(x=='' for x in sers) and not all(x=='' for x in sers):

                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+jj + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = '+','.join(i for i in sers if i!='')+'\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            elif  all(x=='' for x in sers):
                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+jj + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            else:
                print j ,' blocked'
                wrte=''
            return wrte

        '''if any(host in i for i in exxcept_art):
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            if any(host in i for i in exxcept_moviestar):
                wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART,!moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        elif any(host in i for i in exxcept_moviestar):
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
            if any(host in i for i in exxcept_art):
                 wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\nservices                      = !ART,!moviestar\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        else:
            wrte='\n\n[reader]\nlabel= '+str(jn)+'_'+j[4] + '\nprotocol= cccam\ndevice= ' + host + ',' + port + '\nuser= ' + user + '\npassword= ' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 1811:003311,003315;1708:000000;1709:000000;09C4:000000;098C:000000;098D:000000;0500:043300,030B00,042820,042800,043800,041950;0500:050F00;0E00:000000;1861:000000\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\nemmcache= 1,1,2,1\ndropbadcws= 1'
        #the_pag.write(wrte)'''
        aawrt1=aawrt(jn,jj,host,port,user,pasw)
        if  aawrt1!='':
            the_pag.write(aawrt1)
    except IndexError:
        pass
the_pag.close()
