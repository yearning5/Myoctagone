import os, subprocess, requests
import re,random,string
from bs4 import BeautifulSoup
import urllib, urllib3, urllib2
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}

dd=['space', '!', '"', '#', '$', '%', '&amp;', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '&lt;', '=', '&gt;', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '&nbsp;', '`', '\xc2\x81', '\xe2\x80\x9a', '\xc6\x92', '\xe2\x80\x9e', '\xe2\x80\xa6', '\xe2\x80\xa0', '\xe2\x80\xa1', '\xcb\x86', '\xe2\x80\xb0', '\xc5\xa0', '\xe2\x80\xb9', '\xc5\x92', '\xc2\x8d', '\xc5\xbd', '\xc2\x8f', '\xc2\x90', '\xe2\x80\x98', '\xe2\x80\x99', '\xe2\x80\x9c', '\xe2\x80\x9d', '\xe2\x80\xa2', '\xe2\x80\x93', '\xe2\x80\x94', '\xcb\x9c', '\xe2\x84\xa2', '\xc5\xa1', '\xe2\x80\xba', '\xc5\x93', '\xc2\x9d', '\xc5\xbe', '\xc5\xb8', '&nbsp;', '\xc2\xa1', '\xc2\xa2', '\xc2\xa3', '\xc2\xa4', '\xc2\xa5', '\xc2\xa6', '\xc2\xa7', '\xc2\xa8', '\xc2\xa9', '\xc2\xaa', '\xc2\xab', '\xc2\xac', '\xc2\xad', '\xc2\xae', '\xc2\xaf', '\xc2\xb0', '\xc2\xb1', '\xc2\xb2', '\xc2\xb3', '\xc2\xb4', '\xc2\xb5', '\xc2\xb6', '\xc2\xb7', '\xc2\xb8', '\xc2\xb9', '\xc2\xba', '\xc2\xbb', '\xc2\xbc', '\xc2\xbd', '\xc2\xbe', '\xc2\xbf', '\xc3\x80', '\xc3\x81', '\xc3\x82', '\xc3\x83', '\xc3\x84', '\xc3\x85', '\xc3\x86', '\xc3\x87', '\xc3\x88', '\xc3\x89', '\xc3\x8a', '\xc3\x8b', '\xc3\x8c', '\xc3\x8d', '\xc3\x8e', '\xc3\x8f', '\xc3\x90', '\xc3\x91', '\xc3\x92', '\xc3\x93', '\xc3\x94', '\xc3\x95', '\xc3\x96', '\xc3\x97', '\xc3\x98', '\xc3\x99', '\xc3\x9a', '\xc3\x9b', '\xc3\x9c', '\xc3\x9d', '\xc3\x9e', '\xc3\x9f', '\xc3\xa0', '\xc3\xa1', '\xc3\xa2', '\xc3\xa3', '\xc3\xa4', '\xc3\xa5', '\xc3\xa6', '\xc3\xa7', '\xc3\xa8', '\xc3\xa9', '\xc3\xaa', '\xc3\xab', '\xc3\xac', '\xc3\xad', '\xc3\xae', '\xc3\xaf', '\xc3\xb0', '\xc3\xb1', '\xc3\xb2', '\xc3\xb3', '\xc3\xb4', '\xc3\xb5', '\xc3\xb6', '\xc3\xb7', '\xc3\xb8', '\xc3\xb9', '\xc3\xba', '\xc3\xbb', '\xc3\xbc', '\xc3\xbd', '\xc3\xbe', '\xc3\xbf', 'ENQ', 'ACK', 'BS', 'SYN', 'CAN', 'SUB', 'ESC']

