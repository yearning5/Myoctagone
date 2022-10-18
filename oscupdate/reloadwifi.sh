#!/bin/sh
rmmod 8192eu
rmmod cfg80211
modprobe cfg80211
modprobe 8192eu
