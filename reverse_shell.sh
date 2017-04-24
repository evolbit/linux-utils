#!/bin/sh

A=`/usr/bin/ssh myvps netstat -lnt | grep "127.0.0.1:2222"`

if [ -n "$A" ]; then
	echo "NO ACTION" >> /home/intadm/log_reverse
else
	/usr/bin/ssh -fN myvps -R 2222:localhost:22
	D=`date`
	echo $D >> /root/log_reverse
fi
