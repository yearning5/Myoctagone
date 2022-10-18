# -*- coding: utf-8 -*-
# by digiteng...02.2020
#    <widget source="session.Event_Now" render="Label" position="210,166" size="679,100" font="Regular; 14" backgroundColor="tb" zPosition="2" transparent="1" halign="left" valign="top">
#      <convert type="infoMovie">INFO</convert>
#    </widget>
#    <ePixmap pixmap="LiteHD2/star_b.png" position="0,277" size="200,20" alphatest="blend" zPosition="0" transparent="1" />
#    <widget source="session.Event_Now" render="Progress" pixmap="LiteHD2/star.png" position="0,277" size="200,20" alphatest="blend" zPosition="1" transparent="1">
#      <convert type="infoMovie">STARS</convert>
#    </widget>
from Components.Converter.Converter import Converter
from Components.Element import cached
import json
import re
import os

if os.path.isdir("/media/hdd/xtraEvent/infos/"):
	pathLoc = "/media/hdd/xtraEvent/infos/"
else:
	pathLoc = "/media/hdd/infos/"

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

class Kitte888infoMovie(Converter, object):

	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = type

	@cached
	def getText(self):
		event = self.source.event
		if event:

			#if self.type == 'INFO':
			try:
				#evnt = event.getEventName()
				#try:
					#p = '((.*?))[;=:-].*?(.*?)'
					#e1 = re.search(p, evnt)
					#ffilm = re.sub('\W+','&', e1.group(1))
				#except:
					#w = re.sub("([\(\[]).*?([\)\]])", " ", evnt)
					#ffilm = re.sub('\W+','&', w)
				eventNm = REGEX.sub('', event.getEventName()).strip().replace('ё','е')
				eventNm = eventNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
				dwnldFile = "{}{}.json".format(pathLoc, eventNm)
				with open(dwnldFile )as f:
					ff=f.read()
				data = json.loads(ff)
				rtng = data['imdbRating']
				#country = data['Country']
				year = data['Year'][:4]
				#rate = data['Rated']
				#genre = data['Genre']
				#award = data['Awards']
				if rtng == "N/A" or  rtng == "" or not rtng.replace(' ','').replace('.','').isdigit():
					rtng= ""
				else:
					rtng= str(rtng)
				if year == "N/A" or  year == "" or not year.replace(' ','').replace('.','').isdigit():
					year= ""
				else:
					year= str(year)
			except:
				rtng= ""
				year= ""
		else:
			rtng= ""
			year= ""
		if self.type == 'INFO':
			return rtng
		if self.type == 'IMDB':
			return "Imdb\n%s"%rtng
		if self.type == 'YEAR':
			return year
	text = property(getText)


	@cached
	def getValue(self):
		event = self.source.event
		if event:
			if self.type == 'STARS':
				try:
					evnt = event.getEventName()
					#try:
						#p = '((.*?))[;=:-].*?(.*?)'
						#e1 = re.search(p, evnt)
						#ffilm = re.sub('\W+','&', e1.group(1))
					#except:
						#w = re.sub("([\(\[]).*?([\)\]])", " ", evnt)
						#ffilm = re.sub('\W+','&', w)
					
					eventNm = REGEX.sub('', event.getEventName()).strip().replace('ё','е')
					eventNm = eventNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
					dwnldFile = "{}{}.json".format(pathLoc, eventNm)
					with open(dwnldFile )as f:
						ff=f.read()
					data = json.loads(ff)
					#rtng = data['imdbRating']
					#open("/tmp/infomovies1_url.txt", "w").write(url)
					rtng = data['imdbRating']
					if rtng == "N/A" or  rtng == "" or not rtng.replace(' ','').replace('.','').isdigit():
						return 0
					else:
						return int(10*(float(rtng)))
				except:
					return 0	
		else:
			return 0
			
	value = property(getValue)
	range = 100
