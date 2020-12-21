# IP=10.10.126.243


### [Day 17] Reverse Engineering - ReverseELFeering ###

0. Log into the SSH server with the following details:

	* username: `elfmceager`
	* password: `adventofcyber`

1. What is the value of `local_ch` when its corresponding `movl` instruction is called (first if multilple)?

	* View the challenge1 file with the command: `r2 -d challenge1`.
	* Run analysis: `aa`
	* View all functions with references to main: `afl | grep main`
	* View the main function: `pdf @main`
	* Using the notes, I was able to follow along and answer the remaining questions.

```
1
```

2. What is the value of `eax` when the `imull` instruction is called?

```
6
```

3. What is the value of `local_4h` before `eax` is set to 0?

```
6
```
