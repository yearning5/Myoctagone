import requests,re,os
import datetime
import time
import urllib3
import random
urllib3.disable_warnings()

UserAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; Linux x86_64; Linux x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Safari/537.36',
            'Accept': 'text/html'}

import sys

PY3=sys.version_info[0]

try:
    cookies = {
        'PHPSESSID': '702b9f9rhgajh3jctj85opvs4h',
        '_ga': 'GA1.2.234181906.1625343291',
        '_gid': 'GA1.2.2139269596.1625343291',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://iptv.journalsat.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://iptv.journalsat.com/login.php',
        'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6,ar;q=0.5',
    }

    data = {
      'username': 'yearning55',
      'password': 'yearning55',
      'submit': ''
    }

    r = requests.post('http://iptv.journalsat.com/login.php', headers=headers, cookies=cookies, data=data, verify=False)
    if PY3==3:
        r=r.text
    else:
        r=r.text.encode('ascii','ignore')

    if 'off' in re.findall(r'float-right badge badge(.*?)<',r)[0].lower():
        print( re.findall(r'float-right badge badge(.*?)<',r)[0])
        print( 'Your server is OFF and will be activated using  \nuser : yearning55\n passwoerd : yearning55\n m3u user = 939810687')
        cookies = {
                'PHPSESSID': '702b9f9rhgajh3jctj85opvs4h',
                '_ga': 'GA1.2.234181906.1625343291',
                '_gid': 'GA1.2.2139269596.1625343291',
        }

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://iptv.journalsat.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://iptv.journalsat.com/users.php',
            'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6,ar;q=0.5',
        }

        data = {
          'user': '939810687',
          'submit': ''
        }

        r1 = requests.post('http://iptv.journalsat.com/activate.php', headers=headers, cookies=cookies, data=data, verify=False).text.encode('ascii','ignore')
        with open(r'C:\Users\HERE\Desktop\erase-me\userbouquet.journalsat__tv_.tv','r') as f:
            ff=f.read()

        u1=re.findall('25461/(.*?)/',ff)[0]
        with open(r'C:\Users\HERE\Desktop\erase-me\userbouquet.journalsat__tv_.tv','w') as f:
            f.write(ff.replace(u1,'939810687'))
    else:
        print (re.findall(r'float-right badge badge(.*?)<',r)[0])
        if 'on' in re.findall(r'float-right badge badge(.*?)<',r)[0].lower():
            print ('Your server is ON and activated using  \nuser : yearning55\n passwoerd : yearning55\n m3u user = 939810687')

        with open(r'C:\Users\HERE\Desktop\erase-me\userbouquet.journalsat__tv_.tv','r') as f:
            ff=f.read()

        u1=re.findall('25461/(.*?)/',ff)[0]
        with open(r'C:\Users\HERE\Desktop\erase-me\userbouquet.journalsat__tv_.tv','w') as f:
            f.write(ff.replace(u1,'939810687'))


    with open('/tmp/Journalsat.txt','w') as f:
        f.write(re.findall(r'float-right badge badge(.*?)<',r)[0]+'\n')
        f.write('Your server is ON and activated using  \nuser : yearning55\n passwoerd : yearning55\n m3u user = 939810687')
