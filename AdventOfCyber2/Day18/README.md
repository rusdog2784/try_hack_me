# IP=10.10.47.36


### [Day 18] Reverse Engineering - The Bits of Christmas ###

1. Open the "TBFC_APP" application in ILspy and begin decompiling the code.

	* By default, my operating system didn't come with any RDP program so I installed Remmina like this challenge suggested.

2. What is Santa's password?

	* Once you started up ILSpy and open the TBFC_APP, in the navigation pane, find the section that says `Crack Me` and open it up.
	* Open `MainForm`.
	* Scroll down until you see the function, `buttonActivate_Click`. On the second line of the function, you'll see the password.

```
santapassword321
```

3. Now that you've retrieved this password, try to login... What is the flag?

	* Didn't have to log in. In the same function where I found the password, if you look at one of the dialog boxes, you can see the flag.

```
thm{046af}
```
