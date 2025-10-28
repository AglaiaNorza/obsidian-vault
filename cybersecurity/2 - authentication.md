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
An organisation can choose from a range of authentication technologies, based on the degree of confidence in identity proofing and authentication processes.

There are three levels of Identity Assurance Levels (IAL):
- **IAL 1** ⟶ no need to link the applicant to a specific 