#!/bin/sh

distro=$(grep "."  /etc/issue | tail -1 | awk '{print $1}')
echo $distro
distroVersion=$(grep "."  /etc/issue | tail -1 | awk '{print $2}' | awk -F- '{print $1}')
echo $distroVersion

