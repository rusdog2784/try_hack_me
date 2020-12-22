# IP=10.10.129.10


### [Day 20] Blue Teaming - PowershELiF to the rescue ###

0. Connect to the machine via SSH using the following details:

	* Username: `mceager`
	* Password: `r0ckStar!`

1. Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?

	* Navigate to Documents folder and run: `Get-ChildItem -Hidden` followed by `Get-Content .\e1fone.txt`.

```
2 front teeth
```

2. Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?

	* Navigate to the Desktop folder, then into the `elf2wo` folder.
	* Run `ls`, then `Get-Content` the only file in there.

```
Scrooged
```

3. Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)

	* Navigate out of the `mceager` directory and into the base of `C:`.
	* Run the command: `Get-ChildItem -Hidden -Directory -Recurse -ErrorAction SilentlyContinue`. This will print out all hidden directories within the entire C: drive (yes, it will search sub-directories too). About half way through, you should notice a directory that looks like the word 'elfthree', but in l33t speak.

```
3lfthr3e
```

4. How many words does the first file contain?

	* Once in the directory, `C:\Windows\System32\3lfthr3e`, run the command: `Get-Content .\1.txt | Measure-Object -Word`

```
9999
```

5. What 2 words are at index 551 and 6991 in the first file?

	* Run the commands: `(Get-Content .\1.txt)[551]` and `(Get-Content .\1.txt)[6991]`

```
Red Ryder
```

6. This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)

	* Run the command: `Select-String .\2.txt -Pattern 'RedRyder*'`

```
Red Ryder BB Gun
```