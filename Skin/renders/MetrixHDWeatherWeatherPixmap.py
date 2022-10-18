# by nikolasi for MetrixHD
#          <widget source="session.CurrentService" render="MetrixHDWeatherWeatherPixmap" position="156,50" size="50,50" alphatest="blend" zPosition="9">
#              <convert type="MetrixHDWeather">currentWeatherCode</convert>
#              </convert>
#          </widget>	
from Tools.LoadPixmap import LoadPixmap 
from Renderer import Renderer 
from enigma import ePixmap, eTimer 
from Tools.Directories import fileExists, pathExists
import os

class MetrixHDWeatherWeatherPixmap(Renderer):
	__module__ = __name__
        
        searchPaths = ('/media/usb/%s/', '/usr/share/enigma2/MetrixHD/%s/' ,'/usr/share/enigma2/%s/', '/media/hdd/%s/')
	
	def __init__(self):                
		Renderer.__init__(self)
		#self.path = '/media/hdd/AnimatedWeatherPixmap'
		self.path = 'AnimatedWeatherPixmap'
		self.pixdelay = 100
		self.slideicon = None
		
	def applySkin(self, desktop, parent):
		attribs = []
		for (attrib, value,) in self.skinAttributes:
		        if attrib == "path":
			      self.path = value                         
			elif attrib == "pixdelay":
				self.pixdelay = int(value)								
			else:
				attribs.append((attrib, value))
				
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, parent)
		
	GUI_WIDGET = ePixmap
	
	def changed(self, what):                   
	    if self.instance:
		sname = ''
		if (what[0] != self.CHANGED_CLEAR):
		    sname = self.ConvertCondition(self.source.text)
                    for path in self.searchPaths:
                        if pathExists((path % self.path)):
		            self.runAnim(sname)
		        else:
                            pass                            

        def runAnim(self, id):
            global total
            animokicon = False
            for path in self.searchPaths:
                if fileExists('%s%s' % ((path % self.path), id)):
                    pathanimicon = '%s%s/a' % ((path % self.path), id)
                    path2 = '%s%s' % ((path % self.path), id)
                    dir_work = os.listdir(path2)
                    total = len(dir_work)
                    self.slideicon = total
                    animokicon = True
                else:
                    if fileExists('%sNA' % (path % self.path)):    
                        pathanimicon = '%sNA/a' % (path % self.path)
                        path2 = '%sNA'  % (path % self.path)
                        dir_work = os.listdir(path2)
                        total = len(dir_work)
                        self.slideicon = total
                        animokicon = True
            if animokicon == True:
                self.picsicon = []
                for x in range(self.slideicon):
                    self.picsicon.append(LoadPixmap(pathanimicon + str(x) + '.png'))

                self.timericon = eTimer()
                self.timericon.callback.append(self.timerEvent)
                self.timericon.start(100, True)	        
	        

        def timerEvent(self):
                if self.slideicon == 0:
                        self.slideicon = total
                if self.slideicon > total:
                        self.slideicon = total	
                self.timericon.stop()
                self.instance.setScale(1)
                try:
			self.instance.setPixmap(self.picsicon[self.slideicon - 1])
                except:
	                pass   
                self.slideicon = self.slideicon - 1
                self.timericon.start(self.pixdelay, True)

	def ConvertCondition(self, c):
            condition = "NA"
            if c == "S":
                condition = "0"
            elif c == "Z":
                condition = "3"
            elif c == "U":
                condition = "5"
            elif c == "G":
                condition = "8"
            elif c == "Q":
                condition = "9"
            elif c == "R":
                condition = "11"
            elif c == "W":
                condition = "13"
            elif c == "X":
                condition = "17"
            elif c == "F":
                condition = "19"
            elif c == "L":
                condition = "20"
            elif c == "S":
                condition = "23"
            elif c == "N":
                condition = "26"
            elif c == "I":
                condition = "27"
            elif c == "H":
                condition = "28"
            elif c == "C":
                condition = "31"
            elif c == "B":
                condition = "32"
            elif c == "B":
                condition = "36"
            elif c == "0":
                condition = "37"
            elif c == 49:
                condition = "NA"
            else:
                condition = "NA"
            return str(condition)
