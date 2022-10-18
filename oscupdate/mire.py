import requests, re

cookies = {
    'eTagAB': '45',
    's_fid': '04C29698549F304D-0CC2E027C31AC910',
    'authent': '1_undefined',
    's_cc': 'true',
    'eTgdpr': '7',
    'eTiab2': 'CPIXALUPIXALUBPACBFRBgCsAP_AAH_AAAqIIAtf_X__b3_n-_79__t0eY1f9_7_v-0zjhfdt-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7______7________________________-_____9____________9_ggC1_9f_9vf-f7_v3_-3R5jV_3_v-_7TOOF9237w3Z_9f8vxf_Yzu8Xfqmvgq5HiS7dsEhB20c6dxNSbHqiVWtM-xuTYyvs0ons-Saext7Z1gYf3-f3dP9kpnv______v________________________7_____3____________3-AAA',
    'evar28': '2_224637523_334161334',
    'eTab389': '1',
    'eTab313': '2',
    'eTab320': '1',
    'eTab411': '2',
    'eTagUI': '^>BOL^>^#',
    'gpv_p41': 'Web^%^2FADSL^%^2FBoutique^%^2FMire^%^2FMireipadsl^%^2FResultat',
    's_cmCat': '18803:SEO^|18803:Autres+sites^|18803:SEO^|18803:Autres+sites^|18804:SEO^|18804:Autres+sites',
    's_cmDet': '18803:SEO+Inconnu^|18803:Autres+sites^|18803:SEO+Inconnu^|18803:Autres+sites^|18804:SEO+Inconnu^|18804:Autres+sites',
    's_cmCT': '18803:SEO+Inconnu^|18803:Autres+sites^|18803:SEO+Inconnu^|18803:Autres+sites^|18804:SEO+Inconnu^|18804:Autres+sites',
    's_depth': '16',
    'eTagLV': '27078898',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6',
}

response = requests.get('http://mire.ipadsl.net/speedtest.php', headers=headers, cookies=cookies, verify=False).text
a=re.findall('alt="Votre Bande Passante(.*?)>',response)[0].encode('ascii','ignore').strip().split(' ')
a1=float(a[0])/1000
print 'Votre Bande Passante:\n Mire:\n\n'+str(a1)+'  Mb/s'


