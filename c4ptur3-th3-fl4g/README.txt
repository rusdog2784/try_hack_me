export IP=


==================================================

[TASK 1] - Translation & Shifting

Translate, shift and decode the following:

1) c4n y0u c4p7u23 7h3 f149?

	Answer: `can you capture the flag`

2) 01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001

	Answer: `lets try some binary out!`
	Commands:
		1) `python3` (start the shell)
		2) >>> `import binascii`
		3) >>> `binary = "<the question text>"`
		4) >>> `binary = "0b" + binary.replace(" ", "")`
		5) >>> `n = int(binary, 2)`
		6) >>> `n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()`

3) MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

	Answer: ``
	Command: 

4) RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

	Answer: `Each Base64 digit represents exactly 6 bits of data.`
	Command: echo "<the question text>" | base64
	Notes:
		- Maybe a good way to know if something is encoded using base64 is to divide the length by 6 and if you get an even number, then its base 64?


==================================================

[TASK 2] - Spectrograms

1) 


==================================================

[TASK 3] - Steganography

1) 


==================================================

[TASK 4] - Security through obscurity

1) 


==================================================

[IMPORTANT INFORMATION]


==================================================

[APPROACH]

