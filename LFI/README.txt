export IP=10.10.175.109


==================================================

[TASK 2] - Root it

1) user.txt

	Answer: `60989655118397345799`

2) root.txt

	Answer: `42964104845495153909`


==================================================

[IMPORTANT INFORMATION]

SSH Username: falconfeast
SSH Password: rootpassword

Privilege Escalation: sudo socat stdin exec:/bin/bash


==================================================

[APPROACH]

1) Nmap scan.

	Notes:
		- Just showed port 22 (SSH) and 80 (HTTP)
		- Checked out the webpage and found a simple blog. There were articles on LFI (local file inclusion) and RFI (remote file inclusion).
		- I understood the LFI stuff, but had trouble understanding how to implement RFI.

2) Gobuster.
	
	Notes: Turned up nothing.

3) Nikto.

	Notes: Turned up nothing.

4) LFI.
	
	Notes:
		- 'http://10.10.175.109/article?name=../../../../../etc/passwd'
		- Produced the server's /etc/passwd file and I found a username and password commentted out: 'falconfeast:rootpassword'

5) SSH'd into the box using the username and password.

	Commands:
		1) `sudo -l`
		2) `sudo socat stdin exec:/bin/bash`
	Notes:
		- Once in the box I ran 'sudo -l' to see if there were any simple privilege escalations and there was: '(root) NOPASSWD: /usr/bin/socat'
		- Looked up and found a command on GTFOBins. See commands section.