==================================================

[TASK 1] - Level 1

NOTE: All hashes and answers are located inside the 'Task1' folder.

1) 48bb6e862e54f2a795ffc4e541caed4d

	Answer: `easy`
	Command: `hashcat -a 0 -m 0 Task1/question1.hash /usr/share/wordlists/rockyou.txt -o Task1/question1-answer.txt`
	Notes:
		- Looked up what type of hash the text was using Hash Analyzer (https://www.tunnelsup.com/hash-analyzer/).
		- MD5 or MD4 => -m 0

2) CBFDAC6008F9CAB4083784CBD1874F76618D2A97

	Answer: `password123`
	Command: `hashcat -a 0 -m 100 Task1/question2.hash /usr/share/wordlists/rockyou.txt -o Task1/question2-answer.txt`
	Notes:
		- Using Hash Analyzer: SHA1 (or SHA 128) => -m 100

3) 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

	Answer: `letmein`
	Command: `hashcat -a 0 -m 1400 Task1/question3.hash /usr/share/wordlists/rockyou.txt -o Task1/question3-answer.txt`
	Notes:
		- Using Hash Analyzer: SHA2-256 => -m 1400

4) $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

	Answer: `bleh`
	Commands: 
		1) `cat /usr/share/wordlists/rockyou.txt | awk 'length($0) < 5' | tee rockyou_4_char_max.txt`
				> Created 'rockyou_4_char_max.txt' inside Task1.
		2) `hashcat -a 0 -m 3200 Task1/question4.hash Task1/rockyou_4_char_max.txt -o Task1/question4-answer.txt`
	Notes:
		- Using Hash Analyzer: bcrypt => -m 3200
		- Hashcat's bycrypt decryption would have take at least a day to complete the crack so I had to do some out of the box thinking. In the answer text field, I noticed that the answer was only 4 characters, so what I did was modify the rockyou.txt file to only contain password with 4 characters. This in turn made the list of possible passwords much smaller and hashcat was then able to crack the password in about 30 seconds.

5) 279412f945939ba78ce0758d3fd83daa

	Answer: `Eternity22`
	Command: `hashcat -a 0 -m 900 Task1/question5.hash /usr/share/wordlists/rockyou.txt -o Task1/question5-answer.txt`
	Notes:
		- Using Hash Analyzer: MD5 or MD4 => -m 0 (MD5) | -m 900 (MD4)


==================================================

[TASK 2] - Level 2

NOTE: All hashes and answers are located inside the 'Task1' folder.

1) Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

	Answer: `paule`
	Command: `hashcat -a 0 -m 1400 Task2/question1.hash /usr/share/wordlists/rockyou.txt -o Task2/question1-answer.txt`
	Notes:
		- Using Hash Analyzer: SHA2-256 => -m 1400

2) Hash: 1DFECA0C002AE40B8619ECF94819CC1B

	Answer: `n63umy8lkf4i`
	Command: `hashcat -a 0 -m 1000 Task2/question2.hash /usr/share/wordlists/rockyou.txt -o Task2/question2-answer.txt`
	Notes:
		- Using Hash Analyzer: MD5 or MD4 => -m 0 (MD5) | -m 900 (MD4)
			> THis was wrong and didn't work
		- Looking at the question hint, it said: NTLM => -m 1000

3) Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.
	Salt: aReallyHardSalt
	Rounds: 5

	Answer: `waka99`
	Command: `hashcat -a 0 -m 1800 Task2/question3.hash /usr/share/wordlists/rockyou.txt -o Task2/question3-answer.txt`
	Notes:
		- Using Hash Type Identifer (https://hashes.com/en/tools/hash_identifier): sha512crypt $6$, SHA512 (Unix) => -m 1800

4) Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6
	Salt: tryhackme

	Answer: `481616481616`
	Command: `hashcat -a 0 -m 160 Task2/question4.hash /usr/share/wordlists/rockyou.txt -o Task2/question4-answer.txt`
	Notes:
		- Using Hash Type Identifier: SHA1 => -m 100
		- HOWEVER, we are given a salt. Found this in the hashcat documentation: HMAC-SHA1 (key = $salt) => -m 160
		- Had to take the provided hash and salt and combine them myself to make:
			> 'e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme'


==================================================
