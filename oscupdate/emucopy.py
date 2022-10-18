# -*- coding: utf-8 -*-
import sys

PY3=sys.version_info[0]

import os, subprocess

'''
p=open('/etc/image-version','r')
pp=p.readlines()
p.close()
for i in pp:
    if 'creator' in i.lower():
        image=i.split('=')[1]'''
#print image
image=subprocess.check_output('grep "."  /etc/issue | tail -1',shell=True)[:-6]
if PY3==3:
    image=image.decode()

oo=os.popen('df -h').readlines()
for i in oo:
    if '/dev/sda' in i:
        loc=i.split()[-1]
        break
path=i.split()[-1]+'/NFR4XBootI/'
"""images=['opennfr-6.4', 'openvision9r93', 'openspa-7.4', 'openpli-7.2',
'openhdf-6.5', 'openeight-6.7', 'openvix-5.3', 'PKT_Hyp7',
'Satdreamgr-6-sf', 'opendroid-7', 'openhdf-6.4', 'openbh-4.3', 'openatv-6.4']"""

"""'/media/nfr4xboot/NFR4XBootI/openvision9/etc/tuxbox/oscam-emu'

'vix' '/media/nfr4xboot/NFR4XBootI/openvix-5.3/etc/tuxbox/config'

'pkt' '/media/nfr4xboot/NFR4XBootI/Hyp7/var/keys'"""

images=os.popen('ls '+path).readlines()

#filee=raw_input('Input oscam file name  =  ')
#if filee=='':
filee='oscam_emu'


if 'pkt' in image.lower():
    source='/var/emu/'+filee

elif 'vix' in image.lower():
    source='/usr/softcams/'+filee
else:
    source='/usr/bin/cam/'+filee




for i in images:
    i=i.strip('\n')
    if 'pkt' in i.lower() or 'hyp' in i.lower():
        dest='/var/emu/'+filee
        #try: os.system('cp '+source+' '+path+i+dest)
        #except: pass
    elif 'vix' in i.lower():
        dest='/usr/softcams/'+filee
        #try: os.system('cp '+source+' '+path+i+dest)
        #except: pass
    else:
        dest='/usr/bin/cam/'+filee
        #try: os.system('cp '+source+' '+path+i+dest)
        #except: pass
    try:
        os.system('cp '+source+' '+path+i+dest)
        print (path+i+dest)
    except:
        pass

for i in oo:
    if '/dev/sda' in i:
        loc=i.split()[-1]
        break
try:
    path2=i.split()[-1]+'/ImageBoot/'
    images2=os.popen('ls '+path2).readlines()
    for i in images2:
        i=i.strip('\n')
        if 'pkt' in i.lower() or 'hyp' in i.lower():
            dest='/var/emu/'+filee
            #try: os.system('cp '+source+' '+path+i+dest)
            #except: pass
        elif 'vix' in i.lower():
            dest='/usr/softcams/'+filee
            #try: os.system('cp '+source+' '+path+i+dest)
            #except: pass
        else:
            dest='/usr/bin/cam/'+filee
            #try: os.system('cp '+source+' '+path+i+dest)
            #except: pass
        try:
            os.system('cp '+source+' '+path2+i+dest)
            print (path2+i+dest)
        except:
            pass
except:
    pass

# ======================= mmcblk0p16 ==========================

if not os.path.isdir('/media/oscam_fold'):
    os.popen('mkdir /media/oscam_fold')
osc_fold='/media/oscam_fold/'
if os.path.ismount('/dev/mmcblk0p16'):
    os.popen('umount /dev/mmcblk0p16')

os.popen('mount /dev/mmcblk0p16 /media/oscam_fold > /dev/null 2>&1')
imgs=[i for i in os.listdir('/media/oscam_fold') if 'linuxrootfs' in i]
print(imgs)
for n in imgs:
    try:
        image=subprocess.check_output('grep "."  '+osc_fold+n+'/etc/issue | tail -1',shell=True)[:-6]
        if PY3==3:
            image=image.decode()
            print (image)
        if 'pkt' in image.lower():
            os.system('cp '+source+' '+osc_fold+n+'/var/emu/'+filee)
            print (osc_fold+n)
        elif 'vix' in image.lower():
            os.system('cp '+source+' '+osc_fold+n+'/usr/softcams/'+filee)
            print (osc_fold+n)
        elif 'define' in image.lower():
            os.system('cp '+source+' '+osc_fold+'/userdata2/gx/local/oscam-smod/'+filee)
            print( osc_fold+n)
        else:
            os.system('cp '+source+' '+osc_fold+n+'/usr/bin/cam/'+filee)
            print( osc_fold+n)
    except:
        pass

os.popen('umount /dev/mmcblk0p16')









"""
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/opennfr-6.4/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/Satdreamgr-6-sf/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openatv-6.4/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openbh-4.3/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/opendroid-7/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openeight-6.7/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openhdf-6.5/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openhdf-6.4/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openspa-7.4/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openvision9r93/etc/tuxbox/oscam-emu')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openvix-5.3/etc/tuxbox/config')
except: pass
try: os.system('cp '+source+' /media/hdd//NFR4XBootI/openpli-7.2/etc/tuxbox/oscam-emu')
except: pass
"""