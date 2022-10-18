#!/bin/bash
opkg update
opkg install util-linux
opkg install openssh-sftp-server
opkg install samba
opkg install python-pip
pip install requests
pip install --upgrade setuptools
pip install bs4
opkg install gstplayer
opkg install inadyn-mt
opkg install hlsdl
opkg install f4mdump
reboot