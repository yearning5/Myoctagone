import requests, re 

# bee movies adel imam
def fn(link):
    try:
        r1 = requests.get(link)
        r1l=re.findall('https://manifest.*?(https://manifest.*?.m3u8)"',r1.text)[0]
        #print ' adel '+r1l
    except:
        r1l=''
    return r1l

adel='https://www.youtube.com/watch?v=i4A1L4xW6Ns&ab_channel=BeeMovies'
yacin='https://www.youtube.com/watch?v=89iVz5VtvVM&ab_channel=alyelbasl'
beemov='https://www.youtube.com/watch?v=uiqvy-qLRPo&ab_channel=BeeShots'
bo='https://www.youtube.com/watch?v=9xDsvoOaIFk'
TVPlus='https://www.youtube.com/watch?v=zXfA4xnteKY&ab_channel=alyelbasl'

r1l=fn(adel)
r2l=fn(yacin)
r3l=fn(beemov)
r4l=fn(TVPlus)
r5l=fn(bo)
with open(r'/etc/enigma2/userbouquet.nilesat__tv_.tv') as f:
    ff=f.read()
    
imam=re.findall('#SERVICE .*?:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):Bee Adel Imam',ff)[0]
isma=re.findall('#SERVICE .*?:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):Bee Ismail ya',ff)[0]
bee1=re.findall('#SERVICE .*?:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):Bee Movies',ff)[0]
bee2=re.findall('#SERVICE .*?:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):TVPlus Aflam',ff)[0]
Boob=re.findall('#SERVICE .*?:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):Odbods',ff)[0]

#maash=re.findall('#SERVICE 5002:0:1:0:0:0:0:0:0:0:https%3a//manifest.googlevideo.com(.*?):MASH_\xd9\x85\xd8',ff)[0]

with open(r'/etc/enigma2/userbouquet.nilesat__tv_.tv','w') as f:
    ff1=ff
    if r1l!='':
        ff1=ff1.replace(imam,fn(adel).replace('https://manifest.googlevideo.com',''))
    if r2l!='':
        ff1=ff1.replace(isma,fn(yacin).replace('https://manifest.googlevideo.com',''))
    if r3l!='':
        ff1=ff1.replace(bee1,fn(beemov).replace('https://manifest.googlevideo.com',''))
    if r4l!='':
        ff1=ff1.replace(bee2,fn(TVPlus).replace('https://manifest.googlevideo.com',''))
    if r5l!='':
        ff1=ff1.replace(Boob,fn(bo).replace('https://manifest.googlevideo.com',''))
    f.write(ff1)
    