# shamelessly copied from pliExpertInfo (Vali, Mirakels, Littlesat)

from os import path
from Components.Converter.Converter import Converter
from Components.Element import cached
from Poll import Poll
from datetime import datetime
import os
import requests
import re
import urllib3
urllib3.disable_warnings()
import datetime

class MyMod(Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = type

#	Dday=datetime.now().strftime("%d")
#	Mmonth=datetime.now().strftime("%m")
	def getCPUtemp(self):
		info = ""
		temp = ""
		if path.exists('/proc/stb/fp/temp_sensor_avs'):
			f = open('/proc/stb/fp/temp_sensor_avs', 'r')
			temp = f.readline()
			f.close()
		elif path.exists('/proc/stb/power/avs'):
			f = open('/proc/stb/power/avs', 'r')
			temp = f.readline()
			f.close()
		elif path.exists('/proc/hisi/msp/pm_cpu'):
			try:
				for line in open('/proc/hisi/msp/pm_cpu').readlines():
					line = [x.strip() for x in line.strip().split(":")]
					if line[0] in ("Tsensor"):
						temp = line[1].split("=")
						temp = line[1].split(" ")
						temp = temp[2]
			except:
				temp = ""
		elif path.exists('/sys/devices/virtual/thermal/thermal_zone0/temp'):
			try:
				f = open('/sys/devices/virtual/thermal/thermal_zone0/temp', 'r')
				temp = f.read()
				temp = temp[:-4]
				f.close()
			except:
				temp = ""
		if temp and int(temp.replace('\n', '')) > 0:
			#info ="CPU-Temp: " + temp.replace('\n', '')  + str('\xc2\xb0') + "C"
			info = temp.replace('\n', '').replace(' ','') + str('\xc2\xb0') + "C"
			#info = _("CPU-Temp: %s") % info
		return info
	
	def tt(self,val):
		if val==1:
			return str(datetime.now().strftime("%d"))
		elif val==2:
			return str(datetime.now().strftime("%m"))
	def hijri(self,val):
		try:
			ooo=open('/usr/share/skin.txt','r')
			oo=ooo.readlines()
			ooo.close()
			if val==1:
				return oo[0]
			elif val==2:
				return oo[1]
			elif val==3:
				return oo[2]
			elif val==4:
				return oo[3]
			elif val==5:
				return oo[4]
			elif val==6:
				return oo[5]
			elif val==7:
				return oo[6]
			else:
				return ""
		except:
			return "No connection"
	
	def getMemInfo(self, value):
		result = [0,
			0,
			0,
			0]
		try:
			check = 0
			fd = open('/proc/meminfo')
			for line in fd:
				if value + 'Total' in line:
					check += 1
					result[0] = int(line.split()[1]) * 1024
				elif value + 'Free' in line:
					check += 1
					result[2] = int(line.split()[1]) * 1024
				if check > 1:
					if result[0] > 0:
						result[1] = result[0] - result[2]
						result[3] = result[1]*1./result[0]
						x="{0:.0f} %".format(result[3]*100)
						#if x>70:
							#os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
					break

			fd.close()
		except:
			pass

		return result
	
	@cached
	def getText(self):
		service = self.source.service
		if service is None:
			return ""
		info = service and service.info()

		if not info:
			return ""

		if self.type == "CPUtemp":
			return self.getCPUtemp()
		if self.type == "day":
			return self.tt(1)
		if self.type == "month":
			return self.tt(2)
		
		if self.type == "Hijri":
			return self.hijri(1)
		if self.type == "Fajr":
			return self.hijri(2)
		if self.type == "Sun":
			return self.hijri(3)
		if self.type == "Dhuhr":
			return self.hijri(4)
		if self.type == "Asr":
			return self.hijri(5)
		if self.type == "Maghrib":
			return self.hijri(6)
		if self.type == "Ishaa":
			return self.hijri(7)
		if self.type == "Memo":
			return "{0:.0f} %".format(self.getMemInfo('Mem')[3]*100)

		return _("invalid type")

	text = property(getText)