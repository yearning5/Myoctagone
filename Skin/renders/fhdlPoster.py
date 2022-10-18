# -*- coding: utf-8 -*-
# by digiteng...04.2020
# file for skin FullHDLine by sunriser 05.2021

from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, eTimer, loadJPG, eEPGCache, getBestPlayableServiceReference
from Components.Pixmap import Pixmap
from time import gmtime
import sys
import os, requests
import re
import socket
import json
#from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw 
#import io
try:
    from Components.config import config
    lng = config.osd.language.value
    '''with open('/tmp/tex.txt','w') as f:
            f.write(lng+'\n'+lng[:-3])'''
except:
    lng = None
    pass
    
#font = ImageFont.truetype("/usr/share/fonts/nmsbd.ttf", 30)
tmdb_api = "9273a48a3cbdcef9484bf45de6f53ff0"
omdb_api = "cb1d9f55"
sz = "300" # w92 w154 w185 w300 w342  w500 w780 w1280 original
epgcache = eEPGCache.getInstance()

     
if os.path.isdir("/media/hdd"):
    path_folder = "/media/hdd/poster/"
else:
    path_folder = "/tmp/poster/"

if not os.path.exists("/usr/share/enigma2/psatars/"):
    os.mkdir( "/usr/share/enigma2/psatars/")
    
if not os.path.exists(path_folder):
    os.mkdir(path_folder)

if os.path.isdir("/media/hdd"):
    pathLoc = "/media/hdd/infos/"
else:
    pathLoc = "/tmp/infos/"
if not os.path.exists(pathLoc):
    os.mkdir(pathLoc)
PY3 = (sys.version_info[0] == 3)

if PY3:
    from urllib.parse import quote, urlencode
    from urllib.request import urlopen, Request
    from _thread import start_new_thread
else:
    from urllib import quote, urlencode
    from urllib2 import urlopen, Request
    from thread import start_new_thread

REGEX = re.compile(
        r'([\(\[]).*?([\)\]])|'
        r'(: odc.\d+)|'
        r'(\d+: odc.\d+)|'
        r'(\d+ odc.\d+)|(:)|'
        r'/.*|'
        r'\|\s[0-9]+\+|'
        r'[0-9]+\+|'
        r'\s\d{4}\Z|'
        r'([\(\[\|].*?[\)\]\|])|'
        r'(\"|\"\.|\"\,|\.)\s.+|'
        r'\"|\.|'
        r'Премьера\.\s|'
        r'(х|Х|м|М|т|Т|д|Д)/ф\s|'
        r'(х|Х|м|М|т|Т|д|Д)/с\s|'
        r'\s(с|С)(езон|ерия|-н|-я)\s.+|'
        r'\s\d{1,3}\s(ч|ч\.|с\.|с)\s.+|'
        r'\.\s\d{1,3}\s(ч|ч\.|с\.|с)\s.+|'
        r'\s(ч|ч\.|с\.|с)\s\d{1,3}.+|'
        r'\d{1,3}(-я|-й|\sс-н).+|', re.DOTALL)

