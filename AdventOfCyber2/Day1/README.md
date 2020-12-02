# IP=10.10.96.150


### [Day 1] Web Exploitation - A Christmas Crisis ###

1. Copy/paste the machines IP into the browser search bar. Register for an account, and then login.

```
Username: scott
Password: supersecret
```

2. What is the name of the cookie used for authentication?

```
auth
```

3. In what format is the value of this cookie encoded?

```
hexadecimal
```

4. Having decoded the cookie, what format is the data stored in?

```
json (used CyberChef to decode the cookie value from Hex)
```

5. What is the value of Santa's cookie?

```
Because we know that the value of the cookie, auth, translates to a json with the format:

{"company":"The Best Festival Company", "username":"scott"}

We can try replacing the "username" key with "santa" then encode the JSON back into Hex.

Santa cookie value: 7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d

Paste that cookie into auth's value, refresh the page, and voila!
```

6. Now that you are the santa user, you can re-activate the assembly line! What is the flag you're given when the line is fully active?

```
Turn everything on and the flag reveals itself.

Flag: THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}
```