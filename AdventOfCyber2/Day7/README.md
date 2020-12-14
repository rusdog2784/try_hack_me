# IP=NONE


### [Day 7] Networking - The Grinch Really Did Steal Christmas ###

1. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?

```
10.11.3.2
```

2. If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?

```
http.request.method == GET
```

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?

```
Filter: http.request.method == GET && ip.src == 10.10.67.199

/reindeer-of-the-week
```

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process? There's a lot of irrelevant data here - Using a filter here would be useful!

```
Filter: ftp (searched for LOGIN and USER and PASS requests)

plaintext_password_fiasco
```

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?

```
Just by looking in the info section, you can see it says "Encrypted packet".

SSH
```

6. Analyse "pcap3.pcap" and recover Christmas! What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?

	* Notes:
		* Found this in an HTTP request (HTTP/1.1 200 OK (text/html):
		```
		Hey fellow Elves! We&rsquo;re currently recruiting for the positions listed below. As always, please sned your reccomendations to your workshop manager - any successful referer will receieve a $150 bonus in their next pay packet.
		1x HR Manager: We are seeking a new Elf McKaren. All applications must have 3 years prior experience in a similar role and be able to work under crunch time.
		4x Stocking Fillers Our dispatch team is looking for new fresh-faces to bolster the ranks of fellow stocking fillers.
		```
		* Found 'christmas.zip' (HTTP/1.1 200 OK (application/zip). To extract, I found the request with the Media type: application/zip, selected it, then clicked on File > Extract Object > HTTP, and selected christmas.zip. Extracted the zip and saved everything inside a folder called 'christmas-zip'.

	* Commands:
		* Filter to display all HTTP requests: `http`

	* Answer:
	```
	Rubber ducky
	```
