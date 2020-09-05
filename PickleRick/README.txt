export IP=10.10.240.253


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

3) Trying gobuster (After watching John Hammond, he includes file extenstions to look for):
	
	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,js,css,p -o gobuster.txt`
	Output: See `gobuster.txt`

4) Ran nikto for the first time...

	Command: `nikto -h http://$IP | tee nikto.log`
	Output: See `nikto.log`

5) Tried brute forcing into SSH using Hydra:
	
	Command: `hydra -l R1ckRul3s -P /usr/share/wordlists/rockyou.txt $IP ssh`
	Output: No dice. Doesn't support password login meaning it needs SSH.

6) Apache servers most always have a /robots.txt file. Went to http://$IP/robots.txt and found:

	Wubbalubbadubdub