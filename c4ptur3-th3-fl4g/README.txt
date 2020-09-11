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

10) <See the file, task1-question10.txt for this question's text.>

	Answer: `Let's make this a bit trickier...`
	Notes:
		- Ok, think I figured it out, but don't have enough energy to implement or try it out. In order to solve, try the following:
			1) Decode task1-question10.txt using base64 (saved as task1-question10-decoded-base64.txt).
			2) Decode each line of task1-question10-decoded-base64.txt using morse code (saved as task1-question10-decoded-morse.txt).
			3) Decode each line of task1-question10-decoded-morse.txt using binary and that should produce final answer.
		- Ok, the problem goes a bit further than initially thought. As expected, question 10 is a combination of all the previous questions. I've completed the below steps, 1 through 3, using the python script, task1-question10-solver.py. The rest I used online decoders:
			1) Decode <question text> using base64
			2) Decode <step 1 result> using morse code
			3) Decode <step 2 result> using binary
				Result: fe `_` ``e bh ``d ba `_h hf `_f `_` ba ``e `_c `_d ``d ba hf ba hg `_d ``e ba ``e ``c `_d hh `_f `_d `_` ``c ce ce ce
			4) Decode <step 3 result> using ROT47
				Result: 76 101 116 39 115 32 109 97 107 101 32 116 104 105 115 32 97 32 98 105 116 32 116 114 105 99 107 105 101 114 46 46 46
			5) Decode <step 4 result> using Simple Numbers to Letters (ASCII)
				Result: `Let's make this a bit trickier...`


==================================================

[TASK 2] - Spectrograms

1) A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time. When applied to an audio signal, spectrograms are sometimes called sonographs, voiceprints, or voicegrams. When the data is represented in a 3D plot they may be called waterfalls. (See file `secretaudio.wav`)

	Answer: `Super Secret Message`
	Notes:
		- Had to google "create spectrogram from wav" and found this article, "https://stackoverflow.com/questions/44787437/how-to-convert-a-wav-file-to-a-spectrogram-in-python3", which I used to create a small python program to create a spectogram.
		- See file `task2-question1-solver.py`.


==================================================

[TASK 3] - Steganography

1) Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. (See file `stegosteg.jpg`)

	Answer: `SpaghettiSteg`
	Commands:
		1) `apt-get install steghide`
		2) `steghide info stegosteg.jpg` 
			> gave me interesting details about the JPG
		3) `steghide extract -sf stegosteg.jpg` 
			> unpacked and created a new file, `steganopayload2248.txt`
		4) `cat steganopayload2248.txt`
	Notes:
		- Had to google "steganography tools linux" and found this article, "https://0xrick.github.io/lists/stego/".
		- Installed the bin module, steghide.


==================================================

[TASK 4] - Security through obscurity

Security through obscurity is the reliance in security engineering on the secrecy of the design or implementation as the main method of providing security for a system or component of a system. (See file `meme.jpg`)

1) Download and get 'inside' the file. What is the first filename & extension?

	Answer: `hackerchat.png`
	Commands:
		1) `steghide info meme.jpg`
			> didn't work because I needed a passphrase that I didn't know
		2) `./steghide-crack.sh meme.jpg /usr/share/wordlists/rockyou.txt`
			> didn't really finish, but while it was going I ran the following command...
		3) `strings meme.jpg | awk 'length($0) > 8'
			> gave me the answer, hackerchat.png, and some other stuff
	Notes:
		- Found an online steghide passphrase cracker shell script here, "https://github.com/felipesi/steghide-crack/blob/master/steghide-crack.sh"
		- `strings` was the answer.

2) Get inside the archive and inspect the file carefully. Find the hidden text.

	Answer: `AHH_YOU_FOUND_ME!`
	Command: `strings meme.jpg | awk 'length($0) > 8`
