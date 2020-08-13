export IP=10.10.53.123


==================================================

[TASK 2] - Reconnaissance
1) Scan the box, how many ports are open?

	Command: `nmap -Pn -oN nmap/open-ports $IP`
	Answer: 6

2) What version of the squid proxy is running on the machine?

	Command: `nmap -sV -oN nmap/versions $IP`
	Answer: Squid http proxy `3.5.12`

3) How many ports will nmap scan if the flag -p-400 was used?

	Command: `nmap -p-400 -oN nmap/x-number-of-ports $IP`
	Answer: 400 (3 open, 397 closed)

4) Using the nmap flag -n what will it not resolve?

	Command: `nmap -h`
	Answer: DNS

5) What is the most likely operating system this machine is running?
	
	Command: `nmap -A -oN nmap/version-and-os $IP`
	Answer: ubuntu

6) What port is the web server running on?
	
	Command: `nmap -A -oN nmap/version-and-os $IP`
	Answer: 3333


==================================================

[TASK 3] - Locating directories using GoBuster
1) What is the directory that has an upload form page?

	Command: `gobuster dir -u http://$IP:3333 -w /usr/share/wordlists/dirbuster	> gobuster.txt`
	Answer: http://$IP:3333/internal


==================================================

[TASK 4] - Compromising the webserver
1) 	Try upload a few file types to the server, what common extension seems to be blocked?
	
	Command: 
		None... physically tried uploading different file types.
	Answer: 
		`.php`

2) To identify which extensions are not blocked, we're going to fuzz the upload form. 
	
	Answer:
		For this they recommend using BurpSuite, but I don't know what that is and the room to introduce it is for subscribers only. Moving on. EDIT: Kind of figured it out.

3) We're going to use Intruder (used for automating customised attacks).

 - To begin, make a wordlist with the following extensions in:

 - <image from the room>

 - Now make sure BurpSuite is configured to intercept all your browser traffic. Upload a file, once this request is captured, send it to the Intruder. Click on "Payloads" and select the "Sniper" attack type.

 - Click the "Positions" tab now, find the filename and "Add §" to the extension. It should look like so:

 - <image from the room>

 - Run this attack, what extension is allowed?

	Command: 
		None... had to spend some time configuring Burp Suite. Ended up going into Firefox proxy settings and manually setting the proxy to 127.0.0.1:8080. After doing that, I went to the upload URL (https://$IP:3333/internal/) and submitted a dummy form so that Burp Suite could capture the reqest. From there, I followed the instructions specified in the question.
	Answer: 
		`.phtml`

4) Now we know what extension we can use for our payload we can progress.

 - We are going to use a PHP reverse shell as our payload. A reverse shell works by being called on the remote host and forcing this host to make a connection to you. So you'll listen for incoming connections, upload and have your shell executed which will beacon out to you to control!

 - Download the following reverse PHP shell here.

 - To gain remote access to this machine, follow the steps below:

 - a) Edit the php-reverse-shell.php file and edit the ip to be your tun0 ip (you can get this by going to your access page on TryHackMe and using your internal ip).

 - b) Rename this file to php-reverse-shell.phtml

 - c) We're now going to listen to incoming connections using netcat. Run the following command: nc -lvnp 1234

 - d) Upload your shell and navigate to http://<ip>:3333/internal/uploads/php-reverse-shell.phtml - This will execute your payload

 - e) You should see a connection on your netcat session

	Answer: 
		Downloaded and added my internal IP to the $ip section of the php reverse shell script (saved as php-reverse-shell.phtml), which I then uploaded by going to http://$IP:3333/internal and selecting the php-reverse-shell.phtml script. 
		Then I started the netcap operation with this command: `nc -lvnp 1234`.
		Finally, I navigate to http://$IP:3333/internal/uploads/php-reverse-shell.phtml as the instructions above tell me, which in turn connects to my netcat operation allowing me to run shell commands on the webserver from my terminal.

5) What is the name of the user who manages the webserver?

	Command: At the root of the netcat shell, I ran `cd ./home && ls`
	Answer: `bill`

6) What is the user flag?

	Command: There is a `user.txt` file at the /home/bill
	Answer: `8bd7992fbe8a6ad22a63361004cfcedb`


==================================================

[TASK 5] - Privilege Escalation
1) On the system, search for all SUID files. What file stands out?

	Command: `find / -user root -perm -4000 -exec ls -ldb {} \;` (maybe add `> /dev/null` at the end to only display things we have permissions to)
	Answer: `/bin/systemctl`