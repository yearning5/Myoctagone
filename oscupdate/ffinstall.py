#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform
import os
import re

INSTALL_BASE = '/iptvplayer_rootfs/'
MSG_FORMAT = "\n\n=====================================================\n{0}\n=====================================================\n"

def printWRN(txt):
    print(MSG_FORMAT.format(txt))
    
def printMSG(txt):
    print(MSG_FORMAT.format(txt))

def printDBG(txt):
    print(str(txt))

def ReadGnuMIPSABIFP(elfFileName):
    SHT_GNU_ATTRIBUTES=0x6ffffff5
    SHT_MIPS_ABIFLAGS=0x7000002a
    Tag_GNU_MIPS_ABI_FP=4
    Val_GNU_MIPS_ABI_FP_ANY=0
    Val_GNU_MIPS_ABI_FP_DOUBLE=1
    Val_GNU_MIPS_ABI_FP_SINGLE=2
    Val_GNU_MIPS_ABI_FP_SOFT=3
    Val_GNU_MIPS_ABI_FP_OLD_64=4
    Val_GNU_MIPS_ABI_FP_XX=5
    Val_GNU_MIPS_ABI_FP_64=6
    Val_GNU_MIPS_ABI_FP_64A=7
    Val_GNU_MIPS_ABI_FP_NAN2008=8

    def _readUint16(tmp):
        return ord(tmp[1]) << 8 | ord(tmp[0])
    
    def _readUint32(tmp):
        return ord(tmp[3]) << 24 | ord(tmp[2]) << 16 | ord(tmp[1]) << 8 | ord(tmp[0])
    
    def _readLeb128(data, start, end):
        result = 0
        numRead = 0
        shift = 0
        byte = 0

        while start < end:
            byte = ord(data[start])
            numRead += 1

            result |= (byte & 0x7f) << shift

            shift += 7
            if byte < 0x80:
                break
        return numRead, result
    
    def _getStr(stsTable, idx):
        val = ''
        while stsTable[idx] != '\0':
            val += stsTable[idx]
            idx += 1
        return val
    
    Val_HAS_MIPS_ABI_FLAGS = False
    Val_GNU_MIPS_ABI_FP = -1
    with open(elfFileName, "rb") as file:
        # e_shoff - Start of section headers
        file.seek(32)
        shoff = _readUint32(file.read(4))
    
        # e_shentsize - Size of section headers
        file.seek(46)
        shentsize = _readUint16(file.read(2))
        
        # e_shnum -  Number of section headers
        shnum = _readUint16(file.read(2))
        
        # e_shstrndx - Section header string table index
        shstrndx = _readUint16(file.read(2))
        
        # read .shstrtab section header
        headerOffset = shoff + shstrndx * shentsize
        
        file.seek(headerOffset + 16)
        offset = _readUint32(file.read(4))
        size = _readUint32(file.read(4))
        
        file.seek(offset)
        secNameStrTable = file.read(size)
        
        for idx in range(shnum):
            offset = shoff + idx * shentsize
            file.seek(offset)
            sh_name = _readUint32(file.read(4))
            sh_type = _readUint32(file.read(4))
            if sh_type == SHT_GNU_ATTRIBUTES:
                file.seek(offset + 16)
                sh_offset = _readUint32(file.read(4))
                sh_size   = _readUint32(file.read(4))
                file.seek(sh_offset)
                contents = file.read(sh_size)
                p = 0
                if contents.startswith('A'):
                    p += 1
                    sectionLen = sh_size -1
                    while sectionLen > 0:
                        attrLen = _readUint32(contents[p:])
                        p += 4
                        
                        if attrLen > sectionLen:
                            attrLen = sectionLen
                        elif attrLen < 5:
                            break
                        sectionLen -= attrLen
                        attrLen -= 4
                        attrName =  _getStr(contents, p)
                        
                        p += len(attrName) + 1
                        attrLen -= len(attrName) + 1
                        
                        while attrLen > 0 and p < len(contents):
                            if attrLen < 6:
                                sectionLen = 0
                                break
                            tag = ord(contents[p])
                            p += 1
                            size = _readUint32(contents[p:])
                            if size > attrLen:
                                size = attrLen
                            if size < 6:
                                sectionLen = 0
                                break
                                
                            attrLen -= size
                            end = p + size - 1
                            p += 4
                            
                            if tag == 1 and attrName == "gnu": #File Attributes
                                while p < end:
                                    # display_gnu_attribute
                                      numRead, tag = _readLeb128(contents, p, end)
                                      p += numRead
                                      if tag == Tag_GNU_MIPS_ABI_FP:
                                        numRead, val = _readLeb128(contents, p, end)
                                        p += numRead
                                        Val_GNU_MIPS_ABI_FP = val
                                        break
                            elif p < end:
                                p = end
                            else:
                                attrLen = 0
            elif sh_type == SHT_MIPS_ABIFLAGS:
                Val_HAS_MIPS_ABI_FLAGS = True
    return Val_HAS_MIPS_ABI_FLAGS, Val_GNU_MIPS_ABI_FP

