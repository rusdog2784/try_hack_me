## IP=10.10.132.117


# Tartarus #

### Approach:
	* Apache server with a /robots.txt page.
		* User-Agent: *
		* Disallow : /admin-dir
		* 'I told d4rckh we should hide our things deep.'
	* FTP (21), SSH (22), HTTP (80)
		* Can log into FTP with anonymous.
	* Found hidden file on FTP server: `cd .../.../yougotgoodeyes.txt`.
		* Gave us: `/sUp3r-s3cr3t`, which is a login page.
	* Used BurpSuite to brute force the username and password of the login page.
		* Username: `enox`
		* Password: `P@ssword1234`
	* Once logged in, you can upload files. Uploaded a php reverse shell, but didn't know where the uploads were. Decided to run gobuster on the new endpoint: `gobuster dir -u http://$IP/sUp3r-s3cr3t -x html,php,sh -o gobuster_super-secret.log`. 
		* Found `sUp3r-s3cr3t/images/uploads`.
		* Was able to run my php reverse shell and gain access.
			* Locally: `nc -lnvp 4444`.
	* Found two users: `thirtytwo` and `d4rckh`
		* There is a `user.txt` in d4rckh.
			* '0f7dbb2243e692e3ad222bc4eff8521f'
		* There is a `note.txt` in thirtytwo.
			* Hey 32, the other day you were unable to clone my github repository. Now you can use git. Took a while to fix it but now its good :)
			~D4rckh
	* Can switch to euid=(thirtytwo) using gdb:
		* `./gdb -nx -ex 'python import os; os.execl("/bin/bash", "bash", "-p")' -ex quit`



1. User Flag

```
```

2. Root Flag

```
```
