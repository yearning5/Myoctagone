import os, subprocess, requests
import re,random,string
from bs4 import BeautifulSoup
import urllib3, urllib2
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}

def socks_4c(ccc=None):
    if not ccc:
        ccc='ALL'
    lis=['AF = Afghanistan', 'AL = Albania', 'DZ = Algeria', 'AX = Aland Islands', 'AS = American Samoa', 'AI = Anguilla', 'AD = Andorra', 'AO = Angola', 'AN = Antilles - Netherlands ', 'AG = Antigua and Barbuda', 'AQ = Antarctica', 'AR = Argentina', 'AM = Armenia', 'AU = Australia', 'AT = Austria', 'AW = Aruba', 'AZ = Azerbaijan', 'BA = Bosnia and Herzegovina', 'BB = Barbados', 'BD = Bangladesh', 'BE = Belgium', 'BF = Burkina Faso', 'BG = Bulgaria', 'BH = Bahrain', 'BI = Burundi', 'BJ = Benin', 'BM = Bermuda', 'BN = Brunei Darussalam', 'BO = Bolivia', 'BR = Brazil', 'BS = Bahamas', 'BT = Bhutan', 'BV = Bouvet Island', 'BW = Botswana', 'BV = Belarus', 'BZ = Belize', 'KH = Cambodia', 'CM = Cameroon', 'CA = Canada', 'CV = Cape Verde', 'CF = Central African Republic', 'TD = Chad', 'CL = Chile', 'CN = China', 'CX = Christmas Island', 'CC = Cocos (Keeling) Islands', 'CO = Colombia', 'CG = Congo', "CI = Cote D'Ivoire (Ivory Coast)", 'CK = Cook Islands', 'CR = Costa Rica', 'HR = Croatia (Hrvatska)', 'CU = Cuba', 'CY = Cyprus', 'CZ = Czech Republic', 'CD = Democratic Republic of the Congo', 'DJ = Djibouti', 'DK = Denmark', 'DM = Dominica', 'DO = Dominican Republic', 'EC = Ecuador', 'EG = Egypt', 'SV = El Salvador', 'TP = East Timor', 'EE = Estonia', 'GQ = Equatorial Guinea', 'ER = Eritrea', 'ET = Ethiopia', 'FI = Finland', 'FJ = Fiji', 'FK = Falkland Islands (Malvinas)', 'FM = Federated States of Micronesia', 'FO = Faroe Islands', 'FR = France', 'FX = France, Metropolitan', 'GF = French Guiana', 'PF = French Polynesia', 'GA = Gabon', 'GM = Gambia', 'DE = Germany', 'GH = Ghana', 'GI = Gibraltar', 'GB = Great Britain (UK)', 'GD = Grenada', 'GE = Georgia', 'GR = Greece', 'GL = Greenland', 'GN = Guinea', 'GP = Guadeloupe', 'GS = S. Georgia and S. Sandwich Islands', 'GT = Guatemala', 'GU = Guam', 'GW = Guinea-Bissau', 'GY = Guyana', 'HK = Hong Kong', 'HM = Heard Island and McDonald Islands', 'HN = Honduras', 'HT = Haiti', 'HU = Hungary', 'ID = Indonesia', 'IE = Ireland', 'IL = Israel', 'IN = India', 'IO = British Indian Ocean Territory', 'IQ = Iraq', 'IR = Iran', 'IT = Italy', 'JM = Jamaica', 'JO = Jordan', 'JP = Japan', 'KE = Kenya', 'KG = Kyrgyzstan', 'KI = Kiribati', 'KM = Comoros', 'KN = Saint Kitts and Nevis', 'KP = Korea (North)', 'KR = Korea (South)', 'KW = Kuwait', 'KY = Cayman Islands', 'KZ = Kazakhstan', 'LA = Laos', 'LB = Lebanon', 'LC = Saint Lucia', 'LI = Liechtenstein', 'LK = Sri Lanka', 'LR = Liberia', 'LS = Lesotho', 'LT = Lithuania', 'LU = Luxembourg', 'LV = Latvia', 'LY = Libya', 'MK = Macedonia', 'MO = Macao', 'MG = Madagascar', 'MY = Malaysia', 'ML = Mali', 'MW = Malawi', 'MR = Mauritania', 'MH = Marshall Islands', 'MQ = Martinique', 'MU = Mauritius', 'YT = Mayotte', 'MT = Malta', 'MX = Mexico', 'MA = Morocco', 'MC = Monaco', 'MD = Moldova', 'MN = Mongolia', 'MM = Myanmar', 'MP = Northern Mariana Islands', 'MS = Montserrat', 'MV = Maldives', 'MZ = Mozambique', 'NA = Namibia', 'NC = New Caledonia', 'NE = Niger', 'NF = Norfolk Island', 'NG = Nigeria', 'NI = Nicaragua', 'NL = Netherlands', 'NO = Norway', 'NP = Nepal', 'NR = Nauru', 'NU = Niue', 'NZ = New Zealand (Aotearoa)', 'OM = Oman', 'PA = Panama', 'PE = Peru', 'PG = Papua New Guinea', 'PH = Philippines', 'PK = Pakistan', 'PL = Poland', 'PM = Saint Pierre and Miquelon', 'CS = Serbia and Montenegro', 'PN = Pitcairn', 'PR = Puerto Rico', 'PS = Palestinian Territory', 'PT = Portugal', 'PW = Palau', 'PY = Paraguay', 'QA = Qatar', 'RE = Reunion', 'RO = Romania', 'RU = Russian Federation', 'RW = Rwanda', 'SA = Saudi Arabia', 'WS = Samoa', 'SH = Saint Helena', 'VC = Saint Vincent and the Grenadines', 'SM = San Marino', 'ST = Sao Tome and Principe', 'SN = Senegal', 'SC = Seychelles', 'SL = Sierra Leone', 'SG = Singapore', 'SK = Slovakia', 'SI = Slovenia', 'SB = Solomon Islands', 'SO = Somalia', 'ZA = South Africa', 'ES = Spain', 'SD = Sudan', 'SR = Suriname', 'SJ = Svalbard and Jan Mayen', 'SE = Sweden', 'CH = Switzerland', 'SY = Syria', 'SU = USSR (former)', 'SZ = Swaziland', 'TW = Taiwan', 'TZ = Tanzania', 'TJ = Tajikistan', 'TH = Thailand', 'TL = Timor-Leste', 'TG = Togo', 'TK = Tokelau', 'TO = Tonga', 'TT = Trinidad and Tobago', 'TN = Tunisia', 'TR = Turkey', 'TM = Turkmenistan', 'TC = Turks and Caicos Islands', 'TV = Tuvalu', 'UA = Ukraine', 'UG = Uganda', 'AE = United Arab Emirates', 'UK = United Kingdom', 'US = United States', 'UM = United States Minor Outlying Islands', 'UY = Uruguay', 'UZ = Uzbekistan', 'VU = Vanuatu', 'VA = Vatican City State', 'VE = Venezuela', 'VG = Virgin Islands (British)', 'VI = Virgin Islands (U.S.)', 'VN = Viet Nam', 'WF = Wallis and Futuna', 'EH = Western Sahara', 'YE = Yemen', 'YU = Yugoslavia (former)', 'ZM = Zambia', 'ZR = Zaire (former)', 'ZW = Zimbabwe']
    d1=subprocess.check_output('curl "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country='+ccc+'"',shell=True).split()
    lisst=[]
    random.shuffle(d1)
    for i in d1:
        try:
            a=os.popen('curl -L -s --max-time 3 --socks4 '+i+' ip-api.com/json').read()
            if a:
                c=eval(a)['country']
                ip=eval(a)['query']
                cit_reg=eval(a)['city']+'_'+eval(a)['regionName']
                lisst.append(i)
                out=[i,ip,cit_reg,c]
                break
        except:
            pass
    try:
        return out
    except:
        return ''
        #print i
