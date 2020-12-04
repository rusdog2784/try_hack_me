# IP=10.10.120.94


### [Day 3] Web Exploitation - Christmas Chaos ###

1. Use BurpSuite to brute force the login form.  Use the following lists for the default credentials:
	
| Usernames | Passwords	|<br>
|-----------------------|<br>
| root      | root      |<br>
| admin     | password  |<br>
| user      | 12345     |<br>

Use the correct credentials to log in to the Santa Sleigh Tracker app. Don't forget to turn off Foxyproxy once BurpSuite has finished the attack!

What is the flag?

```
--- Configuring BurpSuite and the browser ---
a) Opened and started BurpSuite (temporary project w/ default settings).
b) Opened FireFox and changed the DNS settings to point to BurpSuite's DNS server, 127.0.0.1:8080.
c) Turned intercep ON, then submitted the login form.
d) Once the request is caught by BurpSuite (inside the 'Proxy' tab), select the 'Actions' dropdown and select 'Send to Intruder'.
e) Navigate to the 'Intruder' tab.
f) Select the 'Positions' tab, clear all the automatically found positions, then manually add/set the positions for 'username' and 'password' (highlight the values and select 'Add').
g) Select the 'Payloads' tab and select '1' from the 'Payload set:' dropdown.
h) Load in the 'usernames-to-try.txt' file into the 'Payload Options [Simple list]' section.
i) Go back to the top and now select '2' from the 'Payload set:' dropdown, and repeat step h) using the 'passwords-to-try.txt' file.
j) Press 'Start Attack'.
k) Of all the requests tried, the one with username, 'admin', and password, '12345' was the only one with a different length. Go ahead and try logging into the form with those credentials.

--- Credentials Found ---
username: admin
password: 12345

--- Flag Found ---
THM{885ffab980e049847516f9d8fe99ad1a}
```