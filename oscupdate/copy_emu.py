import os, subprocess
'''p=open('/etc/image-version','r')
pp=p.readlines()
p.close()
for i in pp:
    if 'creator' in i.lower():
        image=i.split('=')[1]'''
#print image

image=subprocess.check_output('grep "."  /etc/issue | tail -1',shell=True)[:-6]

oo=os.popen('df -h').readlines()
for i in oo:
    if '/dev/sda' in i:
        loc=i.split()[-1]
        break
path=i.split()[-1]+'/NFR4XBootI/'

images=os.popen('ls '+path).readlines()

filee='oscam_emu'

if 'pkt' in image.lower():
    source='/var/emu/'+filee

elif 'vix' in image.lower():
    source='/usr/softcams/'+filee
else:
    source='/usr/bin/cam/'+filee




for i in images:
    i=i.strip('\n')
    if 'hyp' in i.lower() or 'pkt' in i.lower():
        dest='/var/emu/'+filee
        try: os.system('cp '+source+' '+path+i+dest)
        except: pass
    elif 'vix' in i.lower():
        dest='/usr/softcams/'+filee
        try: os.system('cp '+source+' '+path+i+dest)
        except: pass
    else:
        dest='/usr/bin/cam/'+filee
        try: os.system('cp '+source+' '+path+i+dest)
        except: pass
