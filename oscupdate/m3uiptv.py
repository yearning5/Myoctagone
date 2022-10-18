import urllib3
import re
import os
import random
import urllib2
urllib3.disable_warnings()
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
http = urllib3.PoolManager()
link='https://m3uiptv.net/'
f = http.request('GET',link,headers=UserAgent)
the_page = f.data.decode('utf-8').encode('ascii', 'ignore')
a=re.findall('href="(.*?xtream.*?)/"',the_page)
f = http.request('GET',a[0],headers=UserAgent)
the_page = f.data.decode('utf-8').encode('ascii', 'ignore')
hos=re.findall(';">(http.*?)<',the_page)
user=re.findall(';">username=(.*?)<',the_page)
pas=re.findall(';">password=(.*?)<',the_page)

n=min(len(hos),len(user),len(pas))

for i in range(n):
    try:
        link=hos[i]+'/get.php?username='+user[i]+'&password='+pas[i]+'&type=m3u&output=ts'
        a=urllib2.urlopen(link)
        aa=a.readlines()
        m3uf=[]
        for line in aa:
            if line.strip():
                if '#EXTVLCOPT' not in line:
                    m3uf.append(line)
        tmmp='/tmp/'+'xtream'+str(random.randrange(1000,9999))+'.m3u'
        fid=open(tmmp,'w')
        for l in m3uf:
            fid.write(l)
        fid.close()
        # the first line containing channel name
        for i in range(len(m3uf)):
            if m3uf[i].find('EXTINF')>-1:
                count=i
                break
        if os.path.isfile('/etc/enigma2/userbouquet.xtream__tv_.tv'):
            ax='xtream'+str(random.randrange(1000,9999))
            with open('/etc/enigma2/bouquets.tv','r') as f: our=f.readlines()
            if not any(ax in s for s in our):
                with open('/etc/enigma2/bouquets.tv','a') as f: f.write('#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+ax+'__tv_.tv" ORDER BY bouquet\n')
        else:
            ax='xtream'
            with open('/etc/enigma2/bouquets.tv','r') as f: our=f.readlines()
            if not any(ax in s for s in our):
                with open('/etc/enigma2/bouquets.tv','a') as f: f.write('#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+ax+'__tv_.tv" ORDER BY bouquet\n')

        file=open('/etc/enigma2/userbouquet.'+ax+'__tv_.tv','w')
        file.write('#NAME '+ax+' (TV)\n')
        while i <len(m3uf)-1:
                channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                channel=re.sub(r'\s\W+', '', channel)
                a1=m3uf[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
        file.close()
    except:
        pass


