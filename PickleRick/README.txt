export IP=10.10.110.56


==================================================

[TASK 1] - Pickle Rick

1) Deploy the virtual machine on this task and explore the web application. What is the first ingredient Rick needs?

	Answer: ``

2) Whats the second ingredient Rick needs?

	Answer: ``

3) Whats the final ingredient Rick needs?

	Answer: ``


==================================================

[IMPORTANT INFORMATION]

Username:		R1ckRul3s



==================================================

[APPROACH]

1) Scan machine with nmap:

	Command: `nmap -sC -sV -oN nmap/initial $IP`
	Output:
		- Open Ports 22, 80
		- HTTP Apache 2.4.18 (Ubuntu)

2) Checked out the address: http://$IP. Viewed the source code. I found:
	
	<!--

	Note to self, remember username!

    Username: R1ckRul3s

  	-->

3) Trying gobuster:
	
	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	Output:
		- /assets	->	contains files (potential reverse shell exploit?)

4) Tried brute forcing into SSH using Hydra:
	
	Command: `hydra -l R1ckRul3s -P /usr/share/wordlists/rockyou.txt $IP ssh`
	Output: No dice. Doesn't support password login meaning it needs SSH.