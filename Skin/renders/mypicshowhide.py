# -*- coding: utf-8 -*-
# by digiteng...04.2020
# file for skin FullHDLine by sunriser 05.2021

from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, loadPNG, eEPGCache
from Components.Pixmap import Pixmap
import os
import re
import socket



epgcache = eEPGCache.getInstance()

path_folder = "/media/hdd/poster/"




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

class mypicshowhide(Renderer):
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
			#self.delay2()
			eventNm = REGEX.sub('', self.event.getEventName()).strip().replace('ё','е')
			eventNm = eventNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
			#open("/tmp/infomovie_rate.txt", "w").write(eventNm)
			pstrNm = "{}{}.jpg".format(path_folder, eventNm)
			#if not os.path.exists(pstrNm):
				#if self.intCheck():
					#self.downloadPoster(eventNm)
			if os.path.exists(pstrNm):
				#self.instance.setPixmap(loadJPG(pstrNm))self.instance.setPixmap(loadPNG("/usr/share/enigma2/psatars/satrs_w.png"))
				self.instance.setPixmap(loadPNG("/usr/share/enigma2/psatars/satrs_w.png"))                
				self.instance.show()
		else:
			self.instance.hide()
			return

	

