#!/bin/bash
# This is the macbot.sh script. An easy script to interactively run 
# macchanger on debian distributions employing network-manager.
# Needs to be run as root.
# Thanks to Hai @ http://wuhrr.wordpress.com for the bit with select 
# and http://chris.com/ascii/index.php?art=television/futurama for the 
# ascii_art.
#
# Author: Manuel Weber (mmweber@gmx.net)


#    This is the main screen.
#    It awaits the user to select the interface to be changed.
#    Sanitizing input has yet to be implemented.

echo
echo
echo "        ###    The MAC Bot 0.1        ###"
echo
echo
echo
echo "               T        "
echo '             .-"-.        '
echo "            |  ___|        "
echo "            | (.\/.)    "
echo "            |  ,,,'     "
echo "            | '###        "
echo "             '----'        "




echo
echo
echo 'Enter the interface you want to change (eg. wlan0 or  eth0 ): '
echo


read int
#int="wlan0"

echo $int
echo
echo 'Enter the specific MAC address  XX:XX:XX:XX:XX:XX   : '
echo

read int1


ifconfig $int down
service network-manager stop
#macchanger -A $int
macchanger -m $int1 $int
echo
echo

mac=`ip link show $int | awk '/ether/ {print $2}'`


# This part asks the user which Network has to be configured.
# 
#

echo 'List of available, already used WLANs: '
echo
echo




# Changes to network directory
cd /etc/NetworkManager/system-connections/



# Change network names to be withouth space characters
rename "s/ /_/g" *



# Set the prompt for the select command
PS3="Type a number or 'q' to quit: "



# Create a list of files to display
fileList=$(find . -maxdepth 1 -type f)




# Show a menu and ask for input, then add line 12 to selected file

select fileName in $fileList; do
    if [ -n "$fileName" ]; then
        sed -i "12s/.*/cloned-mac-address=$mac/" ${fileName}
    fi
    break
done



ifconfig wlan0 up
service network-manager start

echo
echo
echo
echo "Changed MAC address of INT-x to: $mac"
echo
echo
echo

# Functionality to add to script:
# 1. Display network interfaces to choose from
# 2. Display macchangermodes, a)Custom b) Another c)random
# 3.
