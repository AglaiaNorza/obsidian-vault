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
- `password + salt` is encrypted 25 times, and the output is translated to a 11 character sequence

This approach is now considered inadequate, though it is often required for compatibility reasons.

### unix-style, today
UNIX:
- 1000 iterations of MD5 crypt routine with a salt of up to 48 bits
- no limitations on password length
- produces a 128-bit hash value

OpenBSD:
- uses Bcrypt (hash function based on the Blowfish symmetric block cypher), which allows passwords of up to 55 characters
- requires a 128-bit salt
- produces a 192-bit hash value
- includes a configurable cost variable to increase time required to perform a hash

## password strength and cracking
>[!question] what makes a password strong?
> - using both upper and lower case characters, special characters, numbers
> - unpredictability
> - length

The main vulnerability passwords have is that they have to be stored in human memory (so they are far from random).

Password cracking attacks include:
- **dictionary attacks** - attackers develop a large dictionary of possible passwords and try each one against the password file (each password has to be hashedd using each salt value)
- **rainbow table attacks** - hash values are pre-compiled for all salts

### password selection strategies
- *user education* - users can be taught the importance of using hard to guess passwords, and can be provided with guidelines for selecting strong passwords
- *computer generated passwords* (users have trouble remembering them)
- *reactive password checking* - system periodicaly runs its own password cracker to find guessable passwords
- *complex password policy* - system checks to see if the password selected by the user is allowable, and if not, rejects it. 
	- the goal is to eliminate guessable passwords while allowing the user to select a password that is memorable
	- hard to understand the balance, + it requires space and time to check the passwords

>[!tip] periodically changing password
>Requiring users to change passwors periodically, while intuitive, is not a good practice, as it incentivizes weaker passwords that are easier for people to set and remember 

