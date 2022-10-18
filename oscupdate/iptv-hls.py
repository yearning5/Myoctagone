import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
tday=datetime.datetime.today().strftime('%d')
tmonth=datetime.datetime.today().strftime('%m')
tyear=datetime.datetime.today().strftime('%Y')
tdate=(datetime.datetime.today()+timedelta(1)).strftime('%d-%m-%Y')
#tdate=(datetime.datetime.today()- timedelta(1)).strftime('%d-%m-%Y')
link='https://www.iptv4sat.com/'+tyear+'/'+tmonth+'/'
try:
    f = requests.get(link)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    if tdate not in the_page:
        print '                                                                   '
        print '                The website is not yet UPDATED today....           '
        print ' ........  the rogram will try to look for the most recent Update...........'
        print '                                                                      '
        print ' ------------------------------------------------------------------------ '
        time.sleep(3)
        i=0
        while i < 10:
            tdate=(datetime.datetime.today()- timedelta(i)).strftime('%d-%m-%Y')
            if tdate in the_page:
                print '\n'
                print '... "''_''"  .. The most recent link available is : '+'""""  '+tdate+'  """"'+'....'
                break
            i +=1
    time.sleep(3)
    print '\n'
    print 'We will be using the '+'""""  '+tdate+'  """"'+'  IPTV lists'
    print '\n'
    print '\n'
    if os.path.isfile('/etc/enigma2/userbouquet.arabip__tv_.tv'):
        os.remove('/etc/enigma2/userbouquet.arabip__tv_.tv')
        file=open('/etc/enigma2/userbouquet.arabip__tv_.tv','w')
        file.close()
    else:
        file=open('/etc/enigma2/userbouquet.arabip__tv_.tv','w')
        file.close()
    #france__sport    
    if os.path.isfile('/etc/enigma2/userbouquet.france__tv_.tv'):
        os.remove('/etc/enigma2/userbouquet.france__tv_.tv')
        file=open('/etc/enigma2/userbouquet.france__tv_.tv','w')
        file.close()
    else:
        file=open('/etc/enigma2/userbouquet.france__tv_.tv','w')
        file.close()
    #sports
    if os.path.isfile('/etc/enigma2/userbouquet.sportip__tv_.tv'):
        os.remove('/etc/enigma2/userbouquet.sportip__tv_.tv')
        file=open('/etc/enigma2/userbouquet.sportip__tv_.tv','w')
        file.close()
    else:
        file=open('/etc/enigma2/userbouquet.sportip__tv_.tv','w')
        file.close()
    #srch='(https://www.iptv4sat.com/'+tdate[6:]+'/'+tdate[3:5]+'/.*?'+tdate+'/)'
    #a=re.findall(srch,the_page,re.DOTALL)
    #for i in range(len(a)):
    #    if len(a[i])<200:
    #        if 'arab' in a[i]:
    #            break
    #linka=a[i]

    #for i in range(len(a)):
    #    if len(a[i])<200:
    #        if 'frenc' in a[i]:
    #            break
    #linkfr=a[i]
    #for i in range(len(a)):
    #    if len(a[i])<200:
    #        if 'sport' in a[i]:
    #            break
    #linkspr=a[i]
    asspr=re.findall('(https://www.iptv4sat.com/.*?sport.*?)"',the_page,re.DOTALL)
    asaar=re.findall('(https://www.iptv4sat.com/.*?arab.*?)"',the_page,re.DOTALL)
    asafr=re.findall('(https://www.iptv4sat.com/.*?frenc.*?)"',the_page,re.DOTALL)
    for l in asaar:
        if len(l)<100:
            linka=l
            break
    for l in asafr:
        if len(l)<100:
            linkfr=l
            break
    for l in asspr:
        if len(l)<100:
            linkspr=l
            break
    #arabic
    f = requests.get(linka)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    aa=the_page.find('https://www.iptv4sat.com/download-attachment')
    b=the_page[aa:].find('"')
    downlinka=the_page[aa:aa+b]
    import requests, zipfile, StringIO
    r = requests.get(downlinka, stream=True)
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall('/tmp')
    locatf='/tmp/'+z.namelist()[0]
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
    file=open('/etc/enigma2/userbouquet.arabip__tv_.tv','w')
    file.write('#NAME arabip (TV)\n')
    while i <len(m3uf)-1:
            channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
            channel=channel.strip('\r')
            a1=m3uf[i+1].strip('\n')
            a1=a1.strip('\r')
            a=a1.replace(':','%3a')+'&output=HLSRETRY:'+channel+'\n'
            channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
            file.write(channelurl)
            file.write('#DESCRIPTION '+channel+'\n')
            i = i+2
    file.close()
    # the first line containing channel name
    for i in range(len(m3uf)):
        if m3uf[i].find('EXTINF')>-1:
            count=i
            break
    kodi=open('/tmp/arabic.xml','w')
    kodi.write('<streamingInfos>\n')
    while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        channelurl=a1.strip('\r')
        kodi.write('<streaminginfo>\n')
        #kodi.write('\t<cname>'+channel+'</cname>\n')
        kodi.write('\t<item>\n')
        kodi.write('\t<title>'+channel+'<title>\n')
        kodi.write('\t<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+channelurl+'</link>\n')
        kodi.write('\t</item>\n')
        kodi.write('</streaminginfo>\n')
        i = i+2
    kodi.write('</streamingInfos>\n')
    kodi.close()
    #France
    f = requests.get(linkfr)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    aa=the_page.find('https://www.iptv4sat.com/download-attachment')
    b=the_page[aa:].find('"')
    downlinkfr=the_page[aa:aa+b]
    import requests, zipfile, StringIO
    r = requests.get(downlinkfr, stream=True)
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall('/tmp')
    locatf='/tmp/'+z.namelist()[0]
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
    file=open('/etc/enigma2/userbouquet.france__tv_.tv','w')
    file.write('#NAME france (TV)\n')
    while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+'&output=HLS:'+channel+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
    file.close()
    # the first line containing channel name
    for i in range(len(m3uf)):
        if m3uf[i].find('EXTINF')>-1:
            count=i
            break
    kodi=open('/tmp/french.xml','w')
    kodi.write('<streamingInfos>\n')
    while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        channelurl=a1.strip('\r')
        kodi.write('<streaminginfo>\n')
        #kodi.write('\t<cname>'+channel+'</cname>\n')
        kodi.write('\t<item>\n')
        kodi.write('\t<title>'+channel+'<title>\n')
        kodi.write('\t<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+channelurl+'</link>\n')
        kodi.write('\t</item>\n')
        kodi.write('</streaminginfo>\n')
        i =i+2
    kodi.write('</streamingInfos>\n')
    kodi.close()
    #Sport
    f = requests.get(linkspr)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    aa=the_page.find('https://www.iptv4sat.com/download-attachment')
    b=the_page[aa:].find('"')
    downlinkspr=the_page[aa:aa+b]
    import requests, zipfile, StringIO
    r = requests.get(downlinkspr, stream=True)
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall('/tmp')
    locatf='/tmp/'+z.namelist()[0]
    m3ufl = open(locatf,'r')
    m3uf = m3ufl.readlines()
    m3ufl.close()
    m3ufl = open(locatf,'w')
    for line in m3uf:
        if line.strip():
            if '#EXTVLCOPT' not in line:
                m3ufl.write(line)
    m3ufl.close()
    m3ufl = open(locatf,'r')
    m3uf = m3ufl.readlines()
    m3ufl.close()
    # the first line containing channel name
    for i in range(len(m3uf)):
        if m3uf[i].find('EXTINF')>-1:
            count=i
            break
    file=open('/etc/enigma2/userbouquet.sportip__tv_.tv','w')
    file.write('#NAME sportip (TV)\n')
    while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+'&output=HLS:'+channel+'\n'
        channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
    file.close()
    for i in range(len(m3uf)):
        if m3uf[i].find('EXTINF')>-1:
            count=i
            break
    kodi=open('/tmp/sport.xml','w')
    kodi.write('<streamingInfos>\n')
    while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        channelurl=a1.strip('\r')
        kodi.write('<streaminginfo>\n')
        #kodi.write('\t<cname>'+channel+'</cname>\n')
        kodi.write('\t<item>\n')
        kodi.write('\t<title>'+channel+'<title>\n')
        kodi.write('\t<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+channelurl+'</link>\n')
        kodi.write('\t</item>\n')
        kodi.write('</streaminginfo>\n')
        i =i+2
    kodi.write('</streamingInfos>\n')
    kodi.close()
    file=open('/etc/enigma2/bouquets.tv','r')
    m3uf = file.readlines()
    file.close()
    al=[]
    bouq_names=['sportip','france','arabip','filters']
    for line in m3uf:
        if not any( k  in line for k in bouq_names) :
            al.append(line)

    aa='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET '
    for nn in bouq_names:
        arl=aa+'"userbouquet.'+nn+'__tv_.tv" ORDER BY bouquet\n'
        al.append(arl)
    if os.path.isfile('bouquets.tv'):
        os.remove('bouquets.tv')
    open("/etc/enigma2/bouquets.tv", "w").writelines([l for l in al])

    if os.path.isfile('/etc/enigma2/userbouquet.arabip__tv_.tv'):
            file=open('/etc/enigma2/userbouquet.arabip__tv_.tv','r')
            arablines=file.readlines()
            file.close()
    if os.path.isfile('/etc/enigma2/userbouquet.france__tv_.tv'):
            file=open('/etc/enigma2/userbouquet.france__tv_.tv','r')
            franlines=file.readlines()
            file.close()

    fltlines=[]
    fltch=['piwi','bara','jeem','tiji',' jr', '_jr']
    for lin in arablines:
        if any(nn in lin.lower() for nn in fltch):
            fltlines.append(lin)
    for lin in franlines:
        if any(nn in lin.lower() for nn in fltch):
            fltlines.append(lin)

    if os.path.isfile('/etc/enigma2/userbouquet.filters__tv_.tv'):
            os.remove('/etc/enigma2/userbouquet.filters__tv_.tv')
            file=open('/etc/enigma2/userbouquet.filters__tv_.tv','w')
            file.close()
    else:
        file=open('/etc/enigma2/userbouquet.filters__tv_.tv','w')
        file.close()

    file=open('/etc/enigma2/userbouquet.filters__tv_.tv','w')
    file.write('#NAME filters (TV)\n')
    for line in fltlines:
        file.write(line)
    file.close()
except Exception as e:
    print e
    print 'The website is not online yet or Connection Problem....'
    print '............ Please retry later ........'