dd1=['%20', '%21', '%22', '%23', '%24', '%25', '%26', '%27', '%28', '%29', '%2A', '%2B', '%2C', '%2D', '%2E', '%2F', '%30', '%31', '%32', '%33', '%34', '%35', '%36', '%37', '%38', '%39', '%3A', '%3B', '%3C', '%3D', '%3E', '%3F', '%40', '%41', '%42', '%43', '%44', '%45', '%46', '%47', '%48', '%49', '%4A', '%4B', '%4C', '%4D', '%4E', '%4F', '%50', '%51', '%52', '%53', '%54', '%55', '%56', '%57', '%58', '%59', '%5A', '%5B', '%5C', '%5D', '%5E', '%5F', '%60', '%61', '%62', '%63', '%64', '%65', '%66', '%67', '%68', '%69', '%6A', '%6B', '%6C', '%6D', '%6E', '%6F', '%70', '%71', '%72', '%73', '%74', '%75', '%76', '%77', '%78', '%79', '%7A', '%7B', '%7C', '%7D', '%7E', '%7F', '%E2%82%AC', '%81', '%E2%80%9A', '%C6%92', '%E2%80%9E', '%E2%80%A6', '%E2%80%A0', '%E2%80%A1', '%CB%86', '%E2%80%B0', '%C5%A0', '%E2%80%B9', '%C5%92', '%C5%8D', '%C5%BD', '%8F', '%C2%90', '%E2%80%98', '%E2%80%99', '%E2%80%9C', '%E2%80%9D', '%E2%80%A2', '%E2%80%93', '%E2%80%94', '%CB%9C', '%E2%84', '%C5%A1', '%E2%80', '%C5%93', '%9D', '%C5%BE', '%C5%B8', '%C2%A0', '%C2%A1', '%C2%A2', '%C2%A3', '%C2%A4', '%C2%A5', '%C2%A6', '%C2%A7', '%C2%A8', '%C2%A9', '%C2%AA', '%C2%AB', '%C2%AC', '%C2%AD', '%C2%AE', '%C2%AF', '%C2%B0', '%C2%B1', '%C2%B2', '%C2%B3', '%C2%B4', '%C2%B5', '%C2%B6', '%C2%B7', '%C2%B8', '%C2%B9', '%C2%BA', '%C2%BB', '%C2%BC', '%C2%BD', '%C2%BE', '%C2%BF', '%C3%80', '%C3%81', '%C3%82', '%C3%83', '%C3%84', '%C3%85', '%C3%86', '%C3%87', '%C3%88', '%C3%89', '%C3%8A', '%C3%8B', '%C3%8C', '%C3%8D', '%C3%8E', '%C3%8F', '%C3%90', '%C3%91', '%C3%92', '%C3%93', '%C3%94', '%C3%95', '%C3%96', '%C3%97', '%C3%98', '%C3%99', '%C3%9A', '%C3%9B', '%C3%9C', '%C3%9D', '%C3%9E', '%C3%9F', '%C3%A0', '%C3%A1', '%C3%A2', '%C3%A3', '%C3%A4', '%C3%A5', '%C3%A6', '%C3%A7', '%C3%A8', '%C3%A9', '%C3%AA', '%C3%AB', '%C3%AC', '%C3%AD', '%C3%AE', '%C3%AF', '%C3%B0', '%C3%B1', '%C3%B2', '%C3%B3', '%C3%B4', '%C3%B5', '%C3%B6', '%C3%B7', '%C3%B8', '%C3%B9', '%C3%BA', '%C3%BB', '%C3%BC', '%C3%BD', '%C3%BE', '%C3%BF', '%05', '%06', '%08', '%16', '%18', '%1A', '%1B']

tt=raw_input(' sport _ arab _ france  = ').encode('utf-8')
stream=raw_input(' 4097 _ 5001 _ 5002  = ').encode('utf-8')
name='free-iptv-48_'+tt
#bouquets
bouq=open('/etc/enigma2/bouquets.tv','r')
bo=bouq.read()
bouq.close()
if name not in bo:
    new='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+name+'__tv_.tv" ORDER BY bouquet\n'
    file=open('/etc/enigma2/bouquets.tv','a')
    file.write(new)
    file.close()



a1= subprocess.check_output('curl https://free-iptv-48.blogspot.com/',shell=True)
ttt='href="(http.*?'+tt+'.*?)"'
l1=re.findall(ttt,a1)[0]
a2=subprocess.check_output('curl '+l1,shell=True)
ttt1='href="(http.*?'+tt+')"'
l2=re.findall(ttt1,a2)[0]

a3=subprocess.check_output('curl -L '+l2,shell=True)
l31=re.findall('property="og:url.*?http(.*?)"',a3)[0]

l3=re.findall('property="og:url.*?http(.*?)"',a3)
a=re.findall('(http.*)',l31)[0]
for i in range(len(dd1)):
    if dd1[i] in a:
        a=a.replace(dd1[i],dd[i])

link=a.replace('amp;','')

response = urllib.urlopen(link)
aze=response.read().split('\n')
locatf='C:\Users\HERE\Desktop\erase-me\\free-iptv-48_'+tt+'.m3u'
m3ufl = open(locatf,'w')
for line in aze:
    if line.strip():
        if '#EXTVLCOPT' not in line:
            m3ufl.write(line.replace('\r','\n'))
m3ufl.close
m3ufl = open(locatf,'r')
m3uf = m3ufl.readlines()
m3ufl.close()
# the first line containing channel name
for i in range(len(m3uf)):
    if m3uf[i].find('EXTINF')>-1:
        count=i
        break
if os.path.isfile('/etc/enigma2/userbouquet.'+name+'__tv_.tv'):
    os.remove('/etc/enigma2/userbouquet.'+name+'__tv_.tv')
    file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
file.write('#NAME '+name+' (TV)\n')
while i <len(m3uf)-1:
        channel=m3uf[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=m3uf[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+':'+channel+'\n'
        channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
file.close()

