from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def main():
    import urllib2
    import urllib
    import base64
    import os
    import os.path

    def getPage(link, splitting = '\n'):
        from urllib2 import Request, urlopen
        request = Request(link)
        try:
            response = urlopen(request)
        except IOError:
            return -1
        else:
            the_page = response.read()
            the_page=the_page.split('\n')        
            i=0
            while  i<= len(the_page):
                if all(s in the_page[i] for s in ("C:",))==True:
                    c1=the_page[i].find('C:')
                    c2=the_page[i].find('</strong></a>')
                    break  
                i +=1
            ser=the_page[i][c1:c2].split()
            host=ser[1]
            port=ser[2]
            user=ser[3]
            Pass=ser[4]

        return [host,port,user,Pass]

    link='http://mecccam.com/free-cccam.php'
    mecccam=getPage(link)
    link1='http://cccam-free.com/NEW/new0.php'
    cccamfree=getPage(link1)
    link2='http://freeccamserver.com/free/get2.php'
    freeccamserver=getPage(link2)
    servers=[mecccam,cccamfree,freeccamserver]

    if os.path.isfile('/etc/tuxbox/oscam-emu/oscam.server'):
        the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','r')
        the_page =the_pag.readlines()
        the_pag.close()
        the_pag=open('/etc/tuxbox/oscam-emu/oscam.server','w')
        #mecccam
        labels=['ww.mecccam.com','cccam-free','freeccamserver']
        for j in range(len(labels)):
            i=0
            while  i<= len(the_page):
                if all(s in the_page[i] for s in (labels[j], "label"))==True:
                    ll=len(the_page[i+3])
                    c1=the_page[i+3].find('=')
                    c2=the_page[i+3].find(',')
                    #host
                    the_page[i+3]=the_page[i+3].replace(the_page[i+3][c1:c2],'='+servers[j][0])
                    #port
                    c22=the_page[i+3].find(',')
                    the_page[i+3]=the_page[i+3].replace(the_page[i+3][c22+1:ll-1],servers[j][1])
                    c2=the_page[i+4].find('=')
                    ll1=len(the_page[i+4])
                    the_page[i+4]=the_page[i+4].replace(the_page[i+4][c2:ll1-1],'='+servers[j][2])
                    #pass
                    c3=the_page[i+5].find('=')
                    ll2=len(the_page[i+5])
                    the_page[i+5]=the_page[i+5].replace(the_page[i+5][c3:ll2-1],'='+servers[j][3])
                    break  
                i +=1
        for i in the_page:
            the_pag.write(i)
        the_pag.close()

t = Timer(secs, main)
t.start()