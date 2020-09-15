export IP=10.10.52.71


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

	Answer: ``


==================================================

[IMPORTANT INFORMATION]

SMB username = ANONYMOUS
SMB password = namelessone


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

4) Revisting FTP.

	Commands:
		1) [my machine]: `nc -lnvp 9999`
		2) [victim using clean.sh]
	Notes:
		- Noticed that the 'clean_up.sh' script gets called regularly based off what I can see inside the 'removed_files.log'.
		- Going to try to start a reverse shell using this knowledge.
		- Was having trouble getting a reverse shell using the 'clean.sh' script. Instead I went ahead and just copied '/etc/passwd' and '/home/namelessone' into the '/var/ftp/scripts' folder which allowed me to save them locally to my folder.
		# TODO: root the box