class fhdlPoster(Renderer):
    '''with open('/etc/enigma2/lamedb') as f:
            ff=f.readlines()'''
    '''if not os.path.exists(R"/usr/share/satrs_empty.png"):
        r = requests.get(r"https://i.ibb.co/DKNmvNm/satrs-empty.png", allow_redirects=True)
        open(r"/usr/share/satrs_empty.png", 'wb').write(r.content)'''

    def __init__(self):
        Renderer.__init__(self)
        self.intCheck()

    def intCheck(self):
        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except:
            return False

    GUI_WIDGET = ePixmap
    def changed(self, what):
        try:
            if not self.instance:
                return
            if what[0] == self.CHANGED_CLEAR:
                self.instance.hide()
            if what[0] != self.CHANGED_CLEAR:
                self.showPoster()
        except:
            pass

    def showPoster(self):
        self.instance.hide()
        self.event = self.source.event
        if self.event is None:
            self.instance.hide()
            return
        if self.event:
            if not os.path.exists(R"/usr/share/enigma2/psatars/satrs_c.png"):
                r = requests.get(r"https://i.ibb.co/rx2gVQr/satrs-c.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satrs_c.png", 'wb').write(r.content)
            if not os.path.exists(R"/usr/share/enigma2/psatars/satr1.png"):
                r = requests.get(r"https://i.ibb.co/dmMP0ht/satr1.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satr1.png", 'wb').write(r.content)
            if not os.path.exists(R"/usr/share/enigma2/psatars/satrs_w.png"):
                r = requests.get(r"https://i.ibb.co/YpVMMg8/satrs-w.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satrs_w.png", 'wb').write(r.content)
            if not os.path.exists(R"/usr/share/enigma2/psatars/satrs_c1.png"):
                r = requests.get(r"https://i.ibb.co/w6N0Qdj/satrs-c1.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satrs_c1.png", 'wb').write(r.content)
            if not os.path.exists(R"/usr/share/enigma2/psatars/satrs_w1.png"):
                r = requests.get(r"https://i.ibb.co/RpDJ0SY/satrs-w1.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satrs_w1.png", 'wb').write(r.content)
            if not os.path.exists(R"/usr/share/enigma2/psatars/satr11.png"):
                r = requests.get(r"https://i.ibb.co/Qk9b4tv/satr11.png", allow_redirects=True)
                open(r"/usr/share/enigma2/psatars/satr11.png", 'wb').write(r.content)
            self.delay2()
            eventNm = REGEX.sub('', self.event.getEventName()).strip().replace('ё','е')
            eventNm = eventNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
            #open("/tmp/infomovie_rate.txt", "w").write(eventNm)
            pstrNm = "{}{}.jpg".format(path_folder, eventNm)
            if not os.path.exists(pstrNm):
                if self.intCheck():
                    self.downloadPoster(eventNm)
            if os.path.exists(pstrNm):
                self.instance.setPixmap(loadJPG(pstrNm))
                self.instance.show()
        else:
            self.instance.hide()
            return

    def downloadPoster(self, eventNm):
        self.year = self.filterSearch()
        try:
            #url_tmdb = "http://api.tmdb.org/3/search/{}?api_key={}&query={}&language=en-US".format(self.srch, tmdb_api, quote(eventNm))
            url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(self.srch, tmdb_api, quote(eventNm))
            if self.year != None:
                url_tmdb += "&year={}".format(self.year)
            if lng != None:
                url_tmdb += "&language={}".format(lng[:-3])
            else:
                pass
            '''with open('/tmp/ttt.txt','w') as f:
                f.write(eventNm)'''
            poster = json.load(urlopen(url_tmdb))["results"][0]["poster_path"]
            with open('/tmp/ttt1.txt','w') as f:
                f.write(url_tmdb)
            title1 = json.load(urlopen(url_tmdb))["results"][0]["title"]
            with open('/tmp/ttt.txt','w') as f:
                f.write(title1)
            url_omdb = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_api, quote(title1))
            data_omdb = json.load(urlopen(url_omdb))
            rating=data_omdb["imdbRating"]
            dwnldFile = "{}{}.json".format(pathLoc, eventNm)
            if not os.path.exists(dwnldFile):
                with open(dwnldFile,'w') as f:
                    f.write(json.dumps(data_omdb))
            rating =float(rating)
            #rating =json.load(urlopen(url_tmdb))["results"][0]["vote_average"]
            if rating<10:
                if type(rating)==float:
                    rating= str(rating)
                else:
                    rating= str(rating)+'.0'
            else:
                rating= str(rating)
            #title1 = json.load(urlopen(url_tmdb))["results"][0]["title"]
            #url_omdb = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_api, quote(title1))
            #data_omdb = json.load(urlopen(url_omdb))
            #rating=data_omdb["imdbRating"]
            if poster:
                #url_poster = "http://image.tmdb.org/t/p/w185{}".format(poster)
                url_poster = "https://image.tmdb.org/t/p/w{}{}".format(sz, poster)
                dwn_poster = "{}{}.jpg".format(path_folder, eventNm)
                #fd = urllib1.urlopen(url_poster)
                with open(dwn_poster, "wb") as f:
                            f.write(urlopen(url_poster).read())
                #im = Image.open(image_file)
                """#im =im.resize((im.size[0],216))
                w = 50 # 100 pixels wide
                h = 276 # 100 pixels high
                #  for resise  to be 350 pixel 350 / 276 = fact = 1.27
                fact=1.27
                img = Image.new('RGB', (int(w*fact), int(h*fact)))
                #img = Image.new('RGB', (w, h))
                img = Image.open(R"/usr/share/satrs_c.png")
                img=img.resize((int(img.size[0]*fact),int(img.size[1]*fact)))
                '''datas = img.getdata()
                #  convert to white
                newData = []
                for item in datas:
                    if item[0] == 255 and item[1] == 174 and item[2] == 1:
                        newData.append((255, 255, 255, item[3]))
                    else:
                        newData.append(item)
                im2 = Image.new(img.mode, img.size)
                im2.putdata(newData)
                im2.save('/tmp/im2.png')'''
                im2=Image.open(R"/usr/share/satrs_w.png")
                im2=im2.resize((int(im2.size[0]*fact),int(im2.size[1]*fact)))
                draw=ImageDraw.Draw(img)
                rt=(h-70)*(100-float(rating)*10)/100+70
                rt=rt*fact
                #rect_size=(70, int(round(rt)))
                rect_size=(int(70*fact), int(round(rt)))
                #area=(0,int(round(rt)),50,276)
                area=(0,int(round(rt)),int(w*fact), int(h*fact))
                cropped_img = img.crop(area)
                #rect = Image.new("RGBA", rect_size, (255, 255, 255, 0))
                #img.paste(rect, (0,0))
                #img12 = Image.new('RGBA', (w, h), (255, 0, 0, 0))
                img12 = Image.new('RGBA', (int(w*fact), int(h*fact)), (255, 0, 0, 0))
                img12.paste(im2)
                img12.paste(cropped_img,(0,int(round(rt))))
                '''img11 = Image.new('RGB', (w, h))
                img11 = Image.open(R"/usr/share/satrs_empty.png")
                img12 = Image.new('RGBA', (w, h), (255, 0, 0, 0))
                img12.paste(img11)
                img12.paste(cropped_img,(0,int(round(rt))))'''
                img=img12
                img2 = Image.open(R"/usr/share/satr1.png")
                img2=img2.resize((int(img2.size[0]*fact),int(img2.size[1]*fact)))
                draw=ImageDraw.Draw(img2)
                #font = ImageFont.truetype("arial.ttf", 15)
                #w1, h1 = draw.textsize(rating)
                #W,H=img2.size
                #draw.text(((W-w1)/2-12,(H-h1)/2-6), rating,font=font, fill="#000")
                draw.text((16*fact, 23*fact), rating,font=font, fill="#000")
                #img3=Image.new('RGBA', (70, 276),(255, 0, 0, 0))
                img3=Image.new('RGBA', (int(70*fact), int(276*fact)),(255, 0, 0, 0))
                xc=int((img2.size[0]-img.size[0])/2)
                img3.paste(img,(xc,0))
                img3.paste(img2,(0,0))
                #img21=Image.new('RGBA', (255, 276),(255, 0, 0, 0))
                img21=Image.new('RGBA', (int(255*fact), int(276*fact)),(255, 0, 0, 0))
                #im=im.resize((int(im.size[0]),228))
                im=im.resize((int(int(im.size[0]/fact)),int(228*fact)))
                #img21.paste(im,(0,50))
                img21.paste(im,(0,int(50*fact)))
                img21.paste(img3,(int(im.size[0]),0))"""
                #im.save(dwn_poster)
        except:
            infos_file = "{}{}.json".format(pathLoc, eventNm)
            if os.path.exists (infos_file):
                with open(infos_file) as f:
                    url_poster = json.load(f)["Poster"].replace("SX300.jpg","SX185.jpg")
                if url_poster != "N/A":
                    dwn_poster = "{}{}.jpg".format(path_folder, eventNm)
                    with open(dwn_poster, "wb") as f:
                        f.write(urlopen(url_poster).read())
            else:
                return

    def filterSearch(self):
        try:
            sd = "%s\n%s\n%s" % (self.event.getEventName(), self.event.getShortDescription(), self.event.getExtendedDescription())
            w = [
                "т/с",
                "Т/с",
                "м/с",
                "М/с",
                "д/с",
                "Д/с",
                "сезон",
                "с-н",
                "эпизод",
                "сериал",
                "серия"
                ]
            for i in w:
                if i in sd:
                    self.srch = "tv"
                    break
                else:
                    self.srch = "multi"
            yr = [ _y for _y in re.findall(r'\d{4}', sd) if '1930' <= _y <= '%s' % gmtime().tm_year ]
            return '%s' % yr[-1] if yr else ''
        except:
            pass

    def epgs(self):
        events = None
        import NavigationInstance
        ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
        events = epgcache.lookupEvent(['IBDCT', (ref, 0, -1, -1)])
        for i in range(len(events)):
            titleNxt = events[i][4]
            eventNm = REGEX.sub('', titleNxt).rstrip().replace('ё','е')
            pstrNm = "{}{}.jpg".format(path_folder, eventNm)
            if not os.path.exists(pstrNm):
                self.downloadPoster(eventNm)
        return

    def delay2(self):
        self.timer = eTimer()
        self.timer.callback.append(self.dwn)
        self.timer.start(3000, True)

    def dwn(self):
        start_new_thread(self.epgs, ())