except:

    # http://101k.tk/
    #username='57901537460525'
    #password='57901537460525'
    def uri_validator(x):
        try:
            result = requests.get(x,headers=UserAgent,timeout=4.0,verify=False)
            if result.ok:
                return True
            else:
                return False
        except:
            return False

    #iptt=raw_input('which iptv to generate\n"thgss"=1\n"vtpii"=2\n"Alkaicer"=3\n"journalsat"=4\n   ')
    #stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')

    #iptt='4'
    stream='5001'

    srr=['4097','5001','5002','']
    if stream not in srr:
        print ('please enter number from 4097 5001 or 5002\n')
        stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
        if stream not in srr:
            print( "you didn't enter number from 4097 5001 or 5002 the program will exit\n")
            sys.exit()
    now=datetime.datetime.now()

    def iptt():
        name='journalsat'
        cookies = {
            '_ga': 'GA1.2.1444096135.1619435351',
            '_gid': 'GA1.2.1100187472.1619435351',
            '__gads': 'ID=66193be367562bbf-22b36877ada700fc:T=1619435385:RT=1619435385:S=ALNI_MYTUMnvVlJ2xeofoVZY3j9RfJJc3A',
            '_gat_gtag_UA_131846294_1': '1',
            'FCCDCF': '[null,null,["[[],[],[],[],null,null,true]",1619435418969],null,null]',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://iptv.journalsat.com',
            'Connection': 'keep-alive',
            'Referer': 'http://iptv.journalsat.com/',
            'Upgrade-Insecure-Requests': '1',
        }

        r1 = requests.post('http://iptv.journalsat.com/index.php', headers=headers, cookies=cookies)



        cookies = {
            '_ga': 'GA1.2.884653929.1619435494',
            '_gid': 'GA1.2.1063229768.1619435494',
        }

        headers = {
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '0',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://iptv.journalsat.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://iptv.journalsat.com/index.php',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        r2 = requests.post('http://iptv.journalsat.com/index.php', headers=headers, cookies=cookies, verify=False)

        #import random
        #a=str(random.randint(100000000, 999999999))
        cookies = {
            '_ga': 'GA1.2.884653929.1619435494',
            '_gid': 'GA1.2.1063229768.1619435494',
            'uername': ID,
        }

        headers = {
            'Proxy-Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://iptv.journalsat.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://iptv.journalsat.com/get.php',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = (
            ('do', 'cccam'),
        )

        data = {
          'do': 'cccam',
          'doccam': 'generate'
        }

        r3 = requests.post('http://iptv.journalsat.com/get.php', headers=headers, params=params, cookies=cookies, data=data, verify=False)
        if PY3==3:
            r3=r3.content.decode()
        else:
            r3=r3.text.encode('ascii','ignore')

        host=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[0]
        username=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[1]
        password=re.findall('"text-white">(.*?)<',r3,re.DOTALL)[2]
        liin=re.findall(' href=\'(http://iptv.*?)\'',r3,re.DOTALL)[0]
        print (liin)
        with open('/tmp/journalsat_link.txt','w') as f12:
            f12.write(liin)
        print( 'journalsat_link file written')
        try:
            with  open('/etc/enigma2/xstreamity/playlists.txt','r') as f:
                ff=f.read()
            u1=re.findall('http://iptv.journalsat.com:25461/get.php.*?username=(.*?)&pa',ff)[0]
            newff=ff.replace('http://iptv.journalsat.com:25461/get.php?username='+u1,'http://iptv.journalsat.com:25461/get.php?username='+ID)
            with  open('/etc/enigma2/xstreamity/playlists.txt','w') as f:
                f.write(newff)
        except:
            pass
        for i in range(10):
            f=requests.get(liin,headers=UserAgent)
            if PY3==3:
                ttx=f.content.decode().split('\r')
            else:
                ttx=f.text.encode('ascii', 'ignore').split('\r')
            if ttx != ['']:
                print ("  Donne After "+str(i+1)+"  iterations")
                break

        #print ttx

        #bouquets
        bouq=open('/etc/enigma2/bouquets.tv','r')
        bo=bouq.read()
        bouq.close()
        if name not in bo:
            new='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+name+'__tv_.tv" ORDER BY bouquet\n'
            file=open('/etc/enigma2/bouquets.tv','a')
            file.write(new)
            file.close()

        locatf='/tmp/new_'+name+'.m3u'

        d=open(locatf,'w')
        for i in ttx:
            print (i)
            d.write(i)
        d.close()

        m3ufl = open(locatf,'r')
        m3uf = m3ufl.readlines()
        m3ufl.close
        m3ufl = open(locatf,'w')
        for line in m3uf:
            if line.strip():
                if '#EXTVLCOPT' not in line:
                    m3ufl.write(line)
        m3ufl.close
        m3ufl = open(locatf,'r')
        m3uf = m3ufl.readlines()
        m3ufl.close()
        # the first line containing channel name
        for i in range(len(m3uf)):
            if m3uf[i].find('EXTINF')>-1:
                count=i
                break
        if os.path.isfile('/etc/enigma2/userbouquet.'+name+'__tv_.tv'):
            os.remove('/etc/enigma2/userbouquet.'+name+'__tv_.tv')
            file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
            file.close()
        file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
        file.write('#NAME '+name+' (TV)\n')
        while i <len(m3uf)-1:
                channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                a1=m3uf[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:0:'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
        file.close()
        with open(r'/oscupdate/journalsat_check.txt','w') as f:
            f.write(str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+'\n'+ID)
        return


    if not os.path.exists(r'/oscupdate/journalsat_check.txt'):
        ID=str(random.randint(100000000, 999999999))
        print( ' a new  ID will be Used '+ID)
        a1 =iptt()
    else:
        with open(r'/oscupdate/journalsat_check.txt','r') as f:
            aaa=f.readlines()
            aa=aaa[0].split(':')
        dif=((now.year-float(aa[0]))* (365*24*60*60)+(now.month-float(aa[1]))* (730*60*60)+(now.day-float(aa[2]))* (24*60*60)+(now.hour-float(aa[3]))* (60*60)+(now.minute-float(aa[4]))* (60)+now.second-float(aa[5]))/3600
        print( 'Actual ID is '+aaa[1]+' === "_" === ')
        if dif > 6:
            ID=str(random.randint(100000000, 999999999))
            print( ' MORE than 6 Hours a new  ID will be Used '+ID)
            a1 =iptt()
        else:
            print( ' THE same ID will be Used '+aaa[1])
            ID=aaa[1]
            a1 =iptt()





