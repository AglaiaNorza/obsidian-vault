>[!quote] definition of cybersecurity (by NIST)
>prevention of damage to, protection of, and restoration of computers, electronic communication systems, electronic communications services, wire communication, and electronic communication, including information contained therein, to ensure its **availability**, **integrity**, **authentication**, **confidentiality**, and **nonrepudiation**

>[!info] computer security
>Computer security is made up of the measures and controls that ensure **confidentiality**, **integrity** and **availability** of information system assets, including hardware, software, firmware and information that is being processed, stored and communicated.

## C.I.A.
The key concepts of security are united under the C.I.A. acronym, and they are:
### confidentiality

>[!info] confidentiality
> Preserving **authorised restrictions** on **information access** and disclosure, including means for protecting personal privacy and proprietary information
> (avoiding unauthorised disclosure of information).

Confidentiality includes two related concepts:
- **data confidentiality** ⟶ assures that private information is not made available to unauthorised individuals
- **privacy** ⟶ assures that individuals control what information related to them can be collected and stored and by whom
#### tools for confidentiality
- **encryption** ⟶ the transformation of information via a secret ("*encryption key*"), so that it can only be read using another secret ("*decryption key*")
- **access control** ⟶ rules and policies that limit access to a confidential piece of information to those systems on a "need to know" basis
- **authentication** ⟶ determination of someone's identity or role 
- **authorization** ⟶ determining whether a system is allowed access to resources, based on access control policy
- **physical security** ⟶ establishment of physical barriers to limit access to protected computational resources (es. locks, windowless rooms, copper meshes that stop electromagnetic signals from entering)

### integrity
>[!info] integrity
> Guarding against improper information modification or destruction (including ensuring information nonrepudiation and authenticity).

Integrity includes two related concepts:
- **data integrity** ⟶ assures that information and programs are changed only in a specific and authorized manner
- **system integrity** ⟶ assures that a system can perform its intented function free from unauthorised manipulation

#### tools for integrity
- **backups** ⟶ periodic archival of data
- **checksums** ⟶ computation of a function that maps contents of a file to a numerical value; a checksum depends on the entire content of a file and even a small change is highly likely to generate a different output value
- **data-correcting codes** ⟶ methods for storing data so that small changes can be easily detected and corrected (automatically)

### availability
>[!info] availability
> Ensuring timely and reliable access to / use of information.

#### tools for availability
- **physical protections** ⟶ infrastructure meant to keep information available even in the event of physical challenges
- **computational redundancies** ⟶ computers and storage devices that serve as fallbacks in case of failures