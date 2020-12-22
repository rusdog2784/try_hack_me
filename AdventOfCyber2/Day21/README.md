# IP=10.10.192.9


### [Day 21] Blue Teaming - Time for some ELForensics ###

0. Connect to the machine via RDP (Remmina) using the following details:

	* Username: `littlehelper`
	* Password: `iLove5now!`

1. Read the contents of the text file within the Documents folder. What is the file hash for db.exe?

```
596690FFC54AB6101932856E6A78E3A1 
```

2. What is the file hash of the mysterious executable within the Documents folder?

	* Use the command: `Get-FileHash -Algorithm MD5 .\deebee.exe`

```
5F037501FB542AD2D9B06EB12AED09F0
```

3. Using Strings find the hidden flag within the executable?

	* Use the command: `C:\Tools\strings64.exe .\deebee.exe`

```
THM{f6187e6cbeb1214139ef313e108cb6f9} 
```

4. What is the flag that is displayed when you run the database connector file?

	* Determine the location of the hidden data stream for the database execution file: `Get-Item .\deebee.exe -Stream *`. This returns some important information, specifically:
		```
		PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\littlehelper\Documents\deebee.exe:hidedb
		Stream        : hidedb
		Length        : 6144
		```
	* Take the command provided in the end of the walkthrough (the one to execute streamed executables) and edit it with information specific to what we know, like so: `wmic process call create $(Resolve-Path .\deebee.exe:hidedb)`

```
THM{088731ddc7b9fdeccaed982b07c297c}
```
