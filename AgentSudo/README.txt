export IP=10.10.110.231


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

[IMPORTANT INFORMATION]

Potential username: Agent R


==================================================

[APPROACH]

1) Run nmap:

	Command: `nmap -sC -sV -oN nmap/initial $IP`

2) Run gobuster:

	Command: `gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x py,sh,php,html -o gobuster.log`

3) The apache server is vulnerable to an exploit called ShellShock. More specifically, using curl, I can modify and mess with my request to the server using the header, User-Agent, as the index.php page hints at.

	Commands: 
		1) `curl -v -L -H "User-Agent: R" http://$IP -o task2-output1.txt` > task2-output1.txt
		2) `curl -v -L -H "User-Agent: C" http://$IP -o task2-output2.txt` > task2-output2.txt
	Notes:
		- Running the above command for User-Agent: R returns a message that hints that the other agent's names are a part of the alphabet. See file, task2-output1.txt.
		- Using this knowledge, I can check to see if any of the other agents have secret pages. Going to try the above curl command using each letter in the alphabet.
		- "User-Agent: C" worked! Was redirected here: `http://$IP/agent_C_attention.php`. See file, task2-output2.txt.