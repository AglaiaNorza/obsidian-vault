## passwords
Password-based authentication is based on a login-password combination. 
The user's ID determines their privileges, and whether they're authorised to access the system.

>[!warning] password-based authentication has many vulnerabilities
>
>![[pwd-vuln.png|center|500]]
>
>a very big vulnerability is that to **social engineering** (attempting to use various psychological conditions in humans to get hold of confidential information) - some examples of it are:
>- *pretexting* - creating a story to convince someone to reveal secret information
>- *baiting* - offering a "gift" in exchange for an unsafe action
>- *quid pro quo* - offering a service and expecting something in return

## storing passwords
Passwords are stored through **cryptographic hash functions**, which output a checksum on messages of any length.
- the output is of a constant, **fixed size** (independently from the input length)

A cryptographic hash function has to:
- be impossible to invert
- be very efficient to compute
- make it very hard to find two input values with the same output

(also talked about [[1 - cryptographic concepts#hash functions|here]])

There are different ways of storing passwords:
### unix-style, legacy
-  up to **8 printable characters**-long
- **12-bit salt** used to modif DES encryption into a one-way hash function
- 