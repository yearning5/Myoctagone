#!/bin/bash
ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')