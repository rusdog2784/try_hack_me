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

	Answer: `base32 is super common in CTF's`
	Commands:
		1) `python3` (start the shell)
		2) >>> `import base64`
		3) >>> `str = "<the question text>"`
		4) >>> `base64.b32decode(str)` 

4) RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

	Answer: `Each Base64 digit represents exactly 6 bits of data.`
	Command: `echo "<the question text>" | base64`
	Notes:
		- Maybe a good way to know if something is encoded using base64 is to divide the length by 6 and if you get an even number, then its base 64?

5) 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f

	Answer: `hexadecimal or base16?`
	Command: `echo "the question text" | xxd -r -p`

6) Ebgngr zr 13 cynprf!

	Answer: `Rotate me 13 places!`
	Notes: 
		a b c d e f g h i j k l m n o p q r s t u v w x y z
		n o p q r s t u v w x y z a b c d e f g h i j k l m
		- Above is the substitution cipher to use on the provided text. In hindsight and like some articles I read suggested, I should have figured out the two letter word, 'me', then started the alphabet however many spaces from the 'e' that would substitute the 'r'. Also, the 13 was out of place and 13 is the exact number of spaces to start the alphabet in the cipher so in the future take the hint ;).
		- Used this online cryptogram solver tool: https://www.boxentriq.com/code-breaking/cryptogram.

7) *@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX

	Answer: `You spin me right round baby right round (47 times)`
	Notes: 
		- Searched google for 'special character cipher' and first result was an online converter for ROT47: https://www.dcode.fr/rot-47-cipher.
		- ROT47 definition: Rot47 consists in replacing a character with another located 47 positions after in the alphabet.

8) - . .-.. . -.-. --- -- -- ..- -. .. -.-. .- - .. --- -.
	. -. -.-. --- -.. .. -. --.

	Answer: `TELECOMMUNICATION ENCODING`
	Notes:
		- Obviously looks like morse code. Keep note, though, that there are two words here.
		- Found a Morse Code Translater and entered each line separately: https://morsecode.world/international/translator.html
		- First line:	`TELECOMMUNICATION`
		- Second line: 	`ENCODING`

9) 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68

	Answer: `Unpack this BCD`
	Notes:
		- Simple Numbers to ASCII letters. Online decoder: https://www.boxentriq.com/code-breaking/numbers-to-letters

10) <For maintainability and readability, I am not posting the text in this README because its suuuuper long. So if you want to see it, check it out inside the TryHackMe room.>

	Answer: ``


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

