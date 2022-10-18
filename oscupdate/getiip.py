import os
import re
a=os.popen('curl -s http://ip-api.com/json').read()
ip=eval(a)['query']
c=eval(a)['country']
city=eval(a)['city']
print '\nYour IP Address is : '+ip+'\nCountry location : '+c+'\nCity : '+city
