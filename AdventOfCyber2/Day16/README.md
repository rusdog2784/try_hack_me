# IP=10.10.76.247


### [Day 16] Scripting - Help! Where is Santa? ###

1. What is the port number for the web server?

	* Most web servers are hosted on either 80, 8080, or 8000. I took a guess at 8000 and it was right.

```
8000
```

2. Without using enumerations tools such as Diirbuster, what is the directory for the API? (without the API key)

	* Just used what knowledge I already had regarding API URLs.

```
/api/
```

3. Where is Santa right now?

	* First had to find the API key. To do this, I created the api_key_finder.py file, which is in this directory. Reading through the comments, you'll find how it works. Basically, it created a list of odd numbers between the range of 1 and 99 then trys the known API url, /api/, with a key appended to the end. If the key is not valid, then this is returned `{"item_id":1,"q":"Error. Key not valid!"}`. This is helpful, because we'll know when we have the right key if "Error. Key not valid!" isn't returned!
	* Once you've found the key, just enter it into the URL: `http://$IP/api/$API_KEY` and it'll tell you where Santa is.

```
Winter Wonderland, Hyde Park, London.
```

4. What is the API key?

```
57
```