import os
path='/tmp/tv_channels_yqdJRV8Q4_plus.m3u'
ff=open(path,'r')
oo=ff.readlines()
ff.close()

##     arab
it=['arab','netflix','spor','sport','france']
lis=[]
for n in it:
    ind= [i for i, s in enumerate(oo) if all(ii in s.lower() for ii in [n,'---'])]
    ind1= [i for i, s in enumerate(oo[ind[0]+1:]) if '---' in s]
    lis.append(oo[ind[0]:ind[0]+ind1[0]+1])

liss=lis[0]+lis[1]+lis[2]+lis[3]+lis[4]
path='/tmp/'+path.split("\\")[-1].strip('.m3u')[-10:]+'.m3u'
ff=open(path,'w')
ff.write('#EXTM3U\n')
for i in liss:
    ff.write(i)
ff.close()


name='fitiptv'
name1=path
stream ='5002'

execfile("/oscupdate/originsat.py")
os.system('wget -qO - http://127.0.0.1/web/servicelistreload?mode=2')