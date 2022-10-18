import re
import requests
import urllib

query = "De la apusul la răsăritul soarelui 2 imdb"
query = query.replace(' ', '+')
URL = "https://google.com/search?q="+query
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent" : USER_AGENT}
resp = requests.get(URL, headers=headers)
resp=resp.text.encode('ascii', 'ignore')
aa=re.findall('href="(https://www.imdb.com.*?)/"',resp)

resp1=requests.get(aa[0], headers=headers)
resp1=resp1.text.encode('ascii', 'ignore')
aa1=re.findall('href="(.*?.jpg)">',resp1)

imaf=urllib.urlretrieve(aa1[0], ('C:\Users\HERE\Desktop\images\oscupdate\\aa.jpg'))