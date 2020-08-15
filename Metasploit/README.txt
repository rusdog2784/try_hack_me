export IP=


==================================================

[TASK 2] - Initializing...

1) First things first, we need to initialize the database! Let's do that now with the command: `msfdb init`

2) Before starting Metasploit, we can view some of the advanced options we can trigger for starting the console. Check these out now by using the command: `msfconsole -h`

3) We can start the Metasploit console on the command line without showing the banner or any startup information as well. What switch do we add to msfconsole to start it without showing this information? This will include the '-'

	Answer: `-q`

4) Once the database is initialized, go ahead and start Metasploit via the command: `msfconsole`

5) After Metasploit has started, let's go ahead and check that we've connected to the database. Do this now with the command: `db_status`

6) Cool! We've connected to the database, which type of database does Metasploit 5 use?
	
	Answer: `postgresql`


==================================================

[TASK 3] - Rock 'em to the Core [Commands]

1) 	Let's go ahead and start exploring the help menu. On the Metasploit prompt (where we'll be at after we start Metasploit using msfconsole), type the command: `help`

2) The help menu has a very short one-character alias, what is it?

	Answer: `?`

3) Finding various modules we have at our disposal within Metasploit is one of the most common commands we will leverage in the framework. What is the base command we use for searching?

	Answer: `search`

4) Once we've found the module we want to leverage, what command do we use to select it as the active module?

	Answer: `use`

5) How about if we want to view information about either a specific module or just the active one we have selected?

	Answer: `info`

6) Metasploit has a built-in netcat-like function where we can make a quick connection with a host simply to verify that we can 'talk' to it. What command is this?

	Answer: `connect`

7) Entirely one of the commands purely utilized for fun, what command displays the motd/ascii art we see when we start msfconsole (without -q flag)?

	Answer: `banner`

8) We'll revisit these next two commands shortly, however, they're two of the most used commands within Metasploit. First, what command do we use to change the value of a variable?

	Answer: `set`

9) Metasploit supports the use of global variables, something which is incredibly useful when you're specifically focusing on a single box. What command changes the value of a variable globally?

	Answer: `setg`

10) Now that we've learned how to change the value of variables, how do we view them? There are technically several answers to this question, however, I'm looking for a specific three-letter command which is used to view the value of single variables.

	Answer: `get`

11) How about changing the value of a variable to null/no value?

	Answer: `unset`

12) When performing a penetration test it's quite common to record your screen either for further review or for providing evidence of any actions taken. This is often coupled with the collection of console output to a file as it can be incredibly useful to grep for different pieces of information output to the screen. What command can we use to set our console output to save to a file?

	Answer: `spool`

13) Leaving a Metasploit console running isn't always convenient and it can be helpful to have all of our previously set values load when starting up Metasploit. What command can we use to store the settings/active datastores from Metasploit to a settings file? This will save within your msf4 (or msf5) directory and can be undone easily by simply removing the created settings file.

	Answer: `save`


==================================================

[TASK 4] - Modules for Every Occasion!

1) Easily the most common module utilized, which module holds all of the exploit code we will use?

	Answer: `exploit`

2) Used hand in hand with exploits, which module contains the various bits of shellcode we send to have executed following exploitation?

	Answer: `payload`

3) Which module is most commonly used in scanning and verification machines are exploitable? This is not the same as the actual exploitation of course.

	Answer: `auxiliary`

4) One of the most common activities after exploitation is looting and pivoting. Which module provides these capabilities?

	Answer: `post`

5) Commonly utilized in payload obfuscation, which module allows us to modify the 'appearance' of our exploit such that we may avoid signature detection?

	Answer: `encoder`

6) Last but not least, which module is used with buffer overflow and ROP attacks?

	Answer: `NOP`

7) Not every module is loaded in by default, what command can we use to load different modules?

	Answer: `load`


==================================================

[TASK 5] - Move that shell!

1) 