#/bin/bash
wget -qO- http://ipecho.net/plain | xargs echo -e "Your IP Address is:\n"

/oscupdate/speedtest --accept-license