# check free size in the rootfs
s = os.statvfs("/")
freeSpaceMB = s.f_bfree * s.f_frsize / (1024*1024) # in KB
availSpaceMB = s.f_bavail * s.f_frsize / (1024*1024) # in KB

requiredFreeSpaceMB = 12
printDBG("Free space %s MB in rootfs" % (availSpaceMB))
if availSpaceMB < requiredFreeSpaceMB:
    msg = "Not enough disk space for installing ffmpeg libraties!\nAt least %s MB is required.\nYou have %s MB free space in the rootfs.\nDo you want to continue anyway?" % (requiredFreeSpaceMB, availSpaceMB)
    answer = 'Y'
    while answer not in ['Y', 'N']:
        answer = raw_input(MSG_FORMAT.format(msg) + "\nY/N: ").strip().upper()
        msg = ''
    
    if answer != 'Y':
        raise Exception("Not enough disk space for installing ffmpeg libraties!\nAt least %s MB is required." % requiredFreeSpaceMB)
    

iptvPlatform = ''
iptvOpenSSLVer = ''

machine = platform.uname()[4]

printDBG("Machine: %s" % machine)

iptvPlatform = ''
if 'armv7' in machine:  iptvPlatform = "armv7"
elif 'sh4' in machine:  iptvPlatform = "sh4"
elif 'mips' in machine: iptvPlatform = "mipsel"
elif 'x86_64' in machine: iptvPlatform = "i686"
elif 'i686' in machine: iptvPlatform = "i686"

if iptvPlatform == '':
    with open('/proc/cpuinfo', "r") as file:
        data = file.read().lower()
        if " mips" in data: 
            iptvPlatform = "mipsel"
        elif "armv7" in data:
            iptvPlatform = "armv7"

if iptvPlatform == '':
    raise Exception('Your platform has not been detected! Machine [%s].\n' % machine)
elif iptvPlatform not in ['armv7', 'sh4', 'mipsel']: 
    raise Exception('Your platform "%s" is not supported!' % iptvPlatform)

libsslPath = ''
libcryptoPath = ''
for ver in ['1.0.2', '1.0.0', '0.9.8']:
    libsslExist = False
    libcryptoExist = False
    libsslPath = ''
    libcryptoPath = ''
    for path in ['/usr/lib/', '/lib/', '/usr/local/lib/', '/local/lib/', '/lib/i386-linux-gnu/']:
        filePath = path + 'libssl.so.' + ver
        if os.path.isfile(filePath) and not os.path.islink(filePath):
            libsslExist = True
            libsslPath = path
        
        filePath = path + 'libcrypto.so.' + ver
        if os.path.isfile(filePath) and not os.path.islink(filePath):
            libcryptoExist = True
            libcryptoPath = path
        
        if libsslExist and libcryptoExist:
            iptvOpenSSLVer = ver
            break
    
    if iptvOpenSSLVer != '':
        break

