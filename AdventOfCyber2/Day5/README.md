# IP=10.10.90.139


### [Day 5] Web Exploitation - Someone stole Santa's gift list ###

0. Provided information:
	* Santa's TODO: Look at alternative database systems that are better than sqlite. Also, don't forget that you installed a Web Application Firewall (WAF) after last year's attack. In case you've forgotten the command, you can tell SQLMap to try and bypass the WAF by using `--tamper=space2comment`.

1. Without using directory brute forcing, what's Santa's secret login panel?

	* Answer:
	```
	http://10.10.90.139:8000/santapanel
	```

2. Visit Santa's secret login panel and bypass the login using SQLi.

	* Answer: 
		* Inside the username field, I tried `' or true --` and it logged me in as santa.

3. How many entries are there in the gift database?

	* Command:
		* Inside the "Enter" field, I typed: `' ORDER BY 1 --`

	* Answer:
	```
	22 Rows appeared
	```

4. What did Paul ask for?

	* Answer:
	```
	github ownership
	```

5. What is the flag?

	* Notes:
		* See below.

	* Answer:
	```
	```

6. What is admin's password?

	* Notes:
		* See below.

	* Answer:
	```
	EhCNSWzzFP6sc7gB
	```

#### Important Notes About This Exercise ####
* For numbers 5 and 6, I ended up having to go the BurpSuite/SQLMap route in order to get ALL details about the database. Here is what I did:
	
	1. Using BurpSuite, I intercepted the 'search' request made on the /santapanel page (after bypassing the login). I searched 'candy' in the text field.
	2. With the request intercepted, I sent it to the Repeater, then right-clicked and saved the item (saved mine as 'santapanel-search-burp'). After doing this, drop the request or stop intercepting.
	3. Then in my terminal, I used this command to get everything (take note, I got the tamper and dbms values from the special hint at the start of the questions):
	```
	sqlmap -r santapanel-search-burp --dbms=sqlite --tamper=space2comment --dump-all
	```
	4. The outputted results were sent to my home directory under .local/share/sqlmap/output/<IP>. I copied the log file within the output directory into my current directory as 'sqlmap-log.txt'. That file had everything I needed to answer the remaining questions.
