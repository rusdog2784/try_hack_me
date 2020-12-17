# IP=10.10.85.252


### [Day 12] Networking - Ready, set, elf. ###

1. What is the version number of the web server?

	* Ran nmap scan: `nmap -Pn -oN nmap/initial $IP`
	* Web server was running on port 8080. Went to `http://$IP:8080` and immediately saw the version number.

```
9.0.17
```

2. What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)

	* Searched google for `apache tomcat 9.0.17 exploit` and found the exploit with remote code execution.

```
CVE-2019-0232
```

3. Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.

	* Open metasploit: `msfconsole`
	* Search for Apache Tomcat.
	* Found the option with reference to Apache Tomcat CGIServlet enableCmdLineArguments Vulnerability, which is what the CVE vulnerability mentioned (from the last question).
	* Selected `exploit/windows/http/tomcat_cgi_cmdlineargs` and showed its options.
	* Had to set RHOST, TARGETURI, and LHOST.
		* RHOST = target machine's IP
		* TARGETURI = /cgi-bin/elfwhacker.bat
		* LHOST = tun0 IP (the IP of my VPN session)
	* Finally let the exploit run: `exploit`.

4. What are the contents of flag1.txt?

```
thm{whacking_all_the_elves}
```

5. Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!

	* Use built-in meterpreter command, `getsystem`.

```
getsystem > NT AUTHORITY\SYSTEM
```