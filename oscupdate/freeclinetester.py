import requests

def testccam(cline):
    try:
        #cline="C: s2.satbox.xyz 18801 satbox1000 jazair03"
        cookies = {
            '__cfduid': 'd930257e2e53496f70d8c07d0c26acd9a1617359489',
            '_ga': 'GA1.2.284948668.1617359492',
            '_gid': 'GA1.2.1589687749.1617359492',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'http://www.freecline.com',
            'Alt-Used': 'www.freecline.com:443',
            'Connection': 'keep-alive',
            'Referer': 'http://www.freecline.com/index',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
        }


        data = '{"servers":[{"host":"'+cline.split()[1]+'","port":"'+cline.split()[2]+'","lines":["'+cline+'"]}],"share":false}'

        response = requests.post('http://www.freecline.com/check', headers=headers, cookies=cookies, data=data,timeout=5)
        a=response.text.encode('ascii','ignore')
        res=eval(a)['status'][0]['status']
        if res==1:
            return True
        else:
            return False
    except:
        return False




