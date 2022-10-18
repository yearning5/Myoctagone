#!/bin/bash
a=$(cat  /etc/image-version | grep -i creat)
b=$(cut -d'=' -f2 <<<"$a")
echo $b
