# -*- coding: utf-8 -*-
# by digiteng...04.2020
# file for skin FullHDLine by sunriser 05.2021

from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, eTimer, loadJPG, eEPGCache, getBestPlayableServiceReference
from Components.Pixmap import Pixmap
from time import gmtime
import sys
import os
import re
import socket
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import urllib2 as urllib1
import io
font = ImageFont.truetype("/usr/share/fonts/nmsbd.ttf", 30)
tmdb_api = "9273a48a3cbdcef9484bf45de6f53ff0"
omdb_api = "cb1d9f55"
epgcache = eEPGCache.getInstance()

if os.path.isdir("/media/hdd"):
	path_folder = "/media/hdd/poster2/"
else:
	path_folder = "/tmp/poster2/"
if not os.path.exists(path_folder):
	os.mkdir(path_folder)

if os.path.isdir("/media/hdd"):
	pathLoc = "/media/hdd/infos/"
else:
	pathLoc = "/tmp/infos/"

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

class fhdlPoster2(Renderer):

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
			self.delay2()
			eventNm = REGEX.sub('', self.event.getEventName()).strip().replace('ё','е')
			pstrNm = "{}{}.jpg".format(path_folder, eventNm)
			if not os.path.exists(pstrNm):
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
			url_tmdb = "http://api.tmdb.org/3/search/{}?api_key={}&query={}&language=en-US".format(self.srch, tmdb_api, quote(eventNm))
			if self.year != None:
				url_tmdb += "&year={}".format(self.year)
				poster = json.load(urlopen(url_tmdb))["results"][0]["poster_path"]
				rating =json.load(urlopen(url_tmdb))["results"][0]["vote_average"]
				
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
					dwn_poster = "{}{}.jpg".format(path_folder, eventNm)
					#fd = urllib1.urlopen(url_poster)
					#image_file = io.BytesIO(fd.read())
					w = 50 # 100 pixels wide
					h = 256 # 100 pixels high
					img = Image.new('RGB', (w, h))
					img = Image.open(R"/usr/share/enigma2/MetrixHD/stars.png")
					draw=ImageDraw.Draw(img)
					draw.text((4, 0),rating,font=font,fill="#000")
					rt=(h-50)*(100-float(rating)*10)/100+50
					draw.rectangle(((0, 50), (50, rt)), fill="#888785")
					img.save(dwn_poster)
					'''with open(dwn_poster, "wb") as f:
						f.write(urlopen(url_poster).read())'''
		except:
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
		'''with open(r'/tmp/posterr.txt','w') as f:
			f.write('')'''
		for i in events:
			titleNxt1 = i[4]
			eventNm1 = REGEX.sub('', titleNxt1).rstrip().replace('ё','е')
			'''with open(r'/tmp/posterr.txt','a') as f:
				f.write('\n%s' % eventNm1)'''
		for i in range(19):
			titleNxt = events[i][4]
			eventNm = REGEX.sub('', titleNxt).rstrip().replace('ё','е')
			pstrNm = "{}{}.jpg".format(path_folder, eventNm)
			if not os.path.exists(pstrNm):
				self.downloadPoster(eventNm)
		return

	def delay2(self):
		self.timer = eTimer()
		self.timer.callback.append(self.dwn)
		self.timer.start(2000, True)

	def dwn(self):
		start_new_thread(self.epgs, ())