name='jokertv'
stream='5002'
user1=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
bb=socks_4c()
cmd='curl -L --cookie-jar --socks4 '+bb[0]+' http://www.jokertv.link/iptv/index.php --data-raw "user='+user1+'&server=1"'
b=os.popen(cmd).read()
lin2=re.findall(r' class="btn btn-danger" href="(.*?)"',b,re.DOTALL)[0]
ez=os.popen('curl -L --cookie-jar --socks4 '+bb[0]+' "'+lin2+'"').read().split('\n')

for i in range(len(ez)):
    if ez[i].find('EXTINF')>-1:
        count=i
        break
if os.path.isfile('/etc/enigma2/userbouquet.'+name+'__tv_.tv'):
    os.remove('/etc/enigma2/userbouquet.'+name+'__tv_.tv')
    file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
    file.close()
file=open('/etc/enigma2/userbouquet.'+name+'__tv_.tv','w')
file.write('#NAME '+name+' (TV)\n')

while i <len(ez)-1:
        channel=ez[i].strip('\n').split(',')[1].replace(':','')
        channel=channel.strip('\r')
        a1=ez[i+1].strip('\n')
        a1=a1.strip('\r')
        a=a1.replace(':','%3a')+':'+channel+'\n'
        channelurl='#SERVICE '+stream+':0:1:0:0:0:0:0:0:0:'+a
        file.write(channelurl)
        file.write('#DESCRIPTION '+channel+'\n')
        i = i+2
file.close()

bouq=open('/etc/enigma2/bouquets.tv','r')
bo=bouq.read()
bouq.close()
if name not in bo:
    new='#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.'+name+'__tv_.tv" ORDER BY bouquet\n'
    file=open('/etc/enigma2/bouquets.tv','a')
    file.write(new)
    file.close()