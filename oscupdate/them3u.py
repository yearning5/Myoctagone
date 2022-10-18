import requests, re,  urllib, os

headers = {
    'authority': 'them3u.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://them3u.com/m3u-iptv-list-iptv-links-free-16-01-2022/',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
}

try:
    
    r1 = requests.get('https://them3u.com/', headers=headers).text
    a1=re.findall('class="entry-title".*?href="(.*?)"',r1)
    a1=[ i for i in a1 if 'iptv-list' in i.lower()]
    r2=requests.get(a1[0], headers=headers).text
    a22=re.findall('<p>(.*?)</p>',r2) 
    a2=[ i for i in a22 if 'get.php' in i ]
    
    if len(a2)>15:
        ll=15
    else:
        ll=len(a2)
        
    for ij in range(ll):
        try:
            name1='/tmp/them3u_'+str(ij+1)+'.m3u'
            nnnn=urllib.urlretrieve(a2[ij].replace('#038;',''), name1)
            name='them3u_'+str(ij+1)
            stream='5002'
            buff='0'
            #bouquets
            bouq=open('/etc/enigma2/bouquets.tv','r')
            bo=bouq.read()
            bouq.close()
            if name not in bo:
                new='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+name+'__tv_.tv" ORDER BY bouquet\n'
                file=open('/etc/enigma2/bouquets.tv','a')
                file.write(new)
                file.close()
            
            locatf=name1
            
            with open(locatf,'r') as m3ufl :
                m3uf = m3ufl.readlines()
            locatf=[]
            for line in m3uf:
                if line.strip():
                    if '#EXTVLCOPT' not in line:
                        locatf.append(line)
            m3uf =locatf
            
            zip_iterator = zip(m3uf[1:][::2], m3uf[1:][1::2])
            
            a_dictionary = dict(zip_iterator)
            
            if os.path.isfile('/etc/enigma2/userbouquet.'+name+'__tv_.tv'):
                os.remove('/etc/enigma2/userbouquet.'+name+'__tv_.tv')
                file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
                file.close()
            file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
            file.write('#NAME '+name+' (TV)\n')
            
            bein=[]
            for key in a_dictionary.keys():
                if 'bein' in key.lower():
                    bein.append([key,a_dictionary[key]])
                    chn=key.strip('\n').split(',')[1].replace(':','').strip('\r')
                    churl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:'+buff+':'+a_dictionary[key].strip('\n').strip('\r').replace(':','%3a')+':'+chn+'\n'
                    #file.write(churl)
                    #file.write('#DESCRIPTION '+chn+'\n')
                    
                    
            
            bein.sort(key=lambda x:x[0].split(',')[1])        
            bein=sum(bein, [])
            i=0
            while i <len(bein)-1:
                channel=bein[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                a1=bein[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:'+buff+':'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
            
            fr=[]
            for key in a_dictionary.keys():
                if 'rmc' in key.lower():
                    fr.append([key,a_dictionary[key]])
                   
            fr.sort(key=lambda x:x[0].split(',')[1])        
            fr=sum(fr, [])
            
            i=0
            while i <len(fr)-1:
                channel=fr[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                a1=fr[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:'+buff+':'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
                
                
                
            OSN=[]
            for key in a_dictionary.keys():
                if 'osn' in key.lower():
                    OSN.append([key,a_dictionary[key]])
            
            OSN.sort(key=lambda x:x[0].split(',')[1])        
            OSN=sum(OSN, [])
            
            i=0
            while i <len(OSN)-1:
                channel=OSN[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                a1=OSN[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:'+buff+':'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
                    
            '''        
            bein=[]
            for i in range(0,len(m3uf[1:])-1,2):
                if 'bein' in m3uf[1:][i].lower():
                    bein.append(m3uf[1:][i])
                    bein.append(m3uf[1:][i+1])
            
            fr=[]
            
            for i in range(0,len(m3uf[1:])-1,2):
                if 'rmc' in m3uf[1:][i].lower():
                    fr.append(m3uf[1:][i])
                    fr.append(m3uf[1:][i+1])
            
            OSN=[]
            for i in range(0,len(m3uf[1:])-1,2):
                if 'osn' in m3uf[1:][i].lower():
                    OSN.append(m3uf[1:][i])
                    OSN.append(m3uf[1:][i+1])
            
            '''
            m3uf=[ l for l in m3uf if l not in zip(bein,OSN,fr)]
            # the first line containing channel name
            for i in range(len(m3uf)):
                if m3uf[i].find('EXTINF')>-1:
                    count=i
                    break
            
            while i <len(m3uf)-1:
                b=i
                channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
                channel=channel.strip('\r')
                a1=m3uf[i+1].strip('\n')
                a1=a1.strip('\r')
                a=a1.replace(':','%3a')+':'+channel+'\n'
                channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:'+buff+':'+a
                file.write(channelurl)
                file.write('#DESCRIPTION '+channel+'\n')
                i = i+2
            file.close()

            print (name + ' has been created')
        except:
            pass
except:
    pass
