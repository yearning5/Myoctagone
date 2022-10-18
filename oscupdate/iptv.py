import requests
import re
import os
from datetime import date, timedelta
import datetime
import time
import linecache
import sys

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

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
    srchspr='href="(https://www.iptv4sat.com/'+tyear+'.*?sport.*?)"'
    asspr=re.findall(srchspr,the_page,re.DOTALL)
    srchar='href="(https://www.iptv4sat.com/'+tyear+'.*?arab.*?)"'
    asaar=re.findall(srchar,the_page,re.DOTALL)
    srchfr='href="(https://www.iptv4sat.com/'+tyear+'.*?[franc:frenc].*?)"'
    asafr=re.findall(srchfr,the_page,re.DOTALL)
    for l in asaar:
        if len(l)<100 and 'arab' in l:
            linka=l
            break
    for l in asafr:
        if len(l)<100 and 'franc' in l or 'frenc' in l:
            linkfr=l
            break
    
    for l in asspr:
        if len(l)<100 and 'sport' in l:
            linkspr=l
            break
    #arabic
    print 'Arabic will be using the '+'""""  '+linka[len(linka)-11:len(linka)-1]+'  """"''  IPTV lists'
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
            a=a1.replace(':','%3a')+':'+channel+'\n'
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
    print 'French will be using the '+'""""  '+linkfr[len(linkfr)-11:len(linkfr)-1]+'  """"''  IPTV lists'
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
        a=a1.replace(':','%3a')+':'+channel+'\n'
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
    print 'Sport will be using the '+'""""  '+linkspr[len(linkspr)-11:len(linkspr)-1]+'  """"''  IPTV lists'
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
        a=a1.replace(':','%3a')+':'+channel+'\n'
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
    bouq_names=['sportip','france','arabip','filters','autoiptv_sport','autoiptv_normal','autoiptv_movie','autoiptv_kids']
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
    #--------------------------------------#
    #------------- autoiptv ---------------#
    #--------------------------------------#
    link='https://autoiptv.net/playlists/'
    f = requests.get(link)
    the_page = f.text
    the_page =the_page.encode('ascii', 'ignore')
    #SPORT
    a=re.findall('href="(.*?sport.*?)"',the_page,re.DOTALL)
    for l in a:
        if len(l)<=100 and 'xml' not in l:
            break
    sportlin=l
    for l in a:
        if len(l)<=100 and 'xml' in l:
            break
    sportxml=l
    f = requests.get(sportxml)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_sport..xml'
    d=open(locatf,'w')
    for i in ttx:
        d.write(i)
    d.close()
    f = requests.get(sportlin)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_sport..m3u'
    d=open(locatf,'w')
    for i in ttx:
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
    m3ufl.close
    file=open('/etc/enigma2/userbouquet.autoiptv_sport__tv_.tv','w')
    file.write('#NAME autoiptv_sport (TV)\n')

    for i in range(len(m3uf)):
        if 'http:' in m3uf[i]:
            channel=m3uf[i-1].split(',')[1]
            chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
            channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
            file.write(channelurl)
            file.write('#DESCRIPTION '+channel)
    file.close()
          
    #NORMAL
    a=re.findall('href="(.*?normal.*?)"',the_page,re.DOTALL)
    for l in a:
        if len(l)<=100 and 'xml' not in l:
            break
    normallin=l
    for l in a:
        if len(l)<=100 and 'xml' in l:
            break
    normalxml=l
    f = requests.get(normalxml)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_normal..xml'
    d=open(locatf,'w')
    for i in ttx:
        d.write(i)
    d.close()
    f = requests.get(normallin)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_normal..m3u'
    d=open(locatf,'w')
    for i in ttx:
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
    m3ufl.close
    file=open('/etc/enigma2/userbouquet.autoiptv_normal__tv_.tv','w')
    file.write('#NAME autoiptv_normal (TV)\n')

    for i in range(len(m3uf)):
        if 'http:' in m3uf[i]:
            channel=m3uf[i-1].split(',')[1]
            chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
            channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
            file.write(channelurl)
            file.write('#DESCRIPTION '+channel)
    file.close()

    #MOVIE
    a=re.findall('href="(.*?movie.*?)"',the_page,re.DOTALL)
    for l in a:
        if len(l)<=100 and 'xml' not in l:
            break
    movielin=l
    for l in a:
        if len(l)<=100 and 'xml' in l:
            break
    moviexml=l
    f = requests.get(moviexml)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_movie..xml'
    d=open(locatf,'w')
    for i in ttx:
        d.write(i)
    d.close()
    f = requests.get(movielin)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_movie..m3u'
    d=open(locatf,'w')
    for i in ttx:
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
    m3ufl.close
    file=open('/etc/enigma2/userbouquet.autoiptv_movie__tv_.tv','w')
    file.write('#NAME autoiptv_movie (TV)\n')

    for i in range(len(m3uf)):
        if 'http:' in m3uf[i]:
            channel=m3uf[i-1].split(',')[1]
            chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
            channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
            file.write(channelurl)
            file.write('#DESCRIPTION '+channel)
    file.close()
    #KIDS
    a=re.findall('href="(.*?kids.*?)"',the_page,re.DOTALL)
    for l in a:
        if len(l)<=100 and 'xml' not in l:
            break
    kidslin=l
    for l in a:
        if len(l)<=100 and 'xml' in l:
            break
    kidsxml=l
    f = requests.get(kidsxml)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_kids..xml'
    d=open(locatf,'w')
    for i in ttx:
        d.write(i)
    d.close()
    f = requests.get(kidslin)
    ttx=f.text.encode('ascii', 'ignore').split('\r')
    locatf='/tmp/autoiptv_kids..m3u'
    d=open(locatf,'w')
    for i in ttx:
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
    m3ufl.close
    file=open('/etc/enigma2/userbouquet.autoiptv_kids__tv_.tv','w')
    file.write('#NAME autoiptv_kids (TV)\n')

    for i in range(len(m3uf)):
        if 'http:' in m3uf[i]:
            channel=m3uf[i-1].split(',')[1]
            chlink=m3uf[i].strip('\n').replace(':','%3a')+':'+channel.strip('\n')+'\n'
            channelurl='#SERVICE 4097:0:1:0:0:0:0:0:0:0:'+chlink
            file.write(channelurl)
            file.write('#DESCRIPTION '+channel)
    file.close()
#except Exception as e:
#    print e
#    print 'The website is not online yet or Connection Problem....'
#    print '............ Please retry later ........'
except:
    PrintException()
    