printDBG("OpenSSL SONAME VERSION [%s]" % iptvOpenSSLVer)
if iptvOpenSSLVer == '1.0.2':
    linksTab = []
    symlinksText = []
    if not os.path.isfile(libsslPath + 'libssl.so.' + iptvOpenSSLVer):
        linksTab.append((libsslPath + 'libssl.so.' + iptvOpenSSLVer, libsslPath + 'libssl.so.1.0.0'))
        symlinksText.append('%s -> %s' % linksTab[-1])
    
    if not os.path.isfile(libcryptoPath + 'libcrypto.so.' + iptvOpenSSLVer):
        linksTab.append((libcryptoPath + 'libcrypto.so.' + iptvOpenSSLVer, libcryptoPath + 'libcrypto.so.1.0.0'))
        symlinksText.append('%s -> %s' % linksTab[-1])
    
    if len(linksTab):
        msg = "OpenSSL in your image has different library names then these used by E2iPlayer.\nThere is need to create following symlinks:\n%s\nto be able to install binary components from E2iPlayer server.\nDo you want to proceed?" % ('\n'.join(symlinksText))
        answer = 'Y'
        while answer not in ['Y', 'N']:
            answer = raw_input(MSG_FORMAT.format(msg) + "\nY/N: ").strip().upper()
            msg = ''
        
        if answer == 'Y':
            for item in linksTab:
                os.symlink(item[0], item[1])
        else:
            raise Exception('Your OpenSSL version is not supported!')
elif iptvOpenSSLVer == '1.0.0':
    with open(libsslPath + 'libssl.so.' + iptvOpenSSLVer, "rb") as file:
        if 'OPENSSL_1.0.2' in file.read():
            iptvOpenSSLVer = '1.0.2'

printDBG("OpenSSL VERSION [%s]" % iptvOpenSSLVer)
if iptvOpenSSLVer == '':
    raise Exception('Problem with OpenSSL version detection!')

fpuType = ''
if iptvPlatform == "mipsel":
    hasAbiFlags, abiFP = ReadGnuMIPSABIFP('/lib/libc.so.6')
    if abiFP not in [-1, 0]:
        if abiFP == 3: fpuType = "soft"
        else: fpuType = "hard"
    if fpuType == '':
        raise Exception('Unknown FPU type!')
    printDBG("MIPSEL FPU TYPE [%s]" % fpuType)
else:
    fpuType = 'hard'
    
data = os.path.realpath('/lib/libc.so.6')
glibcVer = re.compile('\-([0-9\.]+?)\.so').search(data).group(1)
if glibcVer.count('.') > 1:
    glibcVer = glibcVer.rsplit('.', 1)[0]

glibcVer = float(glibcVer)
printDBG("glibc version [%s]" % glibcVer)

# select valid package

#iptvPlatform
#fpuType
#availSpaceMB
#iptvOpenSSLVer
#glibcVer

if glibcVer < 2.20:
    installOld = 'old_'
else:
    installOld = ''

if iptvPlatform == 'sh4':
    installFPU = ''
else:
    installFPU = 'fpu_%s_' % fpuType

if iptvOpenSSLVer in ['1.0.0', '1.0.2']:
    installSSLVer = '1.0.2'
else:
    installSSLVer = '0.9.8'

ffmpegPackageConfig = '%s_%s%sopenssl%s' % (iptvPlatform, installOld, installFPU, installSSLVer)
ffmpegInstallPackage = 'ffmpeg3.4.2_%s_dash_librtmp_native_rtmp.tar.gz' % ffmpegPackageConfig
if ffmpegPackageConfig not in ['armv7_fpu_hard_openssl1.0.2', 'mipsel_fpu_hard_openssl1.0.2', \
                               'mipsel_fpu_soft_openssl1.0.2', 'mipsel_old_fpu_hard_openssl0.9.8', \
                               'mipsel_old_fpu_soft_openssl1.0.2', 'mipsel_old_fpu_hard_openssl1.0.2', \
                               'sh4_old_openssl1.0.2', 'sh4_openssl1.0.2']:
    raise Exception('At now there is no\n"%s"\npackage available!\nYou can request it via e-mail: IPTVPlayerE2@gmail.com' % ffmpegInstallPackage)

