export IP=10.10.12.0


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
	Notes: RUnning the above command downloaded everything that was on the SMB share (anonymous access) into my local directory. I was then able to cat out the log.txt file and see some interesting information (RSA SSH key).
	Answer: `21`

4) Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just an server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. In our case, port 111 is access to a network file system. Lets use nmap to enumerate this using the command, nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount $IP. What mount can we see?

	Command: `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount $IP`
	Answer: ``