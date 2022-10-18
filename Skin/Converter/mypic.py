# -*- coding: utf-8 -*-


# <widget source="session.CurrentService" render="Label" position="189,397" zPosition="4" size="50,20" valign="center" halign="center" font="Regular;14" foregroundColor="foreground" transparent="1"  backgroundColor="background">
#	<convert type="RouteInfo">Info</convert>
# </widget>
#<widget source="session.CurrentService" render="Pixmap" pixmap="750HD/icons/ico_lan_on.png" position="1103,35" zPosition="1" size="28,15" transparent="1" alphatest="blend">
#    <convert type="RouteInfo">Lan  | Wifi | Modem</convert>
#    <convert type="ConditionalShowHide" />
#  </widget>


from Components.Converter.Converter import Converter
from Components.Element import cached
from enigma import  eEPGCache
import os
import re

epgcache = eEPGCache.getInstance()

if os.path.isdir("/media/hdd/xtraEvent/poster"):
	path_folder = "/media/hdd/xtraEvent/poster/"
else:
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


class mypic(Converter, object):
	Info = 0
	bar1 = 1
	bar2 = 2

	def __init__(self, type):
		Converter.__init__(self, type)
		if type == "Info":
			self.type = self.Info
		elif type == "bar1":
			self.type = self.bar1
		elif type == "bar2":
			self.type = self.bar2

	@cached
	def getBoolean(self):
		info = False
		self.event = self.source.event
		if self.event:
			#self.delay2()
			eventNm = REGEX.sub('', self.event.getEventName()).strip().replace('ё','е')
			eventNm = eventNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
			#open("/tmp/infomovie_rate.txt", "w").write(eventNm)
			pstrNm = "{}{}.jpg".format(path_folder, eventNm)
			#open("/tmp/infomovie_rate1.txt", "w").write(pstrNm)
			#if not os.path.exists(pstrNm):
			#if self.intCheck():
			#self.downloadPoster(eventNm)
			if os.path.exists(pstrNm):
				#self.instance.setPixmap(loadJPG(pstrNm))self.instance.setPixmap(loadPNG("/usr/share/enigma2/psatars/satrs_w.png"))
                		#open("/tmp/infomovie_rate.txt", "w").write("exist")
                		if self.type == self.bar1 :
                			info = True
                		elif self.type == self.bar2 :
                			info = True
		return info

	boolean = property(getBoolean)
	
	@cached
	def getText(self):
		info = ""
		self.event = self.source.event
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
                		if self.type == self.Info:
                			info = "bar1"
                		elif self.type == self.Info:
                    			info = "bar2"
		return info

	text = property(getText)

	def changed(self, what):
		Converter.changed(self, what)
