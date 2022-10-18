#!/bin/sh
#Created By RAED 01-06-2020
#Update By RAED 14-07-2021
#Update By RAED 23-07-2021
#DESCRIPTION= This script will download and install latest version of E2iPlaye (e2iplayer + TSIPlayer)  هذا السكريبت سوف يقوم بتحميل وتثبيت اخرى نسخة لبلجن

PLUGIN_DIR="/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer"

#####  Clean tmp
rm -rf /tmp/*e2iplayer* > /dev/null 2>&1
rm -f /tmp/iptv.zip > /dev/null 2>&1


# check depends packges
if [ -f /var/lib/dpkg/status ]; then
   STATUS=/var/lib/dpkg/status
   OSTYPE=DreamOs
else
   STATUS=/var/lib/opkg/status
   OSTYPE=Dream
fi

BINARYPATH=/usr/bin
PLUGINNAME=enigma2-plugin-extensions-e2iplayer
Packagecmdwrapper=cmdwrapper
Packageduktape=duktape
Packagef4mdump=f4mdump
Packageffmpeg=ffmpeg
Packagegstifdsrc=gst-ifdsrc
Packagehlsdl=hlsdl
Packageiptvsubparser=iptvsubparser
Packagelsdir=lsdir
Packagewget=wget
Packageuchardet=uchardet
Packagertmpdump=rtmpdump

if python --version 2>&1 | grep -q '^Python 3\.'; then
	echo "You have Python3 image"
	PYTHON='python3'
	Packagee2icjson='python3-e2icjson'
	Packagepycurl='python3-pycurl'
else
	echo "You have Python2 image"
	PYTHON='python'
	Packagee2icjson='python-e2icjson'
	Packagepycurl='python-pycurl'
fi

if [ $OSTYPE = "DreamOs" ]; then
	OPKG='apt-get update'
	OPKGINSTAL='apt-get install'
	OPKGREMOVE='apt-get remove'
else
	OPKG='opkg update'
	OPKGINSTAL='opkg install'
	OPKGREMOVE='opkg remove --force-depends'
fi

echo ""
########
#if grep -qs "Package: $PLUGINNAME" cat $STATUS ; then			
#	echo "Found ($PLUGINNAME) Installed"
#else
#	$OPKG
#	$OPKGINSTAL $PLUGINNAME
#fi
#sleep 2	
if ! grep -qs "Package: $PLUGINNAME" cat $STATUS ; then
	$OPKG
	#$OPKGINSTAL $PLUGINNAME
	if grep -qs "Package: $Packagee2icjson" cat $STATUS ; then
		echo ""
	else
		echo "Need to install $Packagee2icjson"
		echo ""
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $PYTHON-e2icjson -y
		else
			$OPKGINSTAL $PYTHON-e2icjson
		fi
	fi
	if grep -qs "Package: $Packagee2icjson" cat $STATUS ; then
		echo ""
	else
		echo "Feed Missing $Packagee2icjson"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if grep -qs "Package: $Packagepycurl" cat $STATUS ; then
		echo ""
	else
		echo "Need to install $Packagepycurl"
		echo ""
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $PYTHON-pycurl -y
		else
			$OPKGINSTAL $PYTHON-pycurl
		fi
	fi
	if grep -qs "Package: $Packagepycurl" cat $STATUS ; then
		echo ""
	else
		echo "Feed Missing $Packagepycurl"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packagecmdwrapper ]; then
		echo ""
	else
		echo "Need to install $Packagecmdwrapper"
		echo ""
		$OPKGREMOVE $Packagecmdwrapper > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagecmdwrapper -y
		else
			$OPKGINSTAL $Packagecmdwrapper
		fi
	fi
	if [ -f $BINARYPATH/$Packagecmdwrapper ]; then
		echo ""
	else
		echo "Feed Missing $Packagecmdwrapper"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/duk ]; then
		echo ""
	else
		echo "Need to install $Packageduktape"
		echo ""
		$OPKGREMOVE $Packageduktape > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packageduktape -y
		else
			$OPKGINSTAL $Packageduktape
		fi
	fi
	if [ -f $BINARYPATH/duk ]; then
		echo ""
	else
		echo "Feed Missing $Packageduktape"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packagef4mdump ]; then
		echo ""
	else
		echo "Need to install $Packagef4mdump"
		echo ""
		$OPKGREMOVE $Packagef4mdump > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagef4mdump -y
		else
			$OPKGINSTAL $Packagef4mdump
		fi
	fi
	if [ -f $BINARYPATH/$Packagef4mdump ]; then
		echo ""
	else
		echo "Feed Missing $Packagef4mdump"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packageffmpeg ]; then
		echo ""
	else
		echo "Need to install $Packageffmpeg"
		echo ""
		$OPKGREMOVE $Packageffmpeg > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packageffmpeg -y
		else
			$OPKGINSTAL $Packageffmpeg
		fi
	fi
	if [ -f $BINARYPATH/$Packageffmpeg ]; then
		echo ""
	else
		echo "Feed Missing $Packageffmpeg"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f /usr/lib/gstreamer-1.0/libgstifdsrc.so ]; then
		echo ""
	else
		echo "Need to install $Packagegstifdsrc"
		echo ""
		$OPKGREMOVE $Packagegstifdsrc > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagegstifdsrc -y
		else
			$OPKGINSTAL $Packagegstifdsrc
		fi
	fi
	if [ -f /usr/lib/gstreamer-1.0/libgstifdsrc.so ]; then
		echo ""
	else
		echo "Feed Missing $Packagegstifdsrc"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packagehlsdl ]; then
		echo ""
	else
		echo "Need to install $Packagehlsdl"
		echo ""
		$OPKGREMOVE $Packagehlsdl > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagehlsdl -y
		else
			$OPKGINSTAL $Packagehlsdl
		fi
	fi
	if [ -f $BINARYPATH/$Packagehlsdl ]; then
		echo ""
	else
		echo "Feed Missing $Packagehlsdl"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f '/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/libs/iptvsubparser/_subparser.so' -o -f '/usr/lib/_subparser.so' ]; then
		echo ""
	else
		echo "Need to install $Packageiptvsubparser"
		echo ""
		$OPKGREMOVE $Packageiptvsubparser > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packageiptvsubparser -y
		else
			$OPKGINSTAL $Packageiptvsubparser
		fi
	fi
	if [ -f '/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/libs/iptvsubparser/_subparser.so' -o -f '/usr/lib/_subparser.so' ]; then
		echo ""
	else
		echo "Feed Missing $Packageiptvsubparser"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packagelsdir ]; then
		echo ""
	else
		echo "Need to install $Packagelsdir"
		echo ""
		$OPKGREMOVE $Packagelsdir > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagelsdir -y
		else
			$OPKGINSTAL $Packagelsdir
		fi
	fi
	if [ -f $BINARYPATH/$Packagelsdir ]; then
		echo ""
	else
		echo "Feed Missing $Packagelsdir"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if grep -qs "Package: $Packagewget" cat $STATUS ; then
		echo ""
	else
		echo "Need to install $Packagewget"
		echo ""
		$OPKGREMOVE $Packagewget > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagewget -y
		else
			$OPKGINSTAL $Packagewget
		fi
	fi
	if grep -qs "Package: $Packagewget" cat $STATUS ; then
		echo ""
	else
		echo "Feed Missing $Packagewget"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packageuchardet ]; then
		echo ""
	else
		echo "Need to install $Packageuchardet"
		echo ""
		$OPKGREMOVE $Packageuchardet > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packageuchardet -y
		else
			$OPKGINSTAL $Packageuchardet
		fi
	fi
	if [ -f $BINARYPATH/$Packageuchardet ]; then
		echo ""
	else
		echo "Feed Missing $Packageuchardet"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
########
	if [ -f $BINARYPATH/$Packagertmpdump ]; then
		echo ""
	else
		echo "Need to install $Packagertmpdump"
		echo ""
		$OPKGREMOVE $Packagertmpdump > /dev/null 2>&1
		if [ $OSTYPE = "DreamOs" ]; then
			$OPKGINSTAL $Packagertmpdump -y
		else
			$OPKGINSTAL $Packagertmpdump
		fi
	fi
	if [ -f $BINARYPATH/$Packagertmpdump ]; then
		echo ""
	else
		echo "Feed Missing $Packagertmpdump"
		echo "Sorry, the plugin will not be install"
		exit 1
	fi
fi
########
# remove old version
echo ""
echo "********** Downlaod and Install ((Update of e2iplayer)) **********"
echo ""
wget --no-check-certificate "https://github.com/OpenVisionE2/e2iplayer-ov/archive/master.zip" -O /tmp/e2iplayer-master.zip > /dev/null 2>&1
unzip /tmp/e2iplayer-master.zip -d /tmp/ > /dev/null 2>&1
rm -rf $PLUGIN_DIR/*
cp -rf /tmp/e2iplayer-ov-master/IPTVPlayer /usr/lib/enigma2/python/Plugins/Extensions > /dev/null 2>&1
rm -rf /tmp/e2iplayer-master* > /dev/null 2>&1
rm -f /tmp/e2iplayer-master.zip > /dev/null 2>&1
####
sed -i '/from Components.SystemInfo import BoxInfo/d' $PLUGIN_DIR/components/configextmovieplayer.py > /dev/null 2>&1
sed -i '/architecture = BoxInfo.getItem("architecture")/d' $PLUGIN_DIR/components/configextmovieplayer.py > /dev/null 2>&1
sed -i 's/if architecture != "sh4":/list.append(getConfigListEntry("    " + _("Software decoding as"), config.plugins.iptvplayer.software_decode_as))/g' $PLUGIN_DIR/components/configextmovieplayer.py > /dev/null 2>&1
sed -i '/list.append(getConfigListEntry("    " + _("Software decoding as"), config.plugins.iptvplayer.software_decode_as))/d' $PLUGIN_DIR/components/configextmovieplayer.py > /dev/null 2>&1
sed -i 's/if architecture != "sh4" and (config.plugins.iptvplayer.show_iframe.value or config.plugins.iptvplayer.use_clear_iframe.value):/if config.plugins.iptvplayer.show_iframe.value or config.plugins.iptvplayer.use_clear_iframe.value:/g' $PLUGIN_DIR/components/configextmovieplayer.py > /dev/null 2>&1
####
sed -i '/from Components.SystemInfo import BoxInfo/d' $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i '/architecture = BoxInfo.getItem("architecture")/d' $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i '/if architecture == "sh4":/,+2d' $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i "s/                        gstAdditionalParams\['iframe_continue'\] = False/                    gstAdditionalParams\['iframe_continue'\] = False/g" $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i '/if architecture == "sh4": # use default value, due to small amount of RAM/,+2d' $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i "/gstAdditionalParams\['buffer-duration'\] = -1/,+2d" $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i "s/                                gstAdditionalParams\['buffer-duration'\] = 18000 # 300min/                            gstAdditionalParams\['buffer-duration'\] = 18000 # 300min/g" $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
sed -i "s/                                gstAdditionalParams\['buffer-size'\] = 10240 # 10MB/                            gstAdditionalParams\['buffer-size'\] = 10240 # 10MB/g" $PLUGIN_DIR/components/iptvplayerwidget.py > /dev/null 2>&1
####
sed -i '/from Components.SystemInfo import BoxInfo/d' $PLUGIN_DIR/iptvdm/iptvdmui.py > /dev/null 2>&1
sed -i '/if BoxInfo.getItem("architecture") == "sh4":/,+2d' $PLUGIN_DIR/iptvdm/iptvdmui.py > /dev/null 2>&1
sed -i "s/                            additionalParams\['iframe_continue'\] = False/                        additionalParams\['iframe_continue'\] = False/g" $PLUGIN_DIR/iptvdm/iptvdmui.py > /dev/null 2>&1
####
sed -i '/from Components.SystemInfo import BoxInfo/d' $PLUGIN_DIR/tools/iptvtools.py > /dev/null 2>&1
sed -i '/if BoxInfo.getItem("architecture") != "sh4":/,+2d' $PLUGIN_DIR/tools/iptvtools.py > /dev/null 2>&1
sed -i "s/        return cmd/        return 'nice -n %d %s' % (GetNice() + factor, cmd)/g" $PLUGIN_DIR/tools/iptvtools.py > /dev/null 2>&1
#####  Download and install TSIPlayer
echo "********** Downlaod and Install ((TSIPlayer)) **********"
echo ""
wget --no-check-certificate "https://gitlab.com/Rgysoft/iptv-host-e2iplayer/-/archive/master/iptv-host-e2iplayer-master.zip" -O /tmp/iptv.zip > /dev/null 2>&1
unzip /tmp/iptv.zip -d /tmp/ > /dev/null 2>&1
cp -rf /tmp/iptv-host-e2iplayer*/IPTVPlayer /usr/lib/enigma2/python/Plugins/Extensions > /dev/null 2>&1
#####  Clean tmp
rm -rf /tmp/*e2iplayer* > /dev/null 2>&1
rm -f /tmp/iptv.zip > /dev/null 2>&1
sync
echo "config.plugins.iptvplayer.ts_xtream_user=alger25" >> /etc/enigma2/settings
echo "config.plugins.iptvplayer.ts_xtream_pass=pvbCiK4g6u" >> /etc/enigma2/settings
echo "config.plugins.iptvplayer.ts_xtream_host=tptv.cz:80" >> /etc/enigma2/settings
killall enigma2

exit 0
