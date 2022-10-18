import os
#name1=stream=name=None
try:
    if not all([name,name1,stream]):
        name1=raw_input(' please input full m3u path =  ').encode('utf-8')
        name=raw_input(' please input bouquet name =  ').encode('utf-8')
        stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
        buff=raw_input('Buffering no= 0 enabel= 1 download=3 ').encode('utf-8')
except:
    name1=raw_input(' please input full m3u path =  ').encode('utf-8')
    name=raw_input(' please input bouquet name =  ').encode('utf-8')
    stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
    buff=raw_input('Buffering no= 0 enabel= 1 download=3 ').encode('utf-8')

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
stream='5002'
buff='0'
with open(locatf,'r') as m3ufl :
    m3uf = m3ufl.readlines()
    
locatf=[]
for line in m3uf:
    if line.strip():
        if '#EXTVLCOPT' not in line and '#EXT-X-SESSION' not in line:
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

