# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:27:48 2022

@author: guira
"""
import re

sk='''
<screen name="ClearMemInfoScreen" position="center,center" zPosition="2" size="400,580" title="ClearMem Info" backgroundColor="#31000000" >
			<widget name="memtext" font="Regular;18" position="10,0" zPosition="2" valign="center" halign="left" size="230,550" backgroundColor="#31000000" transparent="1" />
			<widget name="memvalue" font="Regular;18" position="250,0" zPosition="2" valign="center" halign="right" size="140,550" backgroundColor="#31000000" transparent="1" />
			<ePixmap pixmap="skin_default/div-h.png" position="0,550" zPosition="2" size="400,2" />
			<widget name="key_red" position="10,552" zPosition="2" size="130,28" valign="center" halign="center" font="Regular;22" transparent="1" foregroundColor="red" />
			<widget name="key_green" position="130,552" zPosition="2" size="130,28" valign="center" halign="center" font="Regular;22" transparent="1" foregroundColor="green" />
			<widget name="key_blue" position="260,552" zPosition="2" size="130,28" valign="center" halign="center" font="Regular;22" transparent="1" foregroundColor="blue" />
		</screen>
'''

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
    


def fl(n):
    try:
        float(n)
        return True
    except:
        return False

    
lk=['position','size']    
for k in lk:
    
    regg='('+k+'=".*?)"'
    po=re.findall(regg,sk)
    
    
    po1=[]
    
    for i in po:
        nn=()
        if fl(i.split(',')[0].split('"')[-1]):
            nn1=str(int(float(i.split(',')[0].split('"')[-1])*1.5))
        else:
            nn1=str(i.split(',')[0].split('"')[-1])
        
        if fl(i.split(',')[-1]):
            nn2=str(int(float(i.split(',')[-1])*1.5))
        else:
            nn2=str(i.split(',')[-1])
            
        po1.append(i.split(',')[0].split('"')[0]+'"'+nn1+','+nn2)
    
    
    po0={po[i]:po1[i] for i in range(len(po)) }
    
    sk=replace_all(sk,po0)

po=re.findall('(font=".*?)"',sk)

po1=[]
for i in po:
    
    if fl(i.split(';')[-1]):
        nn2=str(int(float(i.split(';')[-1])*1.5))
    else:
        nn2=str(i.split(';')[-1])
        
    po1.append(i.split(';')[0].split('"')[0]+'"'+';'+nn2)
po0={po[i]:po1[i] for i in range(len(po)) }

sk=replace_all(sk,po0)

print sk