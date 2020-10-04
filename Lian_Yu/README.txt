export IP=10.10.222.145


==================================================

[TASK 1] - Find the Flags

1) Deploy the VM and Start the enumeration.

2) What is the Web Directory you found?

	Answer: `2100`

3) What is the file name you found?

	Answer: `green_arrow.ticket`

4) What is the FTP password?
	
	Answer: `!#th3h00d`

5) What is the file name with the SSH password?

	Answer: `shado`

6) user.txt

	Answer: `THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}`

7) root.txt

	Answer: `THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}`


==================================================

[IMPORTANT INFORMATION]

Endpoints: 
	/island
	/island/2100
	/island/2100/green_arrow.ticket

FTP Username:	vigilante	
FTP Password: 	!#th3h00d

Found some hash:	RTy8yhBQdscX
Decrypted:			!#th3h00d		<- using Base58

Steganography File from FTP server:	aa.jpg
Steganography File Password:		password 	<- using steghide-crack.sh | rockyou.txt

SSH Username: 	slade
SSH Password:	M3tahuman	<- inside 'ss/shado'

ROOT ACCESS COMMAND (as slade):		sudo pkexec /bin/sh


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
		- Analyzed the hash using 'Base58' (https://gchq.github.io/CyberChef/#recipe=From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)&input=UlR5OHloQlFkc2NY).
		- '!#th3h00d'

4) Logged into FTP.

	Notes:
		- Used username, 'vigilante', and password, '!#th3h00d'.
		- There were 3 images, which I downloaded into the 'FTP' folder: aa.jpg, Leave_me_along.png, Queen's_Gambit.png.
		- Leave_me_along.png has a file error.
		- aa.jpg had steghide data inside of it.
		- [side note]: was able to navigate through the file system. Found another user, 'slade'.

5) Use Steghide to extract any data from the images.

	Command: 
		1) `sudo /root/dev/steghide-crack.sh aa.jph /usr/share/wordlists/rockyou.txt`
		2) `steghide --extract -sf aa.jpg -p password`
		3) `mv ss.zip ../ss.zip`
		4) `unzip ss.zip`
	Notes:
		- Had to run the steghide-crack.sh script to crack the steghide password protecting the aa.jpg file.
		- The password found was 'password'. Stupid.
		- An ss.zip file was extracted from the image. I move the file inside of the main 'Yian_Lu' directory and unzipped it.
		- Two files, 'passwd.txt' and 'shado', were unzipped.

6) SSH into the box.

	Commands:
		1) `sudo -l` + `M3tahuman`
		2) `sudo pkexec /bin/sh`
	Notes:
		- Used username, 'slade', and password, 'M3tahuman'.
		- Running sudo -l produced the following: '(root) PASSWD: /usr/bin/pkexec'
		- Search GTFOBins for 'pkexec' privesc exploit. Found this: 'sudo pkexec /bin/sh'.
