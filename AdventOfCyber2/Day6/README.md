# IP=10.10.165.183


### [Day 6] Web Exploitation - Be careful with what you wish on a Christmas night ###

1. What vulnerability type was used to exploit the application?

	* Answer:
	```
	stored cross-site scripting
	```

2. What query string can be abused to craft a reflected XSS?

	* Answer:
	```
	q
	```

3. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?
	
	* Notes:
		* Opened the application ZAP on my computer.
		* Selected "Automatic Attack".
		* Provided the url of the site, then pressed "Attack".
		* Results of the scan pop up in the "Alerts" tab.

	* Answer:
	```
	2 (only the XXS vulnerabilities that were found)
	```

4. Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?

	* Answer:
	```
	yes
	```
