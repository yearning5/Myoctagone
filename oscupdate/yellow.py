import os

with open('/etc/enigma2/settings','r') as f:
    r=f.read().split('\n')
    
for i,s in enumerate(r):
    if 'ButtonSetup.yellow' in s:
        break
print i
print r[i]

rep='config.misc.ButtonSetup.yellow=Plugins/Extensions/Prayertimes/1,Plugins/Extensions/OscamStatus/1,Plugins/Extensions/IMDbFNC/2,Plugins/Extensions/IPTVPlayer/1,Plugins/Extensions/DreamExplorer/1,Plugins/Extensions/FileCommander/1,Plugins/Extensions/SquarDevise/1,MenuPlugin/scan/satfinder,Plugins/Extensions/TMBD/4,Plugins/Extensions/XStreamity/1,Plugins/Extensions/FootOnSat/1,ScriptRunner/'

r[i]=rep

print r[i]
with  open('/etc/enigma2/settings','w') as f:
    for i in r:
        f.write(i+'\n')

os.popen('killall -9 enigma2')