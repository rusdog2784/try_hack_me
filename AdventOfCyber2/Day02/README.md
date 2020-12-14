# IP=10.10.244.135


### [Day 2] Web Exploitation - The Elf Strikes Back! ###

0. Note at the bottom of the dosier:

```
For Elf McEager:
You have been assigned an ID number for your audit of the system: ODIzODI5MTNiYmYw . Use this to gain access to the upload section of the site.
Good luck!
```

1. What string of text needs adding to the URL to get access to the upload page?

```
?id=ODIzODI5MTNiYmYw
```

2. What type of file is accepted by the site?

```
.jpg worked (trial and error; created a folder and placed a bunch of dummy file types into it)

You could also find the upload type by looking at the source code.

The answer the question is looking for is: image
```

3. Bypass the filter and upload a reverse shell. In which directory are the uploaded files stored?

```
a. Renamed my php-reverse-shell.php to php-reverse-shell.jpg.php.
b. Uploaded it.
c. Poked around in the following endpoints: images, uploads.
d. Found my uploaded files inside of /uploads.

Answer: /uploads/
```

4. Activate your reverse shell and catch it in a netcat listener!

```
a. Started netcat listening on local machine with the command: 'sudo nc -lnvp 444'
b. Clicked on my reverse shell file inside the /uploads page.
```

5. What is the flag in /var/www/flag.txt?

```
==============================================================


You've reached the end of the Advent of Cyber, Day 2 -- hopefully you're enjoying yourself so far, and are learning lots! 
This is all from me, so I'm going to take the chance to thank the awesome @Vargnaar for his invaluable design lessons, without which the theming of the past two websites simply would not be the same. 


Have a flag -- you deserve it!
THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}


Good luck on your mission (and maybe I'll see y'all again on Christmas Eve)!
 --Muiri (@MuirlandOracle)


==============================================================
```