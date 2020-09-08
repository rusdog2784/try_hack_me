export IP=10.10.36.12


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

	Answer: ``

6) Where can you login with the details obtained?
	
	Answer: ``

7) What's the user flag?

	Answer: ``

8) Is there any other user in the home directory? What's its name?

	Answer: ``

9) What can you leverage to spawn a privileged shell?

	Answer: ``

10) What's the root flag?

	Answer: ``


==================================================

[IMPORTANT INFORMATION]

Potential username: mike


==================================================

[APPROACH]

1) Scan using nmap:

	Command: `nmap -sV -sC -oN nmap/initial $IP`

2) Running gobuster:

	Command: `gobuster dir -u http://10.10.36.12 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,py,js,html,css -o gobuster.txt`

3) Running nikto:

	Command: `nikto -h http://$IP | tee nikto.log`

4) Found /simple from gobuster. Checked it out and it is a "CMS Made Simple version 2.2.8" website. Checking exploit-db for a CVE.

	Notes: Found CVE-2019-9053 (Unauthenticated SQL Injection; https://www.exploit-db.com/exploits/46635)

5) Tried using the CVE script, cve-2019-9053.py:

	Command: `python cve-2019-9053.py -u http://$IP/simple -w /usr/share/wordlists/best110.txt`
	Notes:
		Saved output to cve-2019-9053-output.txt.
		Didn't seem to work the first time. Gonna try adding the -c flag (crack flag).