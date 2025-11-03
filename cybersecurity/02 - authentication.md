>[!quote] authentication, definition by NIST
> The process of establishing confidence in user identities that are presented electronically to an information system

The definition by NIST lists some identification requirements for protecting data:
- uniquely identify and authenticate system *users*, and associate the *unique identification* with *processes* acting on behalf of those users
- uniquely identify and authenticate *devices* before establishing a system connection
- implement *multi-factor authentication* for access 
- implement *replay-resistant authentication* mechanisms for access
	- replay attack - capturing a valid message (/authentication data) and resending it later to re-gain access

There are three aspects that need to be managed:
- **identifiers**
	- select and assign identifiers to individuals, groups, roles, services or devices
	- prevent the reuse of identifiers for a defined time period
- **passwords**
	- maintain an updated list of commonly-used, expected or compromised passwords, and verify that passwords are not in that list
	- transmit passwords only over cryptographically protected means
	- select a new password upon first use after account recovery
	- enforce composition and complexity rules for passwords
- **authenticators**
	- verify the identity of the individual/group/... receiving the authenticator as part of the initial authenticator distribution
	- establish initial authenticator content
	- establish and implement administrative procedures for initial authenticator distribution; for lost, compromised, or damaged authenticators; and for revoking authenticators
	- change default authenticators at first use, and change them frequently or when relevant events occur
	- protect authenticator content from unauthorized disclosure and modification
-  **feedback** of authentication information must be **obscured** during the authentication process

>[!info] digital identity guidelines architecture model
>
>![[NIST-digital-id.png|center|600]]
## means of authentication
The four means of authentication are based on
- something you know (e.g. password)
- something you possess ⟶ token (e.g. smart card)
- something you are ⟶ biometrics (e.g. fingerprint)
- something you do ⟶ dynamic biometrics (e.g. voice pattern)

## assurance levels for user authentication
### IAL
An organisation can choose from a range of authentication technologies, based on the degree of confidence in identity proofing and authentication processes.

There are three levels of **Identity Assurance Levels** (IAL):
- **IAL 1** ⟶ no need to link the applicant to a specific real-life identity
- **IAL 2** ⟶ provides evidence for the claimed identity using remote or physically-present identity proofing
- **IAL 3** ⟶ requires physical presence for identity proofing

### AAL
AALs define options an organisation can select

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

