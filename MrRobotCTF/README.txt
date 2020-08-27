export IP=10.10.47.107


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

	Answer: ``

3) What is key 3?

	Answer: ``


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

