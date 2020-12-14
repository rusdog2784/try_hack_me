# IP=10.10.131.115


### [Day 8] Networking - What's Under the Christmas Tree? ###

1. When was Snort created?

```
1998
```

2. Using Nmap on <IP>, what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)

	* Command: 
	```
	nmap -sC -sV -oN nmap/initial $IP
	```

	* Answer:
	```
	80
	2222
	3389
	```

3. Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up

	* Command: 
	```
	nmap -Pn -oN nmap/Pn-flag $IP
	```

4. Experiment with different scan settings such as -A and -sV whilst comparing the outputs given.

	* Command:
	```
	nmap -A -oN nmap/A-flag $IP
	```

5. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?

	* Answer: 
	```
	Ubuntu
	```

6. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?

	* Command:
	```
	nmap --script http-title -oN nmap/http-title-script $IP
	```

	* Answer:
	```
	Blog
	```

7. Now use different scripts against the remaining services to discover any further information about them.
