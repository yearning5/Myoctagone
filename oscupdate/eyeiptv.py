import requests,re,os,random,string
usser=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
try:
    cookies = {
        'ezCMPCCS': 'true',
        '_pbjs_userid_consent_data': '3524755945110770',
        'ezosuigeneris': '26bc1700404d1f3980ab8b8c24b955de',
        'id5id.1st': '%7B%22created_at%22%3A%222021-09-12T09%3A37%3A14.172998Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOMxxEE2wcjBBBXGKmNqvzmwG3_VPLlVsL1svNUA!ID5*x74T_q7qGqLx6tKh3Ko8F6tdrSqcQaPiVmMFuks9k-EAALgBBxh-4G08FKOGuAZs%22%2C%22universal_uid%22%3A%22ID5-ZHMOvTHKmXHd-6xZV7dwcbveJz5PFzLnjv7Eu02Xdg!ID5*lU8XTnI2kJi-2qGtllDtcb68hCbxSE0zKImkxXRKzXcAAKf6YHgq6wDkfN5uXrwx%22%2C%22signature%22%3A%22ID5_AUizKMgOy_ioxuoeSdlSOnhYolnsjYvkfPbDofXpNhpG0pUzBNxR6VRoWK62CQmWLE-dJqUwqelg-BVjRkLghRQ%22%2C%22link_type%22%3A1%2C%22cascade_needed%22%3Atrue%2C%22privacy%22%3A%7B%22jurisdiction%22%3A%22other%22%2C%22id5_consent%22%3Atrue%7D%7D',
        'id5id.1st_last': 'Sun%2C%2012%20Sep%202021%2009%3A37%3A17%20GMT',
        'ezds': 'ffid%3D1%2Cw%3D1366%2Ch%3D768',
        'ezohw': 'w%3D1366%2Ch%3D223',
        '__gads': 'ID=12d783fa8e8f14e2-22bd9c151dcb00e1:T=1631439450:S=ALNI_MYCsVyIN1EAKJqdZ47ufublxcKoAA',
        '__qca': 'P0-242977151-1631439448866',
        'ezux_lpl_291153': '1631444051770|68d580df-1eff-48a4-694c-3d81a4261bda|false',
        'ezosuigenerisc': '7ea552cb405ba1dd80ee939e6de9dcd1',
        'cookieconsent_dismissed': 'yes',
        'ezoadgid_291153': '-1',
        'ezoref_291153': '',
        'ezoab_291153': 'mod70',
        'active_template::291153': 'pub_site.1631957666',
        'ezopvc_291153': '137',
        'ezepvv': '0',
        'ezovid_291153': '1887254610',
        'lp_291153': 'https://eyetv.club/',
        'ezovuuidtime_291153': '1631957666',
        'ezovuuid_291153': 'b758a591-4aac-40c0-51d8-e306674a141f',
        'PHPSESSID': 'frctlatet5m27kqfkbqc3lf4dh',
        'ezouspvv': '0',
        'ezouspva': '0',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    
    r1 = requests.get('https://eyetv.club/index.php', headers=headers, cookies=cookies)
    
    cookies = {
        'ezCMPCCS': 'true',
        '_pbjs_userid_consent_data': '3524755945110770',
        'ezosuigeneris': '26bc1700404d1f3980ab8b8c24b955de',
        'id5id.1st': '%7B%22created_at%22%3A%222021-09-12T09%3A37%3A14.172998Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOMxxEE2wcjBBBXGKmNqvzmwG3_VPLlVsL1svNUA!ID5*x74T_q7qGqLx6tKh3Ko8F6tdrSqcQaPiVmMFuks9k-EAALgBBxh-4G08FKOGuAZs%22%2C%22universal_uid%22%3A%22ID5-ZHMOvTHKmXHd-6xZV7dwcbveJz5PFzLnjv7Eu02Xdg!ID5*lU8XTnI2kJi-2qGtllDtcb68hCbxSE0zKImkxXRKzXcAAKf6YHgq6wDkfN5uXrwx%22%2C%22signature%22%3A%22ID5_AUizKMgOy_ioxuoeSdlSOnhYolnsjYvkfPbDofXpNhpG0pUzBNxR6VRoWK62CQmWLE-dJqUwqelg-BVjRkLghRQ%22%2C%22link_type%22%3A1%2C%22cascade_needed%22%3Atrue%2C%22privacy%22%3A%7B%22jurisdiction%22%3A%22other%22%2C%22id5_consent%22%3Atrue%7D%7D',
        'id5id.1st_last': 'Sun%2C%2012%20Sep%202021%2009%3A37%3A17%20GMT',
        'ezds': 'ffid%3D1%2Cw%3D1366%2Ch%3D768',
        'ezohw': 'w%3D1366%2Ch%3D415',
        '__gads': 'ID=12d783fa8e8f14e2-22bd9c151dcb00e1:T=1631439450:S=ALNI_MYCsVyIN1EAKJqdZ47ufublxcKoAA',
        '__qca': 'P0-242977151-1631439448866',
        'ezux_lpl_291153': '1631957687286|aef4894f-0b33-47c0-5c3b-e61fbf04f01e|false',
        'ezosuigenerisc': '7ea552cb405ba1dd80ee939e6de9dcd1',
        'cookieconsent_dismissed': 'yes',
        'ezoadgid_291153': '-1',
        'ezoref_291153': '',
        'ezoab_291153': 'mod70',
        'active_template::291153': 'pub_site.1631957670',
        'ezopvc_291153': '138',
        'ezepvv': '0',
        'ezovid_291153': '1887254610',
        'lp_291153': 'https://eyetv.club/',
        'ezovuuidtime_291153': '1631957670',
        'ezovuuid_291153': 'b758a591-4aac-40c0-51d8-e306674a141f',
        'PHPSESSID': 'frctlatet5m27kqfkbqc3lf4dh',
        'ezouspvv': '440',
        'ezouspva': '5',
        '_dlt': '1',
        'ezouspvh': '240',
        'cto_bundle': 'JeA-iF9KdGgxbUh3U2pPVFRCZE5SbHNrZ3RiYUhvMk5FUnVKRmloNDgzaEwxUHclMkJpWXBNek1RT2VWeVhUTkNFN2RlWUR6SkZXJTJGS1dKcERtRm8zVWZPYXlVRlolMkY2eG1WU3NiQmMlMkI4eSUyRnNBTEF6c1c5TVFJUHUxSEwyZ2tPcU15WGFGbTFFZ0Y0NCUyRlEyYlBySUU4d3lOU3J2V0ElM0QlM0Q',
        'ezux_et_291153': '31',
        'ezux_tos_291153': '133',
        'ezux_ifep_291153': 'true',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://eyetv.club',
        'Connection': 'keep-alive',
        'Referer': 'https://eyetv.club/index.php',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    
    data = {
      'username': usser,
      'bouquet': '0'
    }
    
    r2 = requests.post('https://eyetv.club/index.php', headers=headers, cookies=cookies, data=data)
    
    cookies = {
        'ezCMPCCS': 'true',
        '_pbjs_userid_consent_data': '3524755945110770',
        'ezosuigeneris': '26bc1700404d1f3980ab8b8c24b955de',
        'id5id.1st': '%7B%22created_at%22%3A%222021-09-12T09%3A37%3A14Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5*hhsXGu9PHkawT9ZFnQ848-r4qc7d5KcGF8YBXgqYlwUAAG30Ogfd4NS7_Fn9XWdo%22%2C%22universal_uid%22%3A%22ID5*ZivHbYFSQLtNvnGOZTQ9Uk3YVAUCLJ0Q2-105ocuHVQAAN6Qx1glcVm0moOcuYSs%22%2C%22signature%22%3A%22ID5_Adpd72MH4YPN1mBz-3ubJMvICq5lHulzZxseDN0RBOCV32KwEpjfc_6w3TzmjU-xmLFHwLRT2xV5nVBHI9C1gnY%22%2C%22link_type%22%3A2%2C%22cascade_needed%22%3Atrue%2C%22privacy%22%3A%7B%22jurisdiction%22%3A%22other%22%2C%22id5_consent%22%3Atrue%7D%7D',
        'id5id.1st_last': 'Sat%2C%2018%20Sep%202021%2009%3A39%3A07%20GMT',
        'ezds': 'ffid%3D1%2Cw%3D1366%2Ch%3D768',
        'ezohw': 'w%3D1366%2Ch%3D615',
        '__gads': 'ID=12d783fa8e8f14e2-22bd9c151dcb00e1:T=1631439450:S=ALNI_MYCsVyIN1EAKJqdZ47ufublxcKoAA',
        '__qca': 'P0-242977151-1631439448866',
        'ezux_lpl_291153': '1631958020518|d96e078b-272d-45ec-6846-1edc14ba273b|false',
        'ezosuigenerisc': '7ea552cb405ba1dd80ee939e6de9dcd1',
        'cookieconsent_dismissed': 'yes',
        'ezoadgid_291153': '-1',
        'ezoref_291153': '',
        'ezoab_291153': 'mod70',
        'active_template::291153': 'pub_site.1631958019',
        'ezopvc_291153': '141',
        'ezepvv': '0',
        'ezovid_291153': '1887254610',
        'lp_291153': 'https://eyetv.club/',
        'ezovuuidtime_291153': '1631958019',
        'ezovuuid_291153': 'b758a591-4aac-40c0-51d8-e306674a141f',
        'PHPSESSID': 'frctlatet5m27kqfkbqc3lf4dh',
        'ezouspvv': '0',
        'ezouspva': '3',
        '_dlt': '1',
        'ezouspvh': '240',
        'cto_bundle': 'EpwTpl9KdGgxbUh3U2pPVFRCZE5SbHNrZ3RVNWRmY043SWlmMlQlMkJwYkIycDBXb1FQTjhwMFdxZEFxRUtjUkd2d1RGUTA3SUQ2a0M4NVh5bGFCYk1qMHdmJTJCOWZOTEtCRTJ5RDBvd0ZaZlh4WUQxVVdRaWhtOWp4a0YwMWs0dVJBR1lFTlI4R29BY2J1RFpSTEV4c1RjYjgzdmp3JTNEJTNE',
        'ezux_et_291153': '127',
        'ezux_tos_291153': '339',
        'ezux_ifep_291153': 'true',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    
    params = (
        ('uri', usser),
        ('bouquet', '0'),
    )
    
    r3 = requests.get('https://eyetv.club//godownload.php', headers=headers, params=params, cookies=cookies)
    
    ll2=re.findall('value="(http://eyetv.site:8080/get.php.*?)"',r3.text,re.DOTALL)[0].replace('amp;','')
    userr=re.findall('username=(.*?)&',ll2)[0]
    passs=re.findall('password=(.*?)&',ll2)[0]
    
    with open(r'/etc/enigma2/userbouquet.eye_3days__tv_.tv','r') as f:
        ff=f.readlines()
    
    f1= open(r'/etc/enigma2/userbouquet.eye_3days__tv_.tv','w')
    print "old user : "+i.split('/')[3]
    print "old pass : "+i.split('/')[4]
    for i in ff:
        if '#SERVICE' in i:
            i=i.replace(i.split('/')[3],userr).replace(i.split('/')[4],passs)
        f1.write(i)
    f1.close()
    with open(r'/etc/enigma2/xstreamity/playlists.txt') as f:
        ff=f.read()

    u1=re.findall('http://eyetv.site.*username=(.*?)&',ff)[0]
    p1=re.findall('http://eyetv.site.*password=(.*?)&',ff)[0]
    with open(r'/etc/enigma2/xstreamity/playlists.txt','w') as f:
        f.write(ff.replace(u1,userr).replace(p1,passs))
except:
    pass

        
