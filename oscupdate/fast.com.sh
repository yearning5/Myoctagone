#!/bin/sh
python <<HEREDOC
import sys
sys.path.insert(1, '/oscupdate')
import fast_com
print 'your Bandwidth speed is:\n\n'+  str(fast_com.fast_com(maxtime=6))+' Mb/s\n\n'
HEREDOC