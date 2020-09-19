export IP=10.10.174.219


==================================================

[TASK 2] - Reconnaissance

1) Scan the machine, how many ports are open?

	Answer: `2`

2) What verstion of Apache are running?

	Answer: `2.4.29`

3) What service is running on port 22?

	Answer: `SSH`

4) Find directoried on the web server using the GoBuster tool.

5) What is the hidden directory?

	Answer: `panel`


==================================================

[TASK 3] - Getting a shell

1) Find a form to upload and get a reverse shell, and find the flag.

	Answer: ``


==================================================

[IMPORTANT INFORMATION]

You can upload files to 'http://$IP/panel'
You can see those files at 'http://$IP/uploads'


==================================================

[APPROACH]

1) Run basic reconnaissance enumeration:
	
	Commands:
		1) `nmap -sC -sV -oN nmap/initial $IP`
		2) `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,sh,py -o gobuster.log`
		3) `nikto -h http://$IP | tee nikto.log`

2) Originally tried uploading my php-reverse-shell.php script, but got denied because PHP file types are not allowed. Then I read the hint and it said to look into File Upload Bypass. And thats where I left off; trying to get that to work. 
