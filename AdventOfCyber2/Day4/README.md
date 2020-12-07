# IP=10.10.5.47


### [Day 4] Web Exploitation - Santa's watching ###

1. Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

	* Answer:
	```
	wfuzz -c -z file,big.txt -hw http://shibes.xyz/api.php?breed=FUZZ
	```

2. Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?
	
	* Notes:
		* Found /api directory. Navigated to it and saw the file, site-log.php.
	
	* Commands: 
	```
	gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html -o gobuster.log
	```

	* Answer:
	```
	site-log.php
	```

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

	* Notes:
		* The sysadmin also told us that the API creates logs using dates with a format of YYYYMMDD.
		* Want to try accessing the site-log.php file for all dates within the year (at time of writing this, the date is December 6th, 2020). Going to create a file of 365 properly formatted dates using this Python code:
			```
			>>> from datetime import datetime, timedelta
			>>> today = datetime.today()
			>>> date_list = [today - timedelta(days=x) for x in range(365)]
			>>> with open('formatted_dates.txt', 'w') as f:
			...     for d in date_list:
			...             f.write(f"{d.strftime('%Y%m%d')}\n")
			```

	* Commands:
	```
	wfuzz -c -w formatted_dates.txt -u http://<IP>/api/site-log.php?date=FUZZ --hw 0 > wfuzz-site-log-output.txt
	```

	* Answer:
	```
	THM{D4t3_AP1}
	```
