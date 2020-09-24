export IP=10.10.182.111


==================================================

[TASK 1] - Find the Flags

1) Deploy the VM and Start the enumeration.

2) What is the Web Directory you found?

	Answer: `2100`

3) What is the file name you found?

	Answer: `green_arrow.ticket`

4) What is the FTP password?
	
	Answer: ``

5) 


==================================================

[IMPORTANT INFORMATION]

Endpoints: 
	/island
	/island/2100
	/island/2100/green_arrow.ticket

FTP Username: vigilante	

Found some hash:	RTy8yhBQdscX
Decrypted:			_


==================================================

[APPROACH]

1) Nmap scans.

	Notes: Ports 21 (FTP), 22 (SSH), 80 (HTTP), and 111 (RPCBind) were found.

2) Gobuster. A lot of 'em.

	Commands:
		1) `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.log`
				> Found endpoint '/island'.
				> Used gobuster on that endpoint, see below.
		2) `gobuster dir -u http://$IP/island -w ./numbers_1000_to_9999.txt -o gobuster2.log`
				> Based off knowing the answer for T1-Q2 contained 4 numbers, I created a simple text file containing all numbers from 1000 to 9999 and used it as the wordlist in gobuster.
				> Found endpoint '/island/2100'.
		3) `gobuster dir -u http://$IP/island/2100 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x ticket -o gobuster3.log`
				> Based off '/island/2100' source code, I knew I had to search for a file with the extension, '.ticket', so to gobuster we went... again.
				> Found extension item '/island/2100/green_arrow.ticket'.
				> On that webpage, there was a hash: RTy8yhBQdscX.

3) Decrypt the hash.

	Notes:
		- Analyzed the hash using ''. 