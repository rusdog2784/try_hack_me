# IP=10.10.58.251


### [Day 10] Networking - Don't be sElfish! ###

1. Question #1 Using enum4linux, how many users are there on the Samba server (<IP>)?

	* Notes:
		* Working with Samba shares, so we can use enum4linux to enumerate the basics of the SMB share on the server.

	* Commands:
		* Enumerate for users: `enum4linux -U $IP > smb-enum-users.txt`

	* Answer:
	```
	3
	```

2. Question #2 Now how many "shares" are there on the Samba server?

	* Notes:
		* See Question 1 notes.

	* Commands:
		* Enumerate for shares: `enum4linux -S $IP > smb-enum-shares.txt`

	* Answer:
	```
	4
	```

3. Question #3 Use smbclient to try to login to the shares on the Samba server (<IP>). What share doesn't require a password?

```
tbfc-santa
```

4. Question #4 Log in to this share, what directory did ElfMcSkidy leave for Santa?

	* Commands:
		* Log into the share: `smbclient //$IP/tbfc-santa`

	* Answer:
	```
	jingle-tunes
	```