printDBG("Slected ffmpeg package: %s" % ffmpegInstallPackage)


def HasFFmpeg():
    hasFFmpeg = False
    try:
        file = os.popen(INSTALL_BASE + 'usr/bin/ffmpeg -version')
        data = file.read()
        ret = file.close()
        if ret in [0, None]:
            hasFFmpeg = True
    except Exception,e:
        printDBG(e)
    return hasFFmpeg

if HasFFmpeg():
    msg = 'Old ffmpeg installation has been detected in "%s"\nDo you want to remove it?' % INSTALL_BASE
    answer = 'Y'
    while answer not in ['Y', 'N']:
        answer = raw_input(MSG_FORMAT.format(msg) + "\nY/N: ").strip().upper()
        msg = ''
    
    if answer == 'Y':
        ret = os.system("rm -f %s/usr/bin/ffmpeg && cd %s/usr/lib/ && rm -f libavcodec.so* libavdevice.so* libavfilter.so* libavformat.so* libavutil.so* libswresample.so* libswscale.so*" % (INSTALL_BASE, INSTALL_BASE))
        if ret not in [None, 0]:
            printWRN("Cleanup of the old ffmpeg installation failed! Return code: %s" % ret)
            
ret = os.system("mkdir -p %s" % INSTALL_BASE)
if ret not in [None, 0]:
    raise Exception('Creating %s failed! Return code: %s' % (INSTALL_BASE, ret))

WGET = ''
for cmd in ['wget', 'fullwget', '/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/bin/wget']:
    try:
        file = os.popen(cmd + ' --no-check-certificate "http://e2iplayer.pkteam.pl/precompiled/raw/master/ffmpeg3.4.2/%s" -O "/tmp/%s" ' % (ffmpegInstallPackage, ffmpegInstallPackage))
        data = file.read()
        ret = file.close()
        if ret in [0, None]:
            WGET = cmd
            break
        else:
            printDBG("Download using %s failed with return code: %s" % ret)
    except Exception,e:
        printDBG(e)

if WGET == '':
    raise Exception('Download package %s failed!' % ffmpegInstallPackage)

msg = 'Package %s ready to install.\nDo you want to proceed?' % ffmpegInstallPackage
answer = 'Y'
while answer not in ['Y', 'N']:
    answer = raw_input(MSG_FORMAT.format(msg) + "\nY/N: ").strip().upper()
    msg = ''

if answer == 'Y':
    ret = os.system("mkdir -p %s && tar -xvf /tmp/%s -C %s " % (INSTALL_BASE, ffmpegInstallPackage, INSTALL_BASE))

os.system('rm -f /tmp/%s' % ffmpegInstallPackage)

if ret not in [None, 0]:
    raise Exception('FFmpeg installation failed with return code: %s' % (ret))
    
if answer == 'Y':
    if HasFFmpeg():
        exteplayer3Paths = ['/usr/bin/exteplayer3', '/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/bin/exteplayer3']
        exteplayer3Detected = False
        if os.path.isfile(exteplayer3Paths[0]) or os.path.isfile(exteplayer3Paths[1]):
            msg = 'Old exteplayer3 binary detected. You should remove it. After restart E2iPlayer will install new one.\nDo you want to proceed?'
            answer = 'Y'
            while answer not in ['Y', 'N']:
                answer = raw_input(MSG_FORMAT.format(msg) + "\nY/N: ").strip().upper()
                msg = ''
            if answer == 'Y':
                os.system('rm -f %s' % exteplayer3Paths[0])
                os.system('rm -f %s' % exteplayer3Paths[1])
        os.system('sync')
        printMSG("Done.\nPlease remember to restart your Enigma2.")
    else:
        raise Exception('Installed ffmpeg is NOT working correctly!')



# cd /tmp && rm -f ffinstall.py && wget http://www.iptvplayer.gitlab.io/ffinstall.py && python ffinstall.py

