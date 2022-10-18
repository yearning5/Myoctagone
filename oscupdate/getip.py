import requests

#os.environ['PYTHONWARNINGS']="ignore:Unverified HTTPS request"
import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}


link1='https://ipecho.net/plain'
f = requests.get(link1,headers=UserAgent,timeout=10)
the_page = f.text.encode('ascii', 'ignore')
print the_page