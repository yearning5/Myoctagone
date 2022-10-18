import os, subprocess,urllib2
import re,random,string

'''
p=open('/etc/image-version','r')
pp=p.readlines()
p.close()
for i in pp:
    if 'creator' in i.lower():
        image_v=i.split('=')[1]
'''
image_v=subprocess.check_output('grep "."  /etc/issue | tail -1',shell=True)[:-6]
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

def socks2():
    d=subprocess.check_output('curl -s https://www.socks-proxy.net/',shell=True)
    dd=re.findall('tbody(.*?)tbody',d)
    ddd=re.findall('tr(.*?)tr',dd[0])
    dddd=[re.findall('<td>(.*?)</td>',i) for i in ddd]
    d1=[i[0]+':'+i[1] for i in dddd if i !=[]]
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --socks4 '+i+' --max-time 3 http://ipecho.net/plain').read()
            if a:
                lisst.append(i)
                break
        except:
            pass
        #print i
    return i

def socks_4():
    d=subprocess.check_output('curl -s https://proxyscrape.com/free-proxy-list',shell=True)
    req4=re.findall('href="(.*?)" id="downloadiconsocks4',d)[0]
    req4=req4.replace('timeout=10000','timeout=5000')
    the_files=urllib2.urlopen(req4).read()
    d1=the_files.split()
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --max-time 3 --socks4 '+i+' ip-api.com/json').read()
            if a:
                c=eval(a)['country']
                ip=eval(a)['query']
                lisst.append(i)
                break
        except:
            pass
        #print i
    return [i,ip,c]


# ======    Message on screen =========================================================================

message_script=os.system('wget -O /dev/null -q "http://localhost/web/message?text= \nOscupdate First part script by GUIRA is Running ......&type=2&timeout=6"')

#======================================================================================================

#activation servsat
try:
    try:
        acct=subprocess.check_output('curl -s --max-time 5 "http://www.serversat.net/cccam.php" --data "author=anaana"', shell=True)
    except:
        ecct=os.popen('curl -s --max-time 5 "http://www.serversat.net/cccam.php" --data "author=anaana"')
except:
    pass
#print "servsat updated"
#activation servsat MGCAMD
try:
    try:
        acct=subprocess.check_output('curl -s --max-time 5 "http://www.serversat.net/mgcamd.php" --data "author=anaana"', shell=True)
    except:
        acct=os.popen('curl -s --max-time 5 "http://www.serversat.net/mgcamd.php" --data "author=anaana"')
except:
    pass

#print "servsat MG updated"

#activation tounfite
try:
    user1=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    user2=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
    try:
        a11=subprocess.check_output('curl -s --cookie-jar - "http://tounfite.ddns.net/iptvsmarttv.php" --data-raw "username='+user1+'&password='+user2+'"',shell=True)
    except:
        a11=os.popen('curl -s --cookie-jar - "http://tounfite.ddns.net/iptvsmarttv.php" --data-raw "username='+user1+'&password='+user2+'"').read()
    #activation
    link='http://tounfite.ddns.net/'+a11[a11[:a11.find('Afficher')].rfind('href="'):a11.find('Afficher')].split('"')[1]
    coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
    cmd='curl -s '+link+' -H "Cookie: PHPSESSID='+coki+'"'
    a12=subprocess.check_output(cmd,shell=True)
    #activation algsat mgcamd
    ffii=open(source,'r')
    read=ffii.readlines()
    ffii.close()
    for i in range(len(read)):
        if all(x in read[i] for x in ['label','tounfite']):
            read[i+4]='user                          = '+user1+'\n'
            read[i+5]='password                      = '+user2+'\n'
            break
    ffii=open(source,'w')
    for i in read:
        ffii.write(i)
    ffii.close()
except:
    pass
#activation algsat mgcamd

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    try:
        a11=subprocess.check_output('curl -s -m 5 --cookie-jar - "http://algsat.ddns.net/" --data-raw "Username='+user+'&Username='+user+'&addf1="', shell=True)
        coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
        b=subprocess.check_output('curl -s "http://algsat.ddns.net/mgcamd.php" -H "Cookie: PHPSESSID='+coki+'" --data-raw "Username='+user+'&Username='+user+'&addf1="', shell=True)
    except:
        a11=os.popen('curl -s -m 5 --cookie-jar - "http://algsat.ddns.net/" --data-raw "Username='+user+'&Username='+user+'&addf1="').read()
        coki=a11[a11.find('PHPSESSID'):len(a11)].replace('\t','').replace('\n','').replace('PHPSESSID','')
        b=os.popen('curl -s "http://algsat.ddns.net/mgcamd.php" -H "Cookie: PHPSESSID='+coki+'" --data-raw "Username='+user+'&Username='+user+'&addf1="').read()
    ho=re.findall('N: (.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','algsat']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

#print "algsat MG updated"

# kcccam

try:
    ip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()
    try:
        a=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" --data "protocol=mgcam&server=f3.kcccam.com&vehicle1=agree"', shell=True)
        a1=subprocess.check_output('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" -H "cookie: already='+ip+'"&', shell=True)
        b=a1
    except:
        a=os.popen('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" --data "protocol=mgcam&server=f3.kcccam.com&vehicle1=agree"')
        a1=os.popen('curl -s --max-time 5 "https://testcline.com/cccam_reseller_panel_free.php" -H "cookie: already='+ip+'"&').read()
        b=a1
    ho=re.findall('CWS(.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[1]
    port= ho[2]
    user= ho[3]
    Pass= ho[4]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','kcccam']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+5]='user                          = '+user+'\n'
                read[i+6]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

try:
    ip = os.popen('curl -L --max-time 3 http://ipecho.net/plain').read().strip()
    try:
        a=subprocess.check_output('curl "https://cccamcard.com/free-cccam-server.php" --data-raw "protocol=mgcam&server=f3.cccamcard.com&vehicle1=agree"',shell=True)
        a1=subprocess.check_output('curl "https://cccamcard.com/free-cccam-server.php" -H "cookie: TawkConnectionTime=0; already='+ip+'"',shell=True)
        b=a1
    except:
        a=os.popen('curl "https://cccamcard.com/free-cccam-server.php" --data-raw "protocol=mgcam&server=f3.cccamcard.com&vehicle1=agree"')
        a1=os.popen('curl "https://cccamcard.com/free-cccam-server.php" -H "cookie: TawkConnectionTime=0; already='+ip+'"').read()
        b=a1
    ho=re.findall('CWS(.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[1]
    port= ho[2]
    user= ho[3]
    Pass= ho[4]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','MG_cccamcard']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+5]='user                          = '+user+'\n'
                read[i+6]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

#print "algsat MG2 updated"


# infosat MgCAMD2

try:
    try:
        aa=subprocess.check_output('curl -s --max-time 5 "http://infosat.satunivers.tv/mgfr/" --data "user=anaana&pass=anaana"', shell=True)
    except:
        aa=os.popen('curl -s --max-time 5 "http://infosat.satunivers.tv/mgfr/" --data "user=anaana&pass=anaana"').read()
    mghost=re.findall('host: (.*?)<',aa)[0].strip()
    mgport=re.findall('port: (.*?)<',aa)[0].strip()
    mguser=re.findall('user: (.*?)<',aa)[0].strip()
    mgpass=re.findall('pass: (.*?)<',aa)[0].strip()
    a=[mghost,mgport,mguser,mgpass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if 'infosat.satunivers.tv,30000' in read[i]:
                read[i]='device                        = '+mghost+','+mgport+'\n'
                read[i+2]='user                          = '+mguser+'\n'
                read[i+3]='password                      = '+mgpass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass
#print "infosat MG2 updated"
# infosat MgCAMD1
try:
    try:
        aa1=subprocess.check_output('curl -s --max-time 5 "http://infosat.satunivers.tv/mg/" --data "user=anaana&pass=anaana"', shell=True)
    except:
        aa1=os.popen('curl -s --max-time 5 "http://infosat.satunivers.tv/mg/" --data "user=anaana&pass=anaana"').read()
    mghost1=re.findall('host.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mgport1=re.findall('port.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mguser1=re.findall('user.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    mgpass1=re.findall('pass.*?:.*?(.*?)<',aa1,re.IGNORECASE)[0].strip()
    a=[mghost1,mgport1,mguser1,mgpass1]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read1=ffii.readlines()
        ffii.close()
        for j in range(len(read1)):
            if 'infosat.satunivers.tv,24000' in read1[j]:
                read1[j]='device                        = '+mghost1+','+mgport1+'\n'
                read1[j+2]='user                          = '+mguser1+'\n'
                read1[j+3]='password                      = '+mgpass1+'\n'
                break
        ffii=open(source,'w')
        for i in read1:
            ffii.write(i)
        ffii.close()
except:
    pass
#print "infosat MG1 updated"
try:
    try:
        aa=subprocess.check_output('curl -L -s "http://server.satunivers.tv/gc/cg.php" --data-raw "user=anaana&pass=dzpros-forum&secret==<? echo $secret; ?>"', shell=True)
    except:
        aa=os.popen('curl -L -s "http://server.satunivers.tv/gc/cg.php" --data-raw "user=anaana&pass=dzpros-forum&secret==<? echo $secret; ?>"').read()
    aaa=re.findall('c: (.*?)<',aa,re.IGNORECASE)
    for i in aaa:
        if len(i.split())==4 and i.split()[1].isdigit():
            break
        else:
            1/0
    a=i.split()
    mhost=a[0]
    mport=a[1]
    muser=a[2]
    mpass=a[3]
    a=[mhost,mport,muser,mpass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if 'infosat_cccam' in read[i]:
                read[i+2]='device                        = '+mhost+','+mport+'\n'
                read[i+3]='user                          = '+muser+'\n'
                read[i+4]='password                      = '+mpass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

#print "infosat cccam updated"

#   OSN

try:
    #user='85469512'
    user=''.join(random.choice(string.digits) for _ in range(8))
    #cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="'
    d=open('/tmp/excution.txt','w')
    d.close()
    socc=socks_4()
    #print 'saqr1',socc
    try:
        b=subprocess.check_output('curl -L -s --max-time 10 --socks4 '+socc[0]+' "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="',shell=True)
    except:
        b=os.popen('curl -L -s --max-time 10 --socks4 '+socc[0]+' "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="').read()
    #b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #print 'saqr',socc
    d=open('/tmp/excution.txt','w')
    d.write('the socks used for saqr is: '+socc[0]+' from '+socc[2]+' \n')
    d.close()
    host= re.findall('host.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    port= re.findall('port.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    Pass= re.findall('pass.*?:.*?(.*?)<',b,re.IGNORECASE)[0].strip(' ')
    a=[host,port,user,Pass]
    #print a
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','saqr_Mgcam']):
                read[i+5]='user                          = '+user+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()

except:
    pass
#topservercccam

try:
    #user='85469512'
    user=''.join(random.choice(string.digits) for _ in range(5))
    #cmd='curl -s --max-time 5 "http://saqr.ml/Mgcam/"  --data "Username='+user+'&&cline="'
    bb=socks_4()
    #print 'speeds1',bb
    try:
        a=subprocess.check_output('curl -s -L --max-time 12 --socks4 '+bb[0]+' "https://free.speeds.tv/mgcamd/index.php"  --data-raw "user='+user+'&pass=topservercccam"',shell=True)
    except:
        a=os.popen('curl -s -L --max-time 12 --socks4 '+bb[0]+' "https://free.speeds.tv/mgcamd/index.php"  --data-raw "user='+user+'&pass=topservercccam"').read()
    #b=subprocess.check_output(cmd, shell=True)
    #a1=os.popen(cmd)
    #b=a1.read()
    #print 'speeds',bb
    d=open('/tmp/excution.txt','a')
    d.write('the socks used for topservercccam is: '+bb[0]+' from '+bb[2]+' \n')
    d.close()
    if 'already have a line' in a:
        host= 'free.speeds.tv'
        port= '47579'
        Pass= 'topservercccam'
        a2=[host,port,user,Pass]
    else:
        host= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[0]
        port= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[1]
        Pass= re.findall('N: (.*?)<',a,re.IGNORECASE)[0].split(' ')[3]
        a3=[host,port,user,Pass]
    #print a
    if all(i!='' for i in a2):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','MG_free.speeds']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()

except:
    pass


# urliptv

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    try:
        b=subprocess.check_output('curl -s --max-time 5 "https://urliptv.com/CCcam/" --data "Username='+user+'&cline="', shell=True)
    except:
        b=subprocess.check_output('curl -s --max-time 5 "https://urliptv.com/CCcam/" --data "Username='+user+'&cline="').reaad()
    ho=re.findall('c: (.*?)<',b,re.IGNORECASE)[0].split()
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','urliptv']):
                read[i+3]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

# firecccam

try:
    user=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    cmd='curl -s --max-time 5 "http://firecccam.com/mgcamd02.php"  --data "Username='+user+'&Password='+user+'&Email='+user+'@yahoo.com^&addf="'
    try:
        b=subprocess.check_output(cmd, shell=True)
    except:
        b=os.popen(cmd).read()
    try:
        ho=re.findall('n: (.*?)<',b,re.IGNORECASE)[1].split()
    except:
        ho=re.findall('n: (.*?)<',b,re.IGNORECASE)[0].split()

    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','firecccam']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+4]='user                          = '+user+'\n'
                read[i+5]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass

try:
    cmd='curl -s "https://www.realcccam.com/index.php" --data-raw "addf=addf"'
    try:
        a1=subprocess.check_output(cmd, shell=True)
    except:
        a1=os.popen(cmd).read()
    ho=re.findall('c: (.*?)[<:\n]',a1,re.IGNORECASE)[0].split(' ')
    host= ho[0]
    port= ho[1]
    user= ho[2]
    Pass= ho[3]
    a=[host,port,user,Pass]
    if all(i!='' for i in a):
        ffii=open(source,'r')
        read=ffii.readlines()
        ffii.close()
        for i in range(len(read)):
            if all(x in read[i] for x in ['label','realcccam']):
                read[i+2]='device                        = '+host+','+port+'\n'
                read[i+3]='user                          = '+user+'\n'
                read[i+4]='password                      = '+Pass+'\n'
                break
        ffii=open(source,'w')
        for i in read:
            ffii.write(i)
        ffii.close()
except:
    pass


print '......................... ARE ALL DONE .......................................'
