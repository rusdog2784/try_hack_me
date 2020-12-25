# IP=10.10.32.200


### [Day 23] Blue Teaming - The Grinch strikes again! ###

0. Connect to the machine via RDP (Remmina) using the following details:

	* Username: `administrator`
	* Password: `sn0wF!akes!!!`

1. Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?

	* Use CyberChef (https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Ym05dGIzSmxZbVZ6ZEdabGMzUnBkbUZzWTI5dGNHRnVlUT09) to decrypt the bitcoin address provided in the ransome note.
	
```
nomorebestfestivalcompany
```

2. At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?

	* Just take a look at one of the files inside the 'vStockings' folder.

```
.grinch
```

3. What is the name of the suspicious scheduled task?

	* Open Task Scheduler and view all running schedulers. You'll notice one that doesn't look like it belongs. Also, if you select and review each one, there is one with `>:^P` in the description, which should tip you off.

```
opidsfsdf
```

4. Inspect the properties of the scheduled task. What is the location of the executable that is run at login?

	* Check out the Actions tab.

```
C:\Users\Administrator\Desktop\opidsfsdf.exe
```

5. There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?

	* Click on the ShadowCopyVolume scheduler and check out its title (in between the {} brackets).

```
7a9eea15-0000-0000-0000-010000000000
```

6. Assign the hidden partition a letter. What is the name of the hidden folder?

	* Open Disk Management and map the `Backup` drive to a letter.
	* Open the newly mapped drive in your File Explorer.
	* In the File Explorer application, click View then select the option to see hidden files. You should now see an additional folder.

```
confidential
```

7. Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?

```
m33pa55w0rdIZseecure!
```