(also talked about [[01 - cryptographic concepts#hash functions|here]])

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
>Requiring users to change passwors periodically, while intuitive, is not a good practice, as it incentivizes the use of weaker passwords that are easier for people to set and remember.

## Tokens
Authentication with tokens can be done via:
- **barcodes** ⟶ barcodes encode a unique item number that allows the scanning system to look up the corresponding details
	- since they are *easily clonable*, they provide convenience but not security
- **magnetic stripe cards** ⟶ plastic cards with a magnetic stripe containing personalized information about the card holder 
	- the first track of a magnetic card stripe contains the cardholder's full name, account number and more
	- the second track may contain the account number, expiration date, information about the bank and more
	- they are *easy to read and cheap to reproduce*
- **smart tokens**

### Smart tokens
Smart tokens:
- include an embedded **microprocessor**
- can look like calculators, keys, small objects
- can have manual interfaces (like keypads)
- require an **electronic interface** to communicate with compatible readers/writers
- can implement different authentication protocols: *static*, *dynamic password generators*, and *challenge-response*

#### Smart cards
Smart cards look like credit cards, but they include an electronic interface. They contain an entire **microprocessor** made up of a processor, memory, and I/O ports.
They typically include three types of memory:
- **Read-Only** (ROM) ⟶ stores the data that doesn't change during the card's life
- **Electrically erasable programmable ROM** (EEPROM) ⟶ holds application data and programs
- **Random access** (RAM) ⟶ holds temporary data generated when applications are executed

>[!info] eIDs
> National electronic identity cards are examples of smart cards. In addition to other national ID cards, they provide:
> - ePass - a digital representation of the cardholder's identity
> - eID - an identity record that an authorised service can access with the cardholder's permission
> - eSign - private key and certificate verifying the key; generates a digital signature
> 
> To ensure that the contactless RF chip in the eID card cannot be read without explicit access control, the **Password Authenticated Connection Establishment** (PACE) protocol is used:
> - for online applications, access is established by the user via six-digit PIN
> - for offline application, either the MRZ printed on the back of the card or the six-digit card access number (CAN) printed on the front is used
> 
> ![[eID-auth.png|center|500]]
### OTPs
OTP (One-Time Password) devices are **hardware authentication tokens**. They have a secret key to generate an OTP, which is entered by the user and validated by the system.

They use a block cipher/hash function to combine secret key and time or nonce value (arbitrary number that can only be used once in a cryptographic communication) to create the OTP.
They have a tamper-resistant module for secure storage of the secret key.

>[!bug] The main disadvantage to hardware authentication tokens is that any other person can see the code (which is why they are used in multifactor authentication)
#### Time-based one-time password (TOTP)
Time-based OTPs (TOTPs), are used in many hardware tokens and by many mobile authenticator apps.
The client and the server pre-establish the unix time from which to start counting time steps, and the length of a one-time duration. Both the client and the server calculate a `C_t` value (`current_unix_time/time_step`).
`C_t` and the secret key (which client and server share) are then used in the HMAC ([[01 - cryptographic concepts#MAC with one-way hash functions|hash-based MAc]]) to get an authentication tag 
- TOTPs aren't vulnerable to replay attacks, as the code changes every 30 seconds
- systems using time based OTP need to allow for clock drift between token and verifying system

#### Authentication using a mobile phone
Authentication can also be done on a mobile phone, in two main ways:
- via **SMS**
	- one of the simplest approaches
	- requires mobile coverage to receive the sms
	- if the mobile is lost or stolen, the user will lose access and somene else might gain it
	- an attacker might also intercept messages using either a fake mobile tower, or by attacking SS7 signaling protocol
- via **mobile authenticator apps**:
	- they implement a one-time password generator with the TOTP algorithm
	- they don't require an internet connection, and can be used with multiple accounts
	- the phone might still be lost or stolen
	- an attacker might compromise them by installing malware

## Biometrics
Biometrics are measures used to **uniquely identify** a person, based on **biological or physiological traits**.

Biometric systems incorporate scanners or sensors to read in information, which is then compared to stored templates of accepted users.
- based on pattern recognition

Biometric systems are technically complex and expensive when compared to passwords and tokens.

>[!summary] representation
>
>![[biometric-id.png|center|550]]

>[!info] biometric accuracy dilemma
>Determining how close a presented feature has to be to a reference feature isn't easy.
>
>![[bio-acc.png|center|500]]
>
>In this depiction, the comparison between the presented feature and a reference feature is reduced to a single numeric value, which, to be accepted as a match, has to be greater than a preassigned threshold.

>[!tip]- security vs convenience
>
>![[biom-op-curves.png|center|500]]

There are three steps in the operation of a biometric authentication system:
- **enrollment**

![[enrollment.png|center|500]]


- **verification**

![[verification.png|center|500]]

- **identification**


![[identification.png|center|500]]

## Remote user authentication
Authentication over a network, the internet or a communications link is more complex - there are additional security threats, such as eavesdropping, password capturing, replaying an authentication sequence that has been observed.

Remote authentication generally relies on some form of a **challenge-response** protocol to counter threats.

>[!summary] basic challenge-response protocol for remote user auth
>
>password and token
>
>![[challenge-response.png|center|600]]
>
>static and dynamic biometric
>
> ![[challenge-response1.png|center|600]]

## Authentication security issues
There are a lot of different attacks that can be attempted:
- **client attacks** ⟶ adversary attempts to achieve user authentication *without access to the remote host* or the intervening communications path
- **host attacks** ⟶ directed at the *user file* at the host where passwords, token passcodes, or biometric templates are stored
- **eavesdropping** ⟶ adversary *attempts to learn the password* by some sort of attack that involves physical proximity 
- **replay** ⟶ adversary *repeats a previously captured user response*
- **trojan horse** ⟶ an application or physical device *masquerades as an authentic application* or device for the purpose of capturing a user password, passcode, or biometric
- **denial-of-service** ⟶ attempts to disable a user authentication service by *flooding the service* with numerous authentication attempts

| Attacks                           | Authenticators             | Examples                                       | Typical defenses                                                                                                           |
| --------------------------------- | -------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **client attack**                 | password                   | guessing, exhaustive search                    | large entropy; limited attempts                                                                                            |
|                                   | token                      | exhaustive search                              | large entropy; limited attempts; theft of object requires presence                                                         |
|                                   | biometric                  | false match                                    | large entropy; limited attempts                                                                                            |
| **host attacks**                  | password                   | plaintext theft, dictionary/exhaustive search  | same as password; 1-time passcode                                                                                          |
|                                   | token                      | passcode theft                                 | capture device authentication; challenge response                                                                          |
|                                   | biometric                  | template theft                                 | capture device authentication; challenge response                                                                          |
| **eavesdropping, theft, copying** | password                   | “shoulder surfing”                             | user diligence to keep secret; administrator diligence to quickly revoke compromised passwords; multifactor authentication |
|                                   | token                      | theft, counterfeiting hardware                 | multifactor authentication; tamper resistant/evident token                                                                 |
|                                   | biometric                  | copying (spoofing) biometric                   | copy detection at capture device and capture device authentication                                                         |
| **replay**                        | password                   | replay stolen password response                | challenge-response protocol                                                                                                |
|                                   | token                      | replay stolen passcode response                | challenge-response protocol; 1-time passcode                                                                               |
|                                   | biometric                  | replay stolen biometric template response      | copy detection at capture device and capture device authentication via challenge-response protocol                         |
| **trojan horse**                  | password, token, biometric | installation of rogue client or capture device | authentication of client or capture device within  trusted security perimeter                                              |
| **denial of service**             | password, token, biometric | lockout by multiple failed authentication      | multifactor with token                                                                                